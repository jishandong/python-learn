import tkinter
top =tkinter.Tk()
hello = tkinter.Label(top,text='hello world!')
hello.pack()
quit = tkinter.Button(top,text = 'QUIT',
                      command=top.destroy,bg='red',fg='white')
quit.pack(fill=tkinter.X,expand=1)
tkinter.mainloop()

