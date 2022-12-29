WORKING_DIR = "/home/iratherfear/Desktop/CPTIMER/"
from tkinter import *
import sys
import time
import os

global count
count =0

EMPTY_STRING = ""
for i in range(100):
    EMPTY_STRING += " "

OPTIONS_MENU = ["RATING"]
for itr in range(500, 4000, 100):
    OPTIONS_MENU.append(str(itr))

path1 = ""
path2 = ""

def delete_last_line():
    if path1 == "":
        print("No file selected")
        return

    with open(path1, 'r', encoding='utf-8') as file:
        data = file.readlines() 
    if len(data) == 0:
        print("Nothing to delete")
        return
    data.pop()
    print("DELETED")
    with open(path1, 'w', encoding='utf-8') as file:
        file.writelines(data)
    file.close()

def createFile(SHEET_NAME):
    global path1
    global path2
    path1 = WORKING_DIR + SHEET_NAME + ".csv"
    path2 = WORKING_DIR + SHEET_NAME + "_backup" + ".csv"

    if os.path.isfile(path1) == False:
        file = open(path1, "w")
        file.write("PROBLEM,TIME")
        file.write("\n")
        file.close()
    if os.path.isfile(path2) == False:
        file = open(path2, "w")
        file.write("PROBLEM,TIME")
        file.write("\n")
        file.close()
    

def writeToFile(textToWrite):
    file1 = open(path1, "a+")  # append mode
    file1.write(textToWrite)
    file1.close()
    file2 = open(path2, "a+")
    file2.write(textToWrite)
    file2.close()

class stopwatch():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')        
    def start(self):
        global count
        count=0
        self.timer()   
    def stop(self):
        global count
        count=1
    def close(self):
        self.root.destroy()
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer)     
    def __init__(self):
        self.root=Tk()
        canvas1 = Canvas(self.root, width=300, height=400)
        canvas1.pack()
        entry1 = Entry(self.root) 
        # entry1.pack()
        # canvas1.create_window(210, 80, window=entry1)

        def text_to_display_below_done(display_text, X, Y, isPad=False):
            if isPad:
                display_text = ''.join([' ' for i in range(20)]) + display_text + ''.join([' ' for i in range(20)])
            label3 = Label(self.root, text=display_text, font=('helvetica', 10))
            canvas1.create_window(X, Y, window=label3)
        
        def get_square_root():
            x1 = entry1.get()
            string = str(x1)
            string_list = str(x1).split('/')

            print(1, len(string_list))
            if len(string_list) <= 1:
                text_to_display_below_done("NOT VALID LINK", 150, 280, True)
            else:
                textToWrite = str(x1) + "," + self.t.get() + '\n'
                writeToFile(textToWrite)

                display_text = "ADDED! " + string_list[-2] + " " + string_list[-1] + " TIME: " + self.t.get()
                text_to_display_below_done(display_text, 150, 280, True)

        def clear_text():
            entry1.delete(0, END)

            
        DoneButton = Button(text='Done!', command=lambda:[get_square_root(), self.reset(), clear_text()], bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        # canvas1.create_window(160, 150, window=button1)

        self.root.title("Stop Watch")
        self.root.geometry("300x335")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.StartButton = Button(self.root,text="Start",command=self.start,font=("Times 12 bold"),bg=("green"))
        self.StopButton = Button(self.root,text="Stop",command=self.stop,font=("Times 12 bold"),bg=("red"))
        self.ResetButton = Button(self.root,text="↻",command=lambda:[self.reset(), clear_text(), text_to_display_below_done(EMPTY_STRING,150, 280, True)],font=("Times 12 bold"),bg=("orange"))
        self.ExitButton = Button(self.root, text="Exit", command=self.close,font=("Times 12 bold"),bg=("yellow"))
        self.DeleteRecentAdd = Button(self.root, text="Delete", command=delete_last_line,font=("Times 12 bold"),bg=("violet"))

        # slef.bt5 = create_window(200, 100, window=label2)
        
        def show():
            TEMP_NAME = clicked.get()
            SHEET_NAME = str(TEMP_NAME) 
            createFile(SHEET_NAME)
            print(path1)
            label.config( text = clicked.get() )

        options = OPTIONS_MENU
        clicked = StringVar()
        clicked.set( "RATING" )
        drop = OptionMenu(self.root , clicked , *options )

        SelectButton = Button(self.root , text = "Select" , command = show )
        label = Label(self.root , text = " " )

        PERM_Y_VALUE = 200
        self.lb.place(x=40,y=10)
        text_to_display_below_done("LINK: ", 25, 113)
        entry1.place(x=50,y=100, width=180, height=25)
        self.StartButton.place(x=50,y=PERM_Y_VALUE)
        self.StopButton.place(x=125,y=PERM_Y_VALUE)
        self.ResetButton.place(x=240,y=95)
        self.ExitButton.place(x=200,y=PERM_Y_VALUE)
        self.DeleteRecentAdd.place(x=150,y=300)
        DoneButton.place(x=115,y=240)
        drop.place(x=100,y=130)
        label.place(x=200,y=165)
        SelectButton.place(x=102,y=160)
        # self.bt5.place(x=520,y=100)

        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.configure(bg='black')
        self.root.mainloop()
a=stopwatch()      
