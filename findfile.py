'os.walk()会为我们便利目录层级，且对于进入的每一个目录返回3个元组。（目录的相对路径，该目录内包含的所有的目录名的，列表该目录内包含所有文件名的列表）'
'find_file, ./findfile.py / hello_world.txt'
import os
import sys
def findfile(start,name):
    for relpath,dirs,files in os.walk(start):
        if name in files:
            full_path = os.path.join(start,relpath,name)
            print(os.path.normpath(os.path.abspath(full_path)))
if __name__=='__main__':
    findfile(sys.argv[1],sys.argv[2])
