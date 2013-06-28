from PIL import Image
from pylab import *

im = array(Image.open("NYCity.jpg").convert("L"))
gray()
contour(im, origin='image')
show()
