from tkinter import *
import sys
import time
from networktables import NetworkTables as nt
import logging



#ip Address
ip = "XX.XX.XX.XX" #Replace with Valid IP

'''Network Tables Communication'''

class NetworkTables:
    def __init__(self, sd, scale, switch):
        self.sd = nt.getTable("SmartDashboard")
        self.scale = nt.getTable("Scale")
        self.scale = nt.getTable("Switch")
        
        
def posting():
     sd = nt.getTable("SmartDashboard")
     sd = nt.getTable("Scale")
     sd = nt.getTable("Switch")
     sd.addEntryListener(valueChanged)

     while True:
          #print('robotTime:', sd.getNumber('robotTime', 'N/A'))
     
          print("Posting...")
     
          #sd.putNumber('Motor', 1)
          print(sd.getNumber('Motor', 4))
          time.sleep(1)
          print(sd.putNumber('Motor', 1))
          time.sleep(5)
          print(sd.putNumber('Motor', 0))
          time.sleep(1)
          print(sd.putNumber('Scale\X', 1))
          time.sleep(1)
          print(sd.putNumber('Scale\Y', 1))
          print(sd.putNumber('Scale\Z', 1))
          time.sleep(1)
          print(sd.putNumber('Scale\View', 1))
          time.sleep(1)
          print(sd.putNumber('Scale\Color', 1))
          time.sleep(1)
          print(sd.putNumber('Switch\Y', 1))
          print(sd.putNumber('Switch\Z', 1))
          time.sleep(1)
          print(sd.putNumber('Switch\View', 1))
          time.sleep(1)
          print(sd.putNumber('Switch\Color', 1))
          time.sleep(1)
          print(sd.putNumber('Switch\X', 1))
          time.sleep(1)
          #print(sd.getBoolean('bool','N/A'))      
          time.sleep(1)
#Create the GUI
root = Tk()
root.minsize(width=500,height=500)
root.title("Network Tables!")
frame = Frame(root, height=300, width=300)


label = Label(root,text="Control Panel")
label.pack()
button = Button(root, text="Post to SmartDashboard.", fg="Green", bg="White", command=posting)
button1= Button(root, text="Stop", fg="Red", bg="White", command=quit)
button1.pack()
def get():
     e1 = entry.get()
     e2= entry.get()
     e3 = entry.get()
     e4 = entry.get()
     e5 = entry.get()
     e6 = entry.get()
     e7 = entry.get()
     e8 = entry.get()
     e9 = entry.get()
     e0 = entry.get()
     entry.delete(0, 'end')
     entry2.delete(0, 'end')
     entry3.delete(0, 'end')
     entry4.delete(0, 'end')
     entry5.delete(0, 'end')
     entry6.delete(0, 'end')
     entry7.delete(0, 'end')
     entry8.delete(0, 'end')
     entry9.delete(0, 'end')
     entry0.delete(0, 'end')
     
     return e1,e2,e3,e4,e5,e6,e7,e8,e9,e0

'''Entry'''
labelentry1 = Label(root, text= "ScaleX")
labelentry2 = Label(root, text="ScaleY")
labelentry3 = Label(root, text="ScaleZ")
labelentry4 = Label(root, text="ScaleView")
labelentry5 = Label(root, text= "ScaleColor")
labelentry6 = Label(root, text= "SwitchX")
labelentry7 = Label(root, text="SwitchY")
labelentry8= Label(root, text="SwitchZ")
labelentry9 = Label(root, text="SwitchView")
labelentry0 = Label(root, text= "SwitchColor")

labelentry1.pack(side="left")
labelentry2.pack(side="left")
labelentry3.pack(side="left")
labelentry4.pack(side="left")
labelentry5.pack(side="left")
labelentry6.pack(side="left")
labelentry7.pack(side="left")
labelentry8.pack(side="left")
labelentry9.pack(side="left")
labelentry0.pack(side="left") 

entry = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)
entry7 = Entry(root)
entry8 = Entry(root)
entry9= Entry(root)
entry0 = Entry(root)

entry.pack()
entry2.pack()
entry3.pack()
entry4.pack()
entry5.pack()
entry6.pack()
entry7.pack()
entry8.pack()
entry9.pack()
entry0.pack()

ebutton = Button(root, text="Enter", fg="Blue", bg="White", command=get)


ebutton.pack(side="left")

button.pack(side="top")

        








'''GUI'''
Label(text='Control Panel', relief=RIDGE, width=15).grid(row=0, column=0)
Button(text="Post to SmartDashboard.", fg="Green", bg="White").grid(row=1, column=0)

labelStrings = ["x", "y", "z", "view", "color"]

nScaleEntries = 5
scaleEntries = []
for i in range(nScaleEntries):
    label = Label(text=labelStrings[i]).grid(row=i+2, column=0)

    entry = Entry().grid(row=i+2, column=1)
    scaleEntries.append(entry)

nSwitchEntries = 5
switchEntries = []
for i in range(nSwitchEntries):
    label = Label(text=labelStrings[i]).grid(row=i+2, column=2)
    entry = Entry().grid(row=i+2, column=3)
    switchEntries.append(entry)

nPostingEntries = 10
postingEntries = []
for i in range(nPostingEntries):
    entry = Entry().grid(row=i+2, column=4)
    postingEntries.append(entry)

Button(text="Stop", fg="Red", bg="White", command=quit).grid(row=13, column=0)


mainloop()
