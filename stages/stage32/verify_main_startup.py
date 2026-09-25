#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
AUTHORITY=HERE/"management/178-fullsupport-successor/verify_post_v48_178_fullsupport_384_v49_main_authority_sync.py"
COMMAND_SURFACE=HERE/"verify_command_surface.py"
def replay(path):subprocess.run([sys.executable,str(path)],check=True)
def main():
    replay(AUTHORITY);replay(COMMAND_SURFACE)
    print("PASS: Stage32 MAIN V49 consumes hostile-audited POST-V48 178 384-coordinate same-population bound replacement; effectivity and multibranch remain open")
if __name__=="__main__":main()
