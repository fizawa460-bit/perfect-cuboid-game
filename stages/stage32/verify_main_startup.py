#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
AUTHORITY=HERE/"management/grf04-hpadj22-joint/verify_grf04_hpadj22_v47_full178_authority_sync.py"
COMMAND_SURFACE=HERE/"verify_command_surface.py"
def replay(path):subprocess.run([sys.executable,str(path)],check=True)
def main():
    replay(AUTHORITY);replay(COMMAND_SURFACE)
    print("PASS: Stage32 MAIN V47 consumes hostile-audited FULL178 numerical census; effectivity and multibranch remain open")
if __name__=="__main__":main()
