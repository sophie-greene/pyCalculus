from os import listdir

import os

def ren(fo):
    #fn=''.join([i for i in s if not i.isdigit()])
    fn=fo.translate(None,"")
    print(fo +" to "+fn)
    os.rename(fo, fn)
def main():
    dirs="/home/some/"
    lst=listdir(dirs)
    cDir=os.curdir
    os.chdir(dirs)
    for file in lst:
        ren(file)
    os.chdir(cDir)
main()