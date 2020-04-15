from tkinter import *
import tkinter.messagebox
import LibBksDatabase


class Library:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Database Manager")
        self.root.geometry("1350x600+0+0")
        self.root.configure(bg="black")

        MTy = StringVar
        Ref = StringVar
        Tit = StringVar
        Fna = StringVar
        Lna = StringVar
        Adr1 = StringVar
        Adr2 = StringVar
        pcd = StringVar
        MNo = StringVar
        BKID = StringVar
        Bkt = StringVar
        BKT = StringVar
        Atr = StringVar
        DBo = StringVar
        Ddu = StringVar
        SPr = StringVar
        LrF = StringVar
        DoD = StringVar
        DonL = StringVar

        # ========================================================Functions=================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Teos - Library Database Manger", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def ClearData():
            self.txtMType.delete(0, END)
            self.txtBKID.delete(0, END)
            self.txtRef.delete(0, END)
            self.txtBkt.delete(0, END)
            self.txtTit.delete(0, END)
            self.txtAtr.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtLna.delete(0, END)
            self.txtDdu.delete(0, END)
            self.txtAdr1.delete(0, END)
            self.txtAdr2.delete(0, END)
            self.txtDonL.delete(0, END)
            self.txtLrF.delete(0, END)
            self.txtpcd.delete(0, END)
            self.txtDoD.delete(0, END)
            self.txtMNo.delete(0, END)
            self.txtsPr.delete(0, END)
            self.txtDBo.delete(0, END)

        def AddData(self):
            if len(self.MTy.get()) != 0:
                LibBksDatabase.addDataRec(self.MTy.get(), self.Ref.get(), self.Tit.get(), self.Fna.get(), self.Lna.get(), self.Adr1.get(),
                                          self.Adr2.get(), self.pcd.get(), self.MNo.get(), self.BKID.get(), self.Bkt.get(),
                                          self.Atr.get(), self.DBo.get(), self.Ddu.get(), self.SPr.get(),
                                          self.LrF.get(), self.DoD.get(), self.DonL.get())

                booklist.delete(0, END)
                booklist.insert(END, self.MTy.get(), self.Ref.get(), self.Tit.get(), self.Fna.get(), self.Lna.get(), self.Adr1.get(), self.Adr2.get(),
                                self.pcd.get(), self.MNo.get(), self.BKID.get(), self.Bkt.get(), self.Atr.get(),
                                self.DBo.get(), self.Ddu.get(), self.SPr.get(), self.LrF.get(), self.DoD.get(), self.DonL.get())

        # ========================================================Frames=================================================
        MainFrame = Frame(self.root, bg='black')
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=40, pady=8, bg='Dim grey', relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('Algerian', 46, 'bold'), text="Teos - Library Database Manger",
                            bg='dim grey')
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=100, padx=20, pady=20, bg='black', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=0, width=1350, height=50, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg='slate grey', relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=800, height=300, padx=20, relief=RIDGE,
                                   font=('Baskerville Old Face', 12, 'bold'), text="Library Membership Info:",
                                   bg='Dark Slate Grey')
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=40, pady=8, relief=RIDGE,
                                    font=('Baskerville Old Face', 12, 'bold'), bg="Dark Slate Grey",
                                    text="Book Details:")
        DataFrameRight.pack(side=RIGHT)
        # ========================================================Labels=================================================
        self.lblMemberType = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Member Type', padx=2,
                                   pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblMemberType.grid(row=0, column=0, sticky=W)
        self.txtMType = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=MTy, width=25)
        self.txtMType.grid(row=0, column=1)

        self.lblBKID = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Book ID:', padx=2,
                             pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblBKID.grid(row=0, column=2, sticky=W)
        self.txtBKID = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=BKID, width=25)
        self.txtBKID.grid(row=0, column=3)

        self.lblRef = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Refence No:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblBkt = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Book Title:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblBkt.grid(row=1, column=2, sticky=W)
        self.txtBkt = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Bkt, width=25)
        self.txtBkt.grid(row=1, column=3)

        self.lblTit = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Title:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblTit.grid(row=2, column=0, sticky=W)
        self.txtTit = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Tit, width=25)
        self.txtTit.grid(row=2, column=1)

        self.lblAtr = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Author:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblAtr.grid(row=2, column=2, sticky=W)
        self.txtAtr = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Atr, width=25)
        self.txtAtr.grid(row=2, column=3)

        self.lblFna = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='First Name:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblFna.grid(row=3, column=0, sticky=W)
        self.txtFna = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=BKID, width=25)
        self.txtFna.grid(row=3, column=1)

        self.lblDBo = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Date Borrowed:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblDBo.grid(row=3, column=2, sticky=W)
        self.txtDBo = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=DBo, width=25)
        self.txtDBo.grid(row=3, column=3)

        self.lblLna = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Last Name:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblLna.grid(row=4, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Lna, width=25)
        self.txtLna.grid(row=4, column=1)

        self.lblDdu = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Due Date:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblDdu.grid(row=4, column=2, sticky=W)
        self.txtDdu = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Ddu, width=25)
        self.txtDdu.grid(row=4, column=3)

        self.lblAdr1 = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Address 1:', padx=2,
                             pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblAdr1.grid(row=5, column=0, sticky=W)
        self.txtAdr1 = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Adr1, width=25)
        self.txtAdr1.grid(row=5, column=1)

        self.lblDonL = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Days on Loan:', padx=2,
                             pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblDonL.grid(row=5, column=2, sticky=W)
        self.txtDonL = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=DonL, width=25)
        self.txtDonL.grid(row=5, column=3)

        self.lblAdr2 = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Address 2:', padx=2,
                             pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblAdr2.grid(row=6, column=0, sticky=W)
        self.txtAdr2 = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=Adr2, width=25)
        self.txtAdr2.grid(row=6, column=1)

        self.lblLrF = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Late Return Fine:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblLrF.grid(row=6, column=2, sticky=W)
        self.txtLrF = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=LrF, width=25)
        self.txtLrF.grid(row=6, column=3)

        self.lblpcd = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Post Code:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblpcd.grid(row=7, column=0, sticky=W)
        self.txtpcd = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=pcd, width=25)
        self.txtpcd.grid(row=7, column=1)

        self.lblDoD = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Date Over Due:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblDoD.grid(row=7, column=2, sticky=W)
        self.txtDoD = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=DoD, width=25)
        self.txtDoD.grid(row=7, column=3)

        self.lblMNo = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Mobile No:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblMNo.grid(row=8, column=0, sticky=W)
        self.txtMNo = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=MNo, width=25)
        self.txtMNo.grid(row=8, column=1)

        self.lblsPr = Label(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), text='Selling Price:', padx=2,
                            pady=2, bg='Dark Slate Grey', fg='Orange')
        self.lblsPr.grid(row=8, column=2, sticky=W)
        self.txtsPr = Entry(DataFrameLeft, font=('Baskerville Old Face', 12, 'bold'), textvariable=SPr, width=25)
        self.txtsPr.grid(row=8, column=3)

        # ===============================================Listbox and Scrollbar===========================================
        scrollbar = Scrollbar(DataFrameRight, bg='Dark Slate Grey')
        scrollbar.grid(row=0, column=1, sticky='ns')

        booklist = Listbox(DataFrameRight, width=45, height=12, font=('Baskerville Old Face', 12, 'bold'),
                           yscrollcommand=scrollbar.set)
        booklist.grid(row=0, column=0, padx=0)
        scrollbar.config(command=booklist.yview)

        # ===============================================Buttons===========================================

        self.btnAddData = Button(ButtonFrame, text='Add Data', font=('Algerian', 14, 'bold'), height=2, width=13, bd=4,
                                 bg='Dark Slate Grey', fg='Orange', command=AddData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisDate = Button(ButtonFrame, text='Display Data', font=('Algerian', 14, 'bold'), height=2, width=13,
                                 bd=4,
                                 bg='Dark Slate Grey', fg='Orange')
        self.btnDisDate.grid(row=0, column=1)

        self.btnClrDate = Button(ButtonFrame, text='Clear Data', font=('Algerian', 14, 'bold'), height=2, width=13,
                                 bd=4,
                                 bg='Dark Slate Grey', fg='Orange', command=ClearData)
        self.btnClrDate.grid(row=0, column=2)

        self.btnDelDate = Button(ButtonFrame, text='Delete Data', font=('Algerian', 14, 'bold'), height=2, width=13,
                                 bd=4,
                                 bg='Dark Slate Grey', fg='Orange')
        self.btnDelDate.grid(row=0, column=3)

        self.btnUptDate = Button(ButtonFrame, text='Update Data', font=('Algerian', 14, 'bold'), height=2, width=13,
                                 bd=4,
                                 bg='Dark Slate Grey', fg='Orange')
        self.btnUptDate.grid(row=0, column=4)

        self.btnSchDate = Button(ButtonFrame, text='Search Data', font=('Algerian', 14, 'bold'), height=2, width=13,
                                 bd=4,
                                 bg='Dark Slate Grey', fg='Orange')
        self.btnSchDate.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('Algerian', 14, 'bold'), height=2, width=13, bd=4,
                              bg='Dark Slate Grey', fg='Orange', command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
