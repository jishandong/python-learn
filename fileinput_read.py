'read file to standout ,'
'example : ./fileinput_read.py /etc/passwd'
import fileinput
with fileinput.input() as f: #确保不再使用时候文件被关闭
    for line in f:
        print(line,end='')
