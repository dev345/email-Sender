#bkthakur
#amit.cetpa@gmail.com
import os
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import *
from PIL import Image,ImageTk
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
a=Tk(className='email sender')
a.geometry('1100x800')

V=StringVar()
Rec=StringVar()
subject=StringVar()
userID=StringVar()
pswd=StringVar()
img=PhotoImage(file='C:/Users/91889/Pictures/Saved Pictures/Sketches 204.png')

l=Label(a,image=img)
l.place(x=0,y=0)
######################function provides-written data on the GUI by the user,connect the server with mail,send the data through it#######################################
def fun1():
    print(str(userID.get()))
    print(str(pswd.get()))
    print(str(Rec.get()))
    print(str(subject.get()))
    print(e3.get('1.0',END))
    print(a)
    mail=MIMEMultipart()
    mail['from']=str(userID.get())###sender's name
    mail['to']=str(Rec.get())####receiver's name
    mail['subject']=str(subject.get())####subject /topic
    mail.attach(MIMEText(e3.get('1.0',END),'plain'))###messsage to be send
    att=MIMEBase('application','octet-stream')
    att.set_payload((open(V.get(),"rb")).read())###file to be sent
    email.encoders.encode_base64(att)
    att.add_header('content-Disposition','attachment; filename=%s'%os.path.basename(V.get()))###file name 
    mail.attach(att)
    client=smtplib.SMTP('smtp.gmail.com',587)
    client.starttls()
    client.login(str(userID.get()),str(pswd.get()))
    client.sendmail(str(userID.get()),str(Rec.get()),mail.as_string())

x=Label(a,text='online correspondence',font=('Monotype Corsiva',40,'italic'),bg='#F8F8F8',fg='black')
x.place(x=350,y=0)

l4=Label(a,text='User ID:',bg='#F8F8F8',font=('times',20))
l4.place(x=600,y=90)
e4=Entry(a,width=50,textvariable=userID)
e4.place(x=700,y=100)

l5=Label(a,text='Password:',bg='#F8F8F8',font=('times',20))
l5.place(x=580,y=140)
e5=Entry(a,width=50,textvariable=pswd,show="*")
e5.place(x=700,y=150)

l1=Label(a,text='Send to:',bg='#F8F8F8',font=('times',20))
l1.place(x=600,y=185)
e1=Entry(a,width=50,textvariable=Rec)
e1.place(x=700,y=195)

l2=Label(a,text='Subject:',bg='#F8F8F8',font=('times',20))
l2.place(x=600,y=240)
e2=Entry(a,width=50,textvariable=subject)
e2.place(x=700,y=250)

l3=Label(a,text='Message:',font=('times',20),bg="#F8F8F8")
l3.place(x=600,y=310)
e3=Text(a,width=40,height=20)
e3.place(x=705,y=300)

b2=Button(a,activebackground="#F8F8F8",activeforeground="black",bd=3,text="upload",font=(10),command=lambda :V.set(filedialog.askopenfilenames(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))))
b2.place(x=800,y=650)
############################################function to clear all the written data###############################################################################
def fun():
    e5.delete(0,END)
    e4.delete(0,END)
    e3.delete('1.0',END)
    e2.delete(0,END)
    e1.delete(0,END)
b3=Button(a,activeforeground="black",bd=3,font=(10),text='clear',command=fun)
b3.place(x=710,y=650)

b1=Button(a,activebackground="#F8F8F8",activeforeground="black",bd=3,text="send",font=(10),command=fun1)
b1.place(x=910,y=650)

a.mainloop()
