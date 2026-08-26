#!/usr/bin/env python3
"""Side-effect-free pinned Testa--Stoll source/Magma transport helper."""
import hashlib
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UPSTREAM_URL=(
 "https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/"
 "51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
)
UPSTREAM_BLOB="0422b69847f2afb97cb7b3ed02ebef91279f61b1"
SKIP_START="// Genus 3 hyperelliptic curves of degree 8"
SKIP_END="// Set up the intersection pairing"
STOP_MARKER="// The automorphism group (see Proposition 4)"
MAGMA_URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER="https://magma.maths.usyd.edu.au/calc/"
RETRY_DELAYS=(0,5,15,30)

def git_blob_sha(data):
 return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def urlopen_retry(req,timeout,label):
 last=None
 for attempt,delay in enumerate(RETRY_DELAYS,1):
  if delay: time.sleep(delay)
  try: return urllib.request.urlopen(req,timeout=timeout),attempt
  except (urllib.error.URLError,TimeoutError) as exc:
   last=exc; print(f"{label} transient failure {attempt}/{len(RETRY_DELAYS)}: {exc}")
 raise last

def load_pinned_source():
 req=urllib.request.Request(UPSTREAM_URL,headers={"User-Agent":"perfect-cuboid-stage33/2.6"})
 resp,attempt=urlopen_retry(req,60,"pinned Stoll source")
 with resp: raw=resp.read()
 got=git_blob_sha(raw)
 if got!=UPSTREAM_BLOB: raise SystemExit(f"upstream blob mismatch {got}")
 text=raw.decode("utf-8")
 a=text.index(SKIP_START); b=text.index(SKIP_END,a); c=text.index(STOP_MARKER,b)
 core=text[:a]+"\n// Stage33-07 skips unused degree-8 curves.\n"+text[b:c]
 return text,core,got,attempt

def run_magma(code,timeout,label,user_agent="perfect-cuboid-stage33/2.6"):
 payload=urllib.parse.urlencode({"input":code}).encode()
 req=urllib.request.Request(MAGMA_URL,data=payload,headers={
  "Content-Type":"application/x-www-form-urlencoded",
  "Accept":"text/html, application/xml, application/xhtml+xml",
  "Referer":MAGMA_REFERER,"User-Agent":user_agent},method="POST")
 resp,attempt=urlopen_retry(req,timeout,label)
 with resp: raw=resp.read().decode("utf-8",errors="replace")
 root=ET.fromstring(raw); lines=[]
 for result in root.findall(".//results"):
  for line in result.findall(".//line"): lines.append("".join(line.itertext()))
 return "\n".join(lines)+"\n",attempt
