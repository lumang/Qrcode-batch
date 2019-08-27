import qrcode
import os 
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename


qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    
)

#choose output directory
def selectPath():
    path_ = askdirectory()
    print(path_)
    pathdir.set(path_)
#choose input file
def selectFile():
    path_ = askopenfilename()
    print(path_)
    pathfile.set(path_)
#QrCode Batch
def QrCodeBatch(pathfile,pathdir):
    file = open(pathfile)
    readlines = file.readlines()
    i=0
    for readline in readlines:
        
        qr.add_data(readline.strip())
        qr.make(fit=True)
        img = qr.make_image()
        filename=pathdir+'.png'
        readline=''
        img.save(filename)
        qr.clear()
        i=i+1
        print('done No. '+str(i))
    print('sucess '+str(i))
    file.close()

root = Tk()
root.title("QrCode Batch")
pathfile = StringVar()
pathdir = StringVar()
Label(root,text = "input file:").grid(row = 0, column = 0)
Entry(root, textvariable = pathfile).grid(row = 0, column = 1)
Button(root, text = "input file", command = selectFile).grid(row = 0, column = 2)

Label(root,text = "output dir:").grid(row = 1, column = 0)
Entry(root, textvariable = pathdir).grid(row = 1, column = 1)
Button(root, text = "outputdir", command = selectPath).grid(row = 1, column = 2)

Button(root,text="QrCode Batch",command=QrCodeBatch).grid(row=2,column = 1)





root.mainloop()
