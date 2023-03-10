from tkinter import *
import sys
import time
import os

global count
count =0

EMPTY_STRING = ""
for i in range(100):
    EMPTY_STRING += " "

OPTIONS_MENU = []
for itr in range(500, 4000, 100):
    OPTIONS_MENU.append(str(itr))

SHEET_NAME = "TEMP.csv"

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
        canvas1 = Canvas(self.root, width=300, height=180, relief='raised')
        canvas1.pack()
        entry1 = Entry(self.root) 
        entry1.pack()
        canvas1.create_window(210, 80, window=entry1)
        
        def get_square_root():
            x1 = entry1.get()
            print("THE file name: ", SHEET_NAME)
            # /home/iratherfear/Desktop/CPTIMER/
           
            string = str(x1)
            string_list = str(x1).split('/')
            print(1, len(string_list))
            if len(string_list) <= 1:
                display_text = "NOT VALID LINK " + " TIME: " + self.t.get()
                label3 = Label(self.root, text=display_text, font=('helvetica', 10))
                canvas1.create_window(150, 175, window=label3)
            else:
                path = "/home/iratherfear/Desktop/CPTIMER/" + SHEET_NAME

                if os.path.isfile(path) == False:
                    file = open(SHEET_NAME, "w")
                    file.write("PROBLEM,TIME")
                    file.write("\n")
                    file.close()

                file1 = open(SHEET_NAME, "a+")  # append mode
                file1.write(str(x1) + "," + self.t.get() + '\n')
                file1.close()
                
                display_text = "ADDED! " + string_list[-2] + " " + string_list[-1] + " TIME: " + self.t.get()
                label3 = Label(self.root, text=display_text, font=('helvetica', 10))
                canvas1.create_window(150, 175, window=label3)


        def clear_text():
            entry1.delete(0, END)

            
        button1 = Button(text='Done!', command=lambda:[get_square_root(), self.reset(), clear_text()], bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(160, 150, window=button1)

        self.root.title("Stop Watch")
        self.root.geometry("330x255")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Times 12 bold"),bg=("green"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Times 12 bold"),bg=("red"))
        self.bt3 = Button(self.root,text="Reset",command=lambda:[self.reset(), clear_text()],font=("Times 12 bold"),bg=("orange"))
        self.bt4 = Button(self.root, text="Exit", command=self.close,font=("Times 12 bold"),bg=("yellow"))
        # slef.bt5 = create_window(200, 100, window=label2)
        self.lb.place(x=100,y=10)
        self.bt1.place(x=50,y=100)
        self.bt2.place(x=100,y=100)
        self.bt3.place(x=150,y=100)
        self.bt4.place(x=200,y=100)
        def show():
            TEMP_NAME = clicked.get()
            global SHEET_NAME
            SHEET_NAME = str(TEMP_NAME) + ".csv"
            print(SHEET_NAME)
            label.config( text = clicked.get() )
        
        # Dropdown menu options
        options = OPTIONS_MENU
        # datatype of menu text
        clicked = StringVar()
        # initial menu text
        clicked.set( "TEMP" )
        # Create Dropdown menu
        drop = OptionMenu(self.root , clicked , *options )
        drop.place(x=300,y=150)
        drop.pack()
        
        print(SHEET_NAME)
        # Create button, it will change label text
        button = Button(self.root , text = "click Me" , command = show )
        button.place(x=300,y=100)
        button.pack()
        # Create Label
        label = Label(self.root , text = " " )
        label.pack()
        
        # self.bt5.place(x=520,y=100)
        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.configure(bg='black')
        self.root.mainloop()
a=stopwatch()      
