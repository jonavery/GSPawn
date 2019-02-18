from PIL import Image

def square(img): #square img with blank space
    size = (max(img.size),)*2
    layer = Image.new('RGB', size, (255,255,255))
    layer.paste(img, tuple(map(lambda x:int((x[0]-x[1])/2), zip(size, img.size))))
    return layer
