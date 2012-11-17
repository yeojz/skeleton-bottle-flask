#Merging third party library
import sys, os
libdir = "thirdparty"
libdir_path = os.path.join(os.path.dirname(__file__), libdir)
sys.path.insert(0, libdir)
