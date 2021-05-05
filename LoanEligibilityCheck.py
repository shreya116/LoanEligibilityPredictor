#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from tkinter import *
import joblib as joblib


from joblib import dump, load
import tkinter as tk
from tkinter import messagebox  
win=tk.Tk()
win.configure(background='#D9FCC2')
win.geometry("400x715")
win.title("Loan Eligibility Checker")


# In[ ]:


classifier = joblib.load('loan.h5') 


# In[ ]:


def test1():
    MsgBox = tk.messagebox.showwarning ('warning',ai_var.get(),icon = 'warning')


# In[ ]:



def check():
    msg=StringVar()
    if ai_var.get()=="":
        msg="Applicant's Income field is empty!!"
        Label(win,text=msg,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=100,y=670)

    elif cai_var.get()=="":
        msg="Co-Applicant's Income field is empty!!"
        Label(win,text=msg,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=100,y=670)
        
    elif la_var.get()=="":
        msg="Loan Amount field is empty!!"
        Label(win,text=msg,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=100,y=670)
        
    elif lat_var.get()=="":
        msg="Loan Amount Term field is empty!!"
        Label(win,text=msg,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=100,y=670)
        
    elif ch_var.get()=="":
        msg="Credit history field is empty!!"
        Label(win,text=msg,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=100,y=670)
        
    else:
        test()
        
        


# In[ ]:


def test():
        gen=gen_var.get()
        ms=ms_var.get()
        d=d_var.get()
        edu=edu_var.get()
        se=se_var.get()
        pa=pa_var.get()
        ai=ai_var.get()
        cai=cai_var.get()
        la=la_var.get()
        lat=lat_var.get()
        ch=ch_var.get()
        Prediction = [[gen,ms,d,edu,se,ai,cai,la,lat,ch,pa]]
        result = classifier.predict(Prediction)
        print(result)
        if result[0]==1:
            MsgBox = tk.messagebox.showwarning ('warning',"Congratulations!! You are eligible for loan",icon = 'warning')

        else:
            MsgBox = tk.messagebox.showwarning ('warning',"Sorry! You are not eligible for loan",icon = 'warning')
#     execfile('loanclassification.py')
#     y_pred = pickle.load(sys.stdin)


# In[ ]:





# In[ ]:


def reset():
    gen_var.set("")
    ms_var.set("")
    d_var.set("")
    edu_var.set("")
    se_var.set("")
    pa_var.set("")
    ai_var.set("")
    cai_var.set("")
    la_var.set("")
    lat_var.set("")
    ch_var.set("")


# In[ ]:





# In[ ]:


gen_var=tk.IntVar()
gen=Label(win, 
        text="Gender:",
        background='#D9FCC2',
          font=('Helvetica 13 bold'),
        padx = 20).pack()
# Label.grid(row=0,column=0)

gen_rb=tk.Radiobutton(win, 
               text="Male",
               padx = 30, 
               variable=gen_var,
               background='#D9FCC2',
               value=1).pack(anchor=tk.W)
# R1.grid(row=1,column=0)

gen_rb=tk.Radiobutton(win, 
               text="Female",
               padx = 20, 
               variable=gen_var, 
            background='#D9FCC2',
               value=0).pack(anchor=tk.W)
# R1.grid(row=2,column=0)


# In[ ]:


ms_var=tk.IntVar()
ms=Label(win, 
        text="Are you Married?",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

ms_rb=tk.Radiobutton(win, 
               text="Yes",
               padx = 20,  
               background='#D9FCC2',
               variable=ms_var,
               value=1).pack(anchor=tk.W)
# R1.tk.place(x=12,y=20)

ms_rb=tk.Radiobutton(win, 
               text="No",
               padx = 20, 
               variable=ms_var,
               background='#D9FCC2',
               value=0).pack(anchor=tk.W)
# R2.tk.place(x=12,y=20)


# In[ ]:


d_var=tk.IntVar()
d=tk.Label(win, 
        text="Do you any dependents?",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

d_rb=tk.Radiobutton(win, 
               text="Yes",
               padx = 20, 
               variable=d_var, 
               background='#D9FCC2',
               value=1).pack(anchor=tk.W)
# R1.tk.place(x=12,y=20)

d_rb=tk.Radiobutton(win, 
               text="No",
               padx = 20, 
               variable=d_var,
               background='#D9FCC2',
               value=0).pack(anchor=tk.W)


# In[ ]:


edu_var=tk.DoubleVar()
edu=tk.Label(win, 
        text="Are you a graduate?",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

edu_rb=tk.Radiobutton(win, 
               text="Yes",
               padx = 20, 
               variable=edu_var, 
               background='#D9FCC2',
               value=1).pack(anchor=tk.W)
# R1.tk.place(x=12,y=20)

edu_rb=tk.Radiobutton(win, 
               text="No",
               padx = 20, 
               variable=edu_var,
               background='#D9FCC2',
               value=0).pack(anchor=tk.W)


# In[ ]:


se_var=tk.IntVar()
se=tk.Label(win, 
        text="Are you Self-Employed?",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

se_rb=tk.Radiobutton(win, 
               text="Yes",
               padx = 20, 
               variable=se_var, 
               background='#D9FCC2',
               value=1).pack(anchor=tk.W)
# R1.tk.place(x=12,y=20)

se_rb=tk.Radiobutton(win, 
               text="No",
               padx = 20, 
               variable=se_var,
               background='#D9FCC2',
               value=0).pack(anchor=tk.W)


# In[ ]:


pa_var=tk.IntVar()
pa=tk.Label(win, 
        text="How is the Property Area?",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

pa_rb=tk.Radiobutton(win, 
               text="Urban/SemiUrban",
               padx = 20, 
               variable=pa_var, 
               background='#D9FCC2',
               value=1).pack(anchor=tk.W)
# R1.tk.place(x=12,y=20)

pa_rb=tk.Radiobutton(win, 
               text="Rural",
               padx = 20, 
               variable=pa_var,
               background='#D9FCC2',
               value=0).pack(anchor=tk.W)


# In[ ]:


ai_var=tk.StringVar()
ai=tk.Label(win, 
        text="Please enter Applicant's Income:",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2').pack()
# Label.tk.place(x=12,y=20)

ai_entrybox=tk.Entry(win,
               width=20,
               textvariable=ai_var,
               background='light cyan',
               ).pack(anchor=tk.W)


# In[ ]:


cai_var=tk.StringVar()
cai=tk.Label(win, 
        text="Please enter Co-Applicant's Income:",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2').pack()
# Label.tk.place(x=12,y=20)

cai_entrybox=tk.Entry(win,
               width=20,
               textvariable=cai_var, 
               background='light cyan',
               ).pack(anchor=tk.W)


# In[ ]:


la_var=tk.StringVar()
la=tk.Label(win, 
        text="Please enter Loan Amount:",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

la_entrybox=tk.Entry(win,
               width=20,
               textvariable=la_var, 
               background='light cyan',
               ).pack(anchor=tk.W)


# In[ ]:


lat_var=tk.StringVar()
lat=tk.Label(win, 
        text="Please enter Loan Amount Term in days:",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

lat_entrybox=tk.Entry(win,
               width=20,
               textvariable=lat_var, 
               background='light cyan',
               ).pack(anchor=tk.W)


# In[ ]:


ch_var=tk.StringVar()
ch=tk.Label(win, 
        text="Enter Credit History:",
        font=('Helvetica 13 bold'),
        justify = tk.LEFT,
        background='#D9FCC2',
        padx = 20).pack()
# Label.tk.place(x=12,y=20)

ch_entrybox=tk.Entry(win,
               width=20,
               textvariable=ch_var, 
               background='light cyan',
               ).pack(anchor=tk.W)


# In[ ]:


submit = Button(win, text="Submit", width="12",height="1",bg="brown",command = check,font = ("Calibri 12 ")).pack(anchor=tk.W)
reset = Button(win, text="Reset", width="12",height="1",command = reset,font = ("Calibri 12 ")).pack(anchor=tk.W)


# In[ ]:


win.mainloop()

