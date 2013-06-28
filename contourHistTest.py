from PIL import Image
from pylab import *

im = array(Image.open('NYCity.jpg').convert('L')
#figure()
hist(im.flatten(),128)
show()

