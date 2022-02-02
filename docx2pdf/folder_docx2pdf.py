import os
from docx2pdf import convert

directory = input("Target folder's name: ")
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)
if not os.path.exists(path):
    os.mkdir(path)
if os.path.exists(path):
    try:
        convert(parent_dir,path)
        input('Task Completed')
        os.system('pause')
    except:
        print('Bad file: one of the files seems to be corrupted')
        os.system('pause')