# Maintainer: an truong
# version: v.0.0
from tkinter import filedialog
from tkinter import *
import shutil,os,glob

root = Tk()
#root.wm_withdraw() # this completely hides the root window
def callback():
#    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    sourceFiles =  filedialog.askopenfilenames(initialdir="/data",title="Select files to copy")
    dstDir = filedialog.askdirectory(initialdir="/data",title="Select destination directory")
    #print('Destination directory: ',root.directory)
#    if sourceFiles:
#        srcDir = os.path.dirname(sourceFiles[0])
    for file_ in sourceFiles:
        fileName = os.path.basename(file_)
        desFile = os.path.join(dstDir, fileName)
        print ('...Copying {} to {}'.format(file_, desFile))
        shutil.copy(file_, desFile)
    
    root.destroy()

Button(text='File Copy', command=callback).pack(fill=X)
root.mainloop()
