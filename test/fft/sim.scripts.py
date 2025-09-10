
import sys
from importlib import util
def load_file_as_module(name, location):
    sys.path.insert(0,location.rsplit('/', 1)[0])
    spec = util.spec_from_file_location(name, location)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
sys.argv = [ "/home/skataoka26/src/sniper/scripts/stop-by-icount.py", "50000000" ]
load_file_as_module("stop-by-icount","/home/skataoka26/src/sniper/scripts/stop-by-icount.py")

