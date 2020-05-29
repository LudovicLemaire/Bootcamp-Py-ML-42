from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

imP = ImageProcessor()
cF = ColorFilter()
arr = imP.load("../ex01/pixel.png")
#imP.display(arr)

#result = cF.invert(arr)
#imP.display(result)

#result = cF.to_blue(arr)
#imP.display(result)
arr = imP.load("../ex01/duck.png")
#
result = cF.to_green(arr)
imP.display(result)
#
result = cF.to_red(arr)
imP.display(result)