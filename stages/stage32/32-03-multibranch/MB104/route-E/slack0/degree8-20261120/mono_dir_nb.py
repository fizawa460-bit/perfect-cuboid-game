"""fastmono mono_dir.py with the compiled tracker (track_nb.py) installed; same arguments and outputs."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); FM = os.path.join(HERE, '..', 'fastmono-20261119')
sys.path.insert(0, HERE); sys.path.insert(0, FM); sys.path.insert(0, os.path.join(FM, '../speedup-20261118'))
import mono_dir, track_nb
track_nb.install()
if __name__ == '__main__': mono_dir.main()
