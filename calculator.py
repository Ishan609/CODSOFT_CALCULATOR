#!/usr/bin/env python
# coding: utf-8

# In[140]:


import tkinter
from tkinter import *


# In[141]:


win=Tk()
win.title("CALCUTOR")
win.geometry("520x514")
win.resizable(False,False)
win.configure(bg="black")


# In[142]:


number1=None
operator=None
number2=None


# In[143]:


def get_data(digit):
    current=label['text']
    new=current+str(digit)
    label.config(text=new)
def bcksp():
    a=label['text']
    a=a[0:len(a)-1]
    label.config(text=a)
def clear():
    a=""
    label.config(text=a)
def get_operator(op):
    global number1,operator
    number1=float(label['text'])
    operator=op
    label.config(text="")
def get_decimal():
    a=label['text']
    a=a+"."
    label.config(text=a)
def get_result():
    global number1,number2,operator
    number2=label['text']
    match operator:
        case '+':
            a=float(number1)+float(number2)
            a=str(a)
            label.config(text=a)
        case '-':
            a=float(number1)-float(number2)
            a=str(a)
            label.config(text=a)
        case "*":
            a=float(number1)*float(number2)
            a=str(a)
            label.config(text=a)
        case "/" :
            if(number2=="0"):
                label.config(text="ERROR")
            else:
                a=float(number1)/float(number2)
                a=str(a)
                label.config(text=a)
        case "%" :
            a=(float(number1)*float(number2))/100
            a=str(a)
            label.config(text=a)
    
    
      


# In[144]:


label=Label(win,width=32,height=2,text="",font=("arial",25))
label.place(x=0,y=0)


# In[145]:


button=Button(win,text="clr",width=5,height=1,font=("arial",30),bg="blue",fg="white",command=lambda:clear())
button.place(x=0,y=85)
button1=Button(win,text="/",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_operator('/'))
button1.place(x=130,y=85)
button2=Button(win,text="%",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_operator('%'))
button2.place(x=260,y=85)
button3=Button(win,text="*",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_operator('*'))
button3.place(x=390,y=85)
button4=Button(win,text="7",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(7))
button4.place(x=0,y=170)
button5=Button(win,text="8",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(8))
button5.place(x=130,y=170)
button6=Button(win,text="9",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(9))
button6.place(x=260,y=170)
button7=Button(win,text="-",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_operator('-'))
button7.place(x=390,y=170)
button8=Button(win,text="4",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(4))
button8.place(x=0,y=255)      
button9=Button(win,text="5",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(5))
button9.place(x=130,y=255) 
button10=Button(win,text="6",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(6))
button10.place(x=260,y=255)
button11=Button(win,text="+",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_operator('+'))
button11.place(x=390,y=255) 
button12=Button(win,text="1",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(1))
button12.place(x=0,y=340)
button13=Button(win,text="2",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(2))
button13.place(x=130,y=340)
button14=Button(win,text="3",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(3))
button14.place(x=260,y=340)
button15=Button(win,text="=",width=5,height=3,font=("arial",30),bg="red",fg="white",command=lambda:get_result())
button15.place(x=390,y= 340)
button16=Button(win,text="0",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_data(0))
button16.place(x=0,y=425)
button14=Button(win,text="bcksp",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:bcksp())
button14.place(x=130,y=425)
button18=Button(win,text=".",width=5,height=1,font=("arial",30),bg="grey",fg="white",command=lambda:get_decimal())
button18.place(x=260,y=425)


# In[ ]:





# In[146]:


win.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




