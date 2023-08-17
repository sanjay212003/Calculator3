from tkinter import *
root=Tk()
root.title('CALCULATOR BY SANJAY')
root.geometry('450x560')

def click(x):
    global scvalue
    text=x.widget.cget('text')
    print(text)
    if text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(scvalue.get())
        scvalue.set(value)
        screen.update()
    elif text=='CE':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,padx=20,pady=30)
f=Frame(root,bg='grey')
b=Button(f,text='9',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='8',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='7',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='+',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

f.pack(fill=X)

f=Frame(root,bg='grey')
b=Button(f,text='6',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='5',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='4',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='-',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

f.pack(fill=X)

f=Frame(root,bg='grey')
b=Button(f,text='3',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='2',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='1',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='*',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

f.pack(fill=X)


f=Frame(root,bg='grey')
b=Button(f,text='CE',font='lucida 18 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='0',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='=',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text='/',font='lucida 30 bold')
b.pack(side=LEFT,padx=28,pady=10)
b.bind('<Button-1>',click)

f.pack(fill=X)



root.mainloop()
