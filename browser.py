'加载web浏览器，并且打开一个网页'
import webbrowser
'open the page in a new browser windows'
c1=webbrowser.open('http://www.baidu.com')
print(c1)
'open the page in a new browser tab'
c2=webbrowser.open_new_tab('http://www.baidu.com')
print(c2)
