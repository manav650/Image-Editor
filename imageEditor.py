from PIL import ImageEnhance, ImageFilter
import PIL.Image
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import imgbasic as imgbsc

win = Tk()
win.title("Image Editor")
font_format = ("Helvetica",15,"bold")



label_filename = Label(win, text = "Enter Filename:",font = font_format)
label_filename.grid(row=0, column=0, sticky=W)
fileNameVar = StringVar()
entry_filename = Entry(win, textvariable = fileNameVar)
entry_filename.grid(row=0, column=1, ipadx=75, ipady=5, padx=5, pady=5)


label_chooseDirectory = Label(win, text = "Choose Directory: ", font = font_format)
label_chooseDirectory.grid(row=1, column=0, sticky=W)
directoryVar = StringVar()
combobox_chooseDirectory = ttk.Combobox(win, width=40, textvariable=directoryVar, state="readonly")
combobox_chooseDirectory['values'] = ('None', 'Downloads','Desktop')
combobox_chooseDirectory.current(0)
combobox_chooseDirectory.grid(row=1, column=1, ipadx=5, ipady=5, padx=5, pady=5)
enterDirectory = Label(win, text="or enter path: ",font = ("Helvetica",12,"italic"))
enterDirectory.grid(row=2, column=0)
fileDirectoryVar = StringVar()
fileDirectory = Entry(win, textvariable = fileDirectoryVar)
fileDirectory.grid(row=2, column=1, ipadx=75, ipady=5, padx=5, pady=5)



sep = ttk.Separator(win)
sep.grid(row=3,columnspan=2, sticky='ew')

#####################################################################################################
func1 = IntVar()
func2 = IntVar()
func3 = IntVar()
func4 = IntVar()
func5 = IntVar()
func6 = IntVar()

color_button = ttk.Checkbutton(win, text = "Color", variable=func1).grid(
    row=4, column=0, ipadx=5, ipady=5, padx=5, pady=5)
conrast_button = ttk.Checkbutton(win, text = "Contrast", variable=func2).grid(
    row=4, column=1, ipadx=5, ipady=5, padx=5, pady=5)
brightness_button = ttk.Checkbutton(win, text = "Brighness", variable=func3).grid(
    row=5, column=0, ipadx=5, ipady=5, padx=5, pady=5)
sharpness_button = ttk.Checkbutton(win, text="Sharpness", variable=func4).grid(
    row=5, column=1, ipadx=5, ipady=5, padx=5, pady=5)
BnW_button = ttk.Checkbutton(win, text = "Black & White", variable=func5).grid(
    row=6, column=0, ipadx=5, ipady=5, padx=5, pady=5)
reduce_button = ttk.Checkbutton(win, text = "Reduce Size", variable=func6).grid(
    row=6, column=1, ipadx=5, ipady=5, padx=5, pady=5)
#####################################################################################################

factorVar = DoubleVar()
label_factor = Label(win, text = "Factor:",font = font_format)
label_factor.grid(row=7, column=0, sticky=W)
entry_factor = Entry(win, textvariable = factorVar)
entry_factor.grid(row=7, column=1, ipadx=75, ipady=5, padx=5, pady=5)


label_fileExt = Label(win, text = "File Extension:",font = font_format)
label_fileExt.grid(row=8, column=0, sticky=W)
combobox_fileExt = ttk.Combobox(win, width=40, state="readonly")
combobox_fileExt['values'] = ('Default', '.jpg', '.png', '.jpeg', '.pdf')
combobox_fileExt.current(0)
combobox_fileExt.grid(row=8, column=1, ipadx=5, ipady=5, padx=5, pady=5)




'''
#####################################################################################################
def change_color():
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Color(img)
    newFilePath = 'C:/Users/manav/Desktop/edited/' + filename + extension
    enhancer.enhance(factor).save(newFilePath)
  
    
def change_contrast():
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Contrast(img)
    newFilePath = 'C:/Users/manav/Desktop/edited/' + filename + extension
    enhancer.enhance(factor).save(newFilePath)



def change_brightness():
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Brightness(img)
    newFilePath = 'C:/Users/manav/Desktop/edited/' + filename + extension
    enhancer.enhance(factor).save(newFilePath)



def change_sharpness():
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Sharpness(img)
    enhancer.enhance(factor).save(newFilePath)


    
def change_bnw():
    img = PIL.Image.open(imageName)
    enhancer = ImageEnhance.Color()
    newFilePath = 'C:/Users/manav/Desktop/edited/' + filename + extension
    enhancer.enhance(0.0).save(newFilePath)


    
def change_size():
    img = PIL.Image.open(imageName)
    img.reduce()
    newFilePath = 'C:/Users/manav/Desktop/edited/' + filename + extension
    img.save(newFilePath)
#####################################################################################################
'''
    
def submit():
    filename,extension = fileNameVar.get().split('.')
    
        
    #get_extension()
    imageName = 'D:/wallpaper/animal_umbreon_pokemon_83631_1366x768.jpg'
    directory = directoryVar.get()
    factor = factorVar.get()
    extension = '.' + extension
    
    
    
    if directory == 'None':
        filePath = fileDirectoryVar.get()
        imageName = filePath + filename + extension
    
    elif directory == 'Desktop':
        imageName = 'C:/Users/manav/Desktop/' + filename + extension
        
    elif directory == "Downloads":
        imageName = 'C:/Users/manav/Downloads/' + filename + extension
        
    if combobox_fileExt.get() == "Default":
        pass
    else:
        extension = combobox_fileExt.get()
        
    entry_filename.clipboard_clear()
    
    newFilePath = 'C:/Users/manav/Pictures/edited/' + filename + extension

    
    print(imageName + ' ' + newFilePath + ' ' + str(func1) + ' ' + str(func2))
    
    if func1.get() == 1: 
        imgbsc.change_color(imageName, newFilePath, factor)
        
    if func2.get() == 1:
        imgbsc.change_contrast(imageName, newFilePath, factor)
        
    if func3.get() == 1:
        imgbsc.change_brightness(imageName, newFilePath, factor)
        
    if func4.get() == 1:
        imgbsc.change_sharpness(imageName, newFilePath, factor)
        
    if func5.get() == 1:
        imgbsc.change_bnw(imageName, newFilePath, factor)
        
    if func6.get() == 1:
        imgbsc.change_size(imageName, newFilePath, int(factor))

    messagebox.showinfo("Success", "Image edited")
    



submit_button = Button(win, text = "Sumbit", font=font_format, command=submit)
submit_button.grid(row=9, column=1)


    

win.mainloop()
