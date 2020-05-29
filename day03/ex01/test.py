from ImageProcessor import ImageProcessor
imgP = ImageProcessor()
arr = imgP.load("duck.png")
print(arr)
imgP.display(arr)