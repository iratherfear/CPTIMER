from tkinter import *
import sys
import time

global count
count =0

EMPTY_STRING = ""
for i in range(50):
    EMPTY_STRING += " "

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
    def _init_(self):
        self.root=Tk()
        canvas1 = Canvas(self.root, width=500, height=500, relief='raised')
        canvas1.pack()
        entry1 = Entry(self.root) 
        entry1.pack()
        canvas1.create_window(210, 80, window=entry1)
        
        def get_square_root():
            x1 = entry1.get()
            file1 = open("cpsheet1100.csv", "a")  # append mode
            file1.write(str(x1) + "," + self.t.get() + '\n')
            file1.close()
            string = str(x1)
            label3 = Label(self.root, text='ADDED!', font=('helvetica', 10))
            canvas1.create_window(200, 175, window=label3)
            label4 = Label(self.root, text=x1, font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 190, window=label4)

        def clear_text():
            label3 = Label(self.root, text=EMPTY_STRING, font=('helvetica', 10))
            canvas1.create_window(200, 175, window=label3)
            label4 = Label(self.root, text=EMPTY_STRING, font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 190, window=label4)
            entry1.delete(0, END)

            
        button1 = Button(text='Done!', command=get_square_root, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(200, 150, window=button1)

        self.root.title("Stop Watch")
        self.root.geometry("400x200")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Times 12 bold"),bg=("green"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Times 12 bold"),bg=("red"))
        self.bt3 = Button(self.root,text="Reset",command=lambda:[self.reset(), clear_text()],font=("Times 12 bold"),bg=("orange"))
        self.bt4 = Button(self.root, text="Exit", command=self.close,font=("Times 12 bold"),bg=("yellow"))
        # slef.bt5 = create_window(200, 100, window=label2)
        self.lb.place(x=100,y=10)
        self.bt1.place(x=100,y=100)
        self.bt2.place(x=150,y=100)
        self.bt3.place(x=200,y=100)
        self.bt4.place(x=250,y=100)
        # self.bt5.place(x=520,y=100)
        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.configure(bg='black')
        self.root.mainloop()
a=stopwatch()
