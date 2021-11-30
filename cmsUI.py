from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('1000x1200')  
tkWindow.title('CMS LOGIN PAGE')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").pack()
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=1, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=15, column=1)  

tkWindow.mainloop()