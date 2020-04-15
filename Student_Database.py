#front end

from tkinter import*
import tkinter.messagebox
import stdDataBackend

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Student Database Manager")
        self.root.geometry('1500x800+0+0')
        self.root.config(bg='black')

        stdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # =====================================================Frames============================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Manager", "Are You Sure You Want to Exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtstdID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtLna.delete(0, END)
            self.txtDob.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGnd.delete(0, END)
            self.txtAds.delete(0, END)
            self.txtMbl.delete(0, END)
            
        def addData():
            if (len(stdID.get()) !=0):
                stdDataBackend.AddStdRec(stdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), \
                                         Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (stdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDataBackend.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            studentlist.delete(0, END)
            global sd
            searchestd = studentlist.curselection()[0]
            sd = studentlist.get(searchestd)

            self.txtstdID.delete(0, END)
            self.txtstdID.insert(END, sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END,[2])
            self.txtLna.delete(0, END)
            self.txtLna.insert(END, [3])
            self.txtDob.delete(0, END)
            self.txtDob.insert(END, [4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, [5])
            self.txtGnd.delete(0, END)
            self.txtGnd.insert(END, [6])
            self.txtAds.delete(0, END)
            self.txtAds.insert(END, [7])
            self.txtMbl.delete(0, END)
            self.txtMbl.insert(END, [8])

        def DeleteData():
            if (len(stdID.get()) != 0):
                stdDataBackend.deleteRec(stdID[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in stdDataBackend.searchData(stdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), \
                                         Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END, row,str(""))

        def Update():
            if(len(stdID.get()) != 0):
                stdDataBackend.deleteRec(sd[0])
            if (len(stdID.get()) != 0):
                stdDataBackend.AddStdRec(stdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), \
                                         Gender.get(), Address.get(), Mobile.get())
                stdDataBackend.deleteRec(0, END)
                studentlist.insert(END,(stdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), \
                                         Gender.get(), Address.get(), Mobile.get()))




        #=====================================================Frames============================================
        MainFrame = Frame(self.root, bg='Dim Grey')
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Dim Grey", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial',50, 'bold'), text="Student Database Manager", bg='Dim Grey', justify=CENTER)
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width='1350', height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width='1300', height=400, padx=20, pady=20, bg="black", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width='1000', height=600, padx=20, bg="Dark Slate Grey", relief=RIDGE,
                                   font=('arial',20, 'bold'), text="Student Info\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width='450', height=300, padx=54, pady=8, bg="Dark Slate Grey", relief=RIDGE,
                                    font=('arial',20, 'bold'), text="Student Details\n")
        DataFrameRight.pack(side=RIGHT)

        # =====================================================Labels and widgets============================================

        self.lblstdID = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='Student ID :', padx=2, pady=2, bg='Dark Slate Grey')
        self.lblstdID.grid(row=0, column=0, sticky=W)
        self.txtstdID = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey', textvariable=stdID, bg='black', width=32)
        self.txtstdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='First Name :', padx=2,
                              pady=2, bg='Dark Slate Grey')
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey',
                              textvariable=Firstname, bg='black', width=32)
        self.txtfna.grid(row=1, column=1)

        self.lblLna = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='Last  Name :', padx=2,
                              pady=2, bg='Dark Slate Grey')
        self.lblLna.grid(row=2, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey',
                              textvariable=Lastname, bg='black', width=32)
        self.txtLna.grid(row=2, column=1)

        self.lblDob = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='Date of Birth :', padx=2,
                              pady=2, bg='Dark Slate Grey')
        self.lblDob.grid(row=3, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey',
                              textvariable=DoB, bg='black', width=32)
        self.txtDob.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='Age  Details:', padx=2,
                              pady=2, bg='Dark Slate Grey')
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey',
                              textvariable=Age, bg='black', width=32)
        self.txtAge.grid(row=4, column=1)

        self.lblGnd = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='Gender  Fld:', padx=2,
                              pady=2, bg='Dark Slate Grey')
        self.lblGnd.grid(row=5, column=0, sticky=W)
        self.txtGnd = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey',
                              textvariable=Gender, bg='black', width=32)
        self.txtGnd.grid(row=5, column=1)

        self.lblAds = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='Address No:', padx=2,
                              pady=2, bg='Dark Slate Grey')
        self.lblAds.grid(row=6, column=0, sticky=W)
        self.txtAds = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey',
                              textvariable=Address, bg='black', width=32)
        self.txtAds.grid(row=6, column=1)

        self.lblMbl = Label(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), text='Mobile  No :', padx=2,
                              pady=2, bg='Dark Slate Grey')
        self.lblMbl.grid(row=7, column=0, sticky=W)
        self.txtMbl = Entry(DataFrameLeft, font=('Baskerville Old Face', 22, 'bold'), fg='Dim Grey',
                              textvariable=Mobile, bg='black', width=32)
        self.txtMbl.grid(row=7, column=1)

        # =====================================================ListBox and ScrollBar widgets============================================

        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRight, width=41, height=16, font=('Baskerville Old Face', 14, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)
        # =====================================================Buttons============================================
        self.btnAddDate = Button(ButtonFrame, text="Add New", font=('Baskerville Old Face', 20, 'bold'), height=1,
                                 width=10, bd=4, bg='Dark Slate Grey', command=addData)
        self.btnAddDate.grid(row=0, column=0, padx=8)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('Baskerville Old Face', 20, 'bold'), height=1,
                                 width=10, bd=4, bg='Dark Slate Grey', command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1, padx=8)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('Baskerville Old Face', 20, 'bold'), height=1,
                                 width=10, bd=4, bg='Dark Slate Grey', command=clearData)
        self.btnClearData.grid(row=0, column=2, padx=8)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('Baskerville Old Face', 20, 'bold'), height=1,
                                 width=10, bd=4, bg='Dark Slate Grey', command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3, padx=8)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('Baskerville Old Face', 20, 'bold'), height=1,
                                 width=10, bd=4, bg='Dark Slate Grey', command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4, padx=8)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('Baskerville Old Face', 20, 'bold'), height=1,
                                 width=10, bd=4, bg='Dark Slate Grey', command=Update)
        self.btnUpdateData.grid(row=0, column=5, padx=8)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('Baskerville Old Face', 20, 'bold'), height=1,
                                    width=10, bd=4, bg='Dark Slate Grey', command=iExit)
        self.btnExit.grid(row=0, column=6, padx=8)







if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
