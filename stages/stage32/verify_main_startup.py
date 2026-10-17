#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
AUTHORITY=HERE/"management/178-fullsupport-successor/verify_post_v48_178_fullsupport_384_v49_main_authority_sync.py"
V50_AUTHORITY=HERE/"management/unibranch-node-hurwitz/verify_v50_main_authority_sync.py"
V51_AUTHORITY=HERE/"management/hpadj22-unibranch/verify_v51_main_authority_sync.py"
V52_AUTHORITY=HERE/"management/fixed-direction-certificates/verify_v52_main_authority_sync.py"
COMMAND_SURFACE=HERE/"verify_command_surface.py"
LIVE_CONTROL=HERE/"verify_live_control.py"
def replay(path):subprocess.run([sys.executable,str(path)],check=True)
def main():
    replay(AUTHORITY);replay(V50_AUTHORITY);replay(V51_AUTHORITY);replay(V52_AUTHORITY);replay(LIVE_CONTROL);replay(COMMAND_SURFACE)
    print("PASS: Stage32 MAIN V52 consumes hostile-audited FIXED-DIRECTION-CERTIFICATES (726240487 compressed terminals, strata upper bound 530) as same-population per-row MIN with V51; effectivity and multibranch remain open")
if __name__=="__main__":main()
