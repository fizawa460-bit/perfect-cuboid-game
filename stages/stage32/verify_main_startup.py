#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
AUTHORITY=HERE/"management/178-fullsupport-successor/verify_post_v48_178_fullsupport_384_v49_main_authority_sync.py"
V50_AUTHORITY=HERE/"management/unibranch-node-hurwitz/verify_v50_main_authority_sync.py"
COMMAND_SURFACE=HERE/"verify_command_surface.py"
LIVE_CONTROL=HERE/"verify_live_control.py"
def replay(path):subprocess.run([sys.executable,str(path)],check=True)
def main():
    replay(AUTHORITY);replay(V50_AUTHORITY);replay(LIVE_CONTROL);replay(COMMAND_SURFACE)
    print("PASS: Stage32 MAIN V50 consumes hostile-audited UNIBRANCH-NODE-HURWITZ (511353002049 compressed terminals, 530 strata) as same-population MIN over V49; effectivity and multibranch remain open")
if __name__=="__main__":main()
