from PIL import Image
from pylab import *

im = array(Image.open("NYCity.jpg").convert("L"))
gray()
contour(im, origin='image')
print "this is new thing for me, uploading to github"
show()
