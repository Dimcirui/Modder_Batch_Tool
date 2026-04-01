import sys
import site

sys.path.insert(0, site.getusersitepackages())

try:
    from PIL import Image
    from PIL import ImageChops

    pil_exist = True
except ImportError:
    pil_exist = False

smc_pi = False

CL_OBJECT = 0
CL_MATERIAL = 1
CL_SEPARATOR = 2
