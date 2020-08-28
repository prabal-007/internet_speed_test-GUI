from speedtest import Speedtest
from tkinter import *

def refresh():
    var1.set(st.download())
    var2.set(st.upload())
st = Speedtest()
root = Tk()
root.title('Internet speed test')
root.geometry('400x400')
Label(text='Download Speed',font='arial 20 bold').grid(column=2,padx=30,pady=10)
var1=IntVar()
var1.set(st.download())
var2=IntVar()
var2.set(st.upload())
Entry(root, font='arial 16 bold', textvariable=var1).grid(row=1,column=2,padx=30,pady=10)
Label(text='Upload Speed',font='arial 20 bold').grid(row=2,column=2,padx=30,pady=10)
Entry(root,font='arial 16 bold', textvariable=var2).grid(row=3,column=2,padx=30,pady=10)

Button(text='Refresh',font='arial 15 bold', command=refresh).grid(row=4,column=2,pady=5)

root.mainloop()
