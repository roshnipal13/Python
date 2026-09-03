from tkinter import *
from tkinter import ttk


class Librarymanagementsystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management system")
        self.root.geometry("1550x800+0+0")


        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="black",fg ="white",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        frame.place(x=0,y=130,width=1500,height=400)

         #=================== Data left====================

        DataFrameLeft = LabelFrame(frame,text="Library students information",bg="black",fg ="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0, y=5, width=800, height=350)

        lblMemeber=Label(DataFrameLeft,text="Member Type",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblMemeber.grid(row=0,column=0,sticky=W)

        DataFrameRight = LabelFrame(frame,text="Book detials",bg="black",fg ="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=810, y=5, width=600, height=350)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin staf","Student","Lacturar")
        comMember.grid(row=0,column=1)

        lblENRoll_No=Label(DataFrameLeft,text="ENRoll No :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblENRoll_No.grid(row=1,column=0,sticky=W)

        txtEN_No = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtEN_No.grid(row=1 ,column=1, padx=2, pady=6)


        lblFirst_Name=Label(DataFrameLeft,text="Id No :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblFirst_Name.grid(row=2,column=0,sticky=W)

        txtFirst_Name = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtFirst_Name.grid(row=2 ,column=1)


        lblFirst_Name=Label(DataFrameLeft,text="First Name :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblFirst_Name.grid(row=3,column=0,sticky=W)

        txtFirst_Name = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtFirst_Name.grid(row=3 ,column=1)

        lblFirst_Name=Label(DataFrameLeft,text="surename Name :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblFirst_Name.grid(row=4,column=0,sticky=W)

        txtFirst_Name = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtFirst_Name.grid(row=4 ,column=1)

        lblFirst_Name=Label(DataFrameLeft,text="Address :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblFirst_Name.grid(row=5,column=0,sticky=W)

        txtFirst_Name = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtFirst_Name.grid(row=5 ,column=1)


        lblFirst_Name=Label(DataFrameLeft,text="contect No :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblFirst_Name.grid(row=6,column=0,sticky=W)

        txtFirst_Name = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtFirst_Name.grid(row=6 ,column=1)


        lblFirst_Name=Label(DataFrameLeft,text="whatsapp No :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblFirst_Name.grid(row=7,column=0,sticky=W)

        txtFirst_Name = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtFirst_Name.grid(row=7 ,column=1)

        lblFirst_Name=Label(DataFrameLeft,text="book Id :",bg="black",font=("times new roman",12,"bold"),fg="white",padx=2,pady=6)
        lblFirst_Name.grid(row=8,column=0,sticky=W)

        txtFirst_Name = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),width=24)
        txtFirst_Name.grid(row=8 ,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",bg="black",fg="white")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtBookId.grid(row=0,column=3)


        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",bg="black",fg="white")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtBookId.grid(row=1,column=3)


        lblAutherName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther name:",bg="black",fg="white")
        lblAutherName.grid(row=2,column=2,sticky=W)
        txtAutherName=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtAutherName.grid(row=2,column=3)


        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed :",bg="black",fg="white")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",bg="black",fg="white")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtDateDue.grid(row=4,column=3)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days on book:",bg="black",fg="white")
        lblBookId.grid(row=5,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtBookId.grid(row=5,column=3)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",bg="black",fg="white")
        lblBookId.grid(row=6,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtBookId.grid(row=6,column=3)


        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date over Due:",bg="black",fg="white")
        lblBookId.grid(row=7,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtBookId.grid(row=7,column=3)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual price:",bg="black",fg="white")
        lblBookId.grid(row=8,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=24)
        txtBookId.grid(row=8,column=3)

    #========================================== Data frame right =========================================
        
        DataFrameRight=LabelFrame(frame,bd=12,padx=20,relief=RIDGE,fg="white" ,bg="black",font=("arial",12,"bold"),text="Book details")
        DataFrameRight.place(x=820,y=5,width=580,height=350)
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=28,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=3)

        


        #============= botton frame ================

        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        framebutton.place(x=0,y=530,width=1530,height=70)

        #============= Information frame  ================

        frameinformation=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        frameinformation.place(x=0,y=600,width=1530,height=195)


if __name__ == "__main__":
    root=Tk()
    obj=Librarymanagementsystem(root)
    root.mainloop()