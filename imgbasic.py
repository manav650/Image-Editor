import PIL.Image
from PIL import ImageEnhance



def change_color(imageName, newFilePath, factor):
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Color(img)
    enhancer.enhance(factor).save(newFilePath)
  
    
def change_contrast(imageName, newFilePath, factor):
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Contrast(img)
    enhancer.enhance(factor).save(newFilePath)



def change_brightness(imageName, newFilePath, factor):
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Brightness(img)
    enhancer.enhance(factor).save(newFilePath)



def change_sharpness(imageName, newFilePath, factor):
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Sharpness(img)
    enhancer.enhance(factor).save(newFilePath)


    
def change_bnw(imageName, newFilePath, factor):
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Color(img)
    enhancer.enhance(0).save(newFilePath)


    
def change_size(imageName, newFilePath, factor):
    img = PIL.Image.open(imageName)
    img.thumbnail((int(factor),int(factor)))
    img.save(newFilePath)