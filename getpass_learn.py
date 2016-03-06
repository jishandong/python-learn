import getpass
user = getpass.getuser()#获取shell中的用户名
print(user)
passwd = getpass.getpass()
if passwd == '123':
    print ('yes,entered')
else:
    print ('no')
