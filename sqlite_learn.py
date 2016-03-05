' python sqlite3 '
import sqlite3
cxn = sqlite3.connect('test.db')#connect local datebase test.db
cur = cxn.cursor()              #游标对象
cur.execute('CREATE TABLE users(login VARCHAR(8),uid INTEGER)') 
cur.execute('INSERT INTO users VALUES("lilei",100)')
cur.execute('INSERT INTO users VALUES("hanmeimei",110)')
cur.execute('SELECT * FROM users')
for eachuser in cur.fetchall():  #返回结果集合中剩下的内容
    print (eachuser)
cur.execute('DROP TABLE users')
cur.close()
cxn.commit() #提交当前事物
cxn.close()
    
