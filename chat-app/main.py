import socket
import time
import threading
from tkinter import *


root = Tk()


root.geometry("300x500")
root.config(bg="white")


# background_image=PhotoImage("bg.png")
# background_label = Label(image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


def func():
     t = threading.Thread(target=recv)
     t.start()

def recv():
     listensocket = socket.socket()
     port = 3050
     maxconnection = 99
     ip = socket.gethostname()
     print(ip)

     listensocket.bind(('',port))
     listensocket.listen(maxconnection)
     (clientsocket,address) = listensocket.accept()

     while True:
          sendermsg = clientsocket.recv(1024).decode()
          if not sendermsg=="":
               time.sleep(5)
               lstbx.insert(0,"Client : ",+sendermsg)




def threadsendmsg():
     pass



startchatImage = PhotoImage(file="sc.png")

buttons = Button(root,text="Start Chat",command=func,borderwidth=2)
buttons.place(x=100,y=15)


message = StringVar()
messagebox = Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)


sendImg = PhotoImage(file="send.png")

sendmessagebutton = Button(root,text="send",command=threadsendmsg,borderwidth=1)
sendmessagebutton.place(x=260,y=440)

lstbx = Listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)




root.mainloop()
















