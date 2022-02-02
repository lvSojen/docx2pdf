import os
from docx2pdf import convert

directory = "outputs"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)
if not os.path.exists(path):
    os.mkdir(path)
if os.path.exists(path):
    try:
        convert(parent_dir,path)
        print('Task Completed')
        os.system('pause')
    except:
        print('Bad file: one of the files seems to be corrupted')
        os.system('pause')