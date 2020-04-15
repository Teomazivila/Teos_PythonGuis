from tkinter import *
import time
import datetime
import pygame, sys, random
import tkinter.messagebox

pygame.init()
root = Tk()
root.title("Sales Management System")
root.geometry('1352x700+0+0')
root.configure(background='Black')

#=========================================Frame====================================================

ABC=Frame(root, bg="powder blue", bd=28, relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC, bg="cadet blue", bd=10,  relief=RIDGE)
ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
ABC2 =Frame(ABC, bg= "Black", bd=10, relief=RIDGE)
ABC2.grid(row=1, column=0, sticky=W)
ABC3 =Frame(ABC, bg= "Black", bd=10, relief=RIDGE)
ABC3.grid(row=1, column=1, sticky=W)
ABC4 =Frame(ABC, bg= "Black", bd=10, relief=RIDGE)
ABC4.grid(row=1, column=2, sticky=W)
ABC5 =Frame(ABC4, bg= "Black", bd=10, relief=RIDGE)
ABC5.grid(row=0, column=0, sticky=W)
ABC6 =Frame(ABC4, bg= "Black", bd=10, relief=RIDGE)
ABC6.grid(row=1, column=0, columnspan=4, sticky=W)

#=========================================Variables====================================================
Date1=StringVar()
Time1 = StringVar()
Receipt_Ref = StringVar()
Tax = StringVar()
Subtotal = StringVar()
Total = StringVar()

Jeans_Jeggers = StringVar()
Coats_Jackets = StringVar()
Sportwear = StringVar()
Dresses = StringVar()
Skirts = StringVar()
Swimwear = StringVar()
School_Uniform = StringVar()
Pyjamas_Dressing=StringVar()

Jackect_Blazer= StringVar()
Formal_Trousers = StringVar()
Formal_Shirts = StringVar()
Men_Boots= StringVar()
Bed_Sheet = StringVar()
Pillow_Cases = StringVar()
Patterned_Bedding= StringVar()
Mattress_Protectors=StringVar()

Jeans_Jeggers.set("0")
Coats_Jackets.set("0")
Sportwear.set("0")
Dresses.set("0")
Skirts.set("0")
Swimwear.set("0")
School_Uniform.set("0")
Pyjamas_Dressing.set("0")

Jackect_Blazer.set("0")
Formal_Trousers.set("0")
Formal_Shirts.set("0")
Men_Boots.set("0")
Bed_Sheet.set("0")
Pillow_Cases.set("0")
Patterned_Bedding.set("0")
Mattress_Protectors.set("0")
#=========================================Date and Time====================================================
Date1.set(time.strftime("%d/%m/%y"))
Time1.set(time.strftime("%H:%M:%S"))
#=========================================Function Declaration====================================================
def iExit():
    iExit =tkinter.messagebox.askyesno("Sales Management System", "Confirm if you want to exit")
    if iExit >0:
        root.destroy()
        return

def Reset():
    txtReceipt.delete("1.0", END)
    Jeans_Jeggers.set("0")
    Coats_Jackets.set("0")
    Sportwear.set("0")
    Dresses.set("0")
    Skirts.set("0")
    Swimwear.set("0")
    School_Uniform.set("0")
    Pyjamas_Dressing.set("0")

    Jackect_Blazer.set("0")
    Formal_Trousers.set("0")
    Formal_Shirts.set("0")
    Men_Boots.set("0")
    Bed_Sheet.set("0")
    Pillow_Cases.set("0")
    Patterned_Bedding.set("0")
    Mattress_Protectors.set("0")

def Total():
    Item1 = float (Jeans_Jeggers.get())
    Item2 = float(Coats_Jackets.get())
    Item3 = float(Sportwear.get())
    Item4 = float(Dresses.get())
    Item5 = float(Skirts.get())
    Item6 = float(Swimwear.get())
    Item7 = float(School_Uniform.get())
    Item8 = float(Pyjamas_Dressing.get())

    Item9 = float(Jackect_Blazer.get())
    Item10 = float(Formal_Trousers.get())
    Item11 = float(Formal_Shirts.get())
    Item12 = float(Men_Boots.get())
    Item13 = float(Bed_Sheet.get())
    Item14 = float(Pillow_Cases.get())
    Item15 = float(Patterned_Bedding.get())
    Item16 = float(Mattress_Protectors.get())

    priceofItem1 = ("MZN")+ str('%.2f' %(Item1 * 250))
    priceofItem2 = ("MZN")+ str('%.2f' %(Item2 * 300))
    priceofItem3 = ("MZN")+ str('%.2f' %(Item3 * 1250))
    priceofItem4 = ("MZN")+ str('%.2f' %(Item4 * 550))
    priceofItem5 = ("MZN")+ str('%.2f' %(Item5 * 750))
    priceofItem6 = ("MZN")+ str('%.2f' %(Item6 * 900))
    priceofItem7 = ("MZN")+ str('%.2f' %(Item7 * 1300))
    priceofItem8 = ("MZN")+ str('%.2f' %(Item8 * 2500))
    priceofItem9 = ("MZN")+ str('%.2f' %(Item9 * 2250))
    priceofItem10 = ("MZN")+ str('%.2f' %(Item10 * 1250))
    priceofItem11 = ("MZN")+ str('%.2f' %(Item11 * 2750))
    priceofItem12 = ("MZN")+ str('%.2f' %(Item12 * 1530))
    priceofItem13 = ("MZN")+ str('%.2f' %(Item13 * 650))
    priceofItem14 = ("MZN")+ str('%.2f' %(Item14 * 5000))
    priceofItem15 = ("MZN")+ str('%.2f' %(Item15 * 10000))
    priceofItem16 = ("MZN")+ str('%.2f' %(Item16 * 7500))

    priceofWomen = (Item1 * 250) + (Item2 * 300) + (Item3 * 1250) + (Item4 * 550)
    priceofKids = (Item5 * 750) + (Item6 * 900) + (Item7 * 1300) + (Item8 * 2500)
    priceofMen = (Item9 * 2250) + (Item10 * 1250) + (Item11 * 2750) + (Item12 * 1530)
    priceofHomeware = (Item13 * 650) + (Item14 * 5000) + (Item15 * 10000) + (Item16 * 7500)

    subTotalofITEMS = ("MZN")+ str('%.2f' %(priceofWomen + priceofKids + priceofMen + priceofHomeware))
    iTax = ("MZN")+ str('%.2f' %((priceofWomen + priceofKids + priceofMen + priceofHomeware) * 0.15))

    TT = (priceofWomen + priceofKids + priceofMen + priceofHomeware)
    TC = (((priceofWomen + priceofKids + priceofMen + priceofHomeware) * 0.15))
    TotalCost = ("MZN")+ str('%.2f' %(TT + TC))

    txtReceipt.delete("1.0", END)
    x = random.randint(10747, 500298)
    ramdomRef = str(x)
    Receipt_Ref.set("BILL"+ ramdomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t'+ Receipt_Ref.get()+ '\n'+ Date1.get()+ '\t\t\t\t' + Time1.get()+ "\n")
    txtReceipt.insert(END, '----------------------------------------------------------------------------' + "\n")
    txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t'+ "Cost of Items\n")
    txtReceipt.insert(END, '----------------------------------------------------------------------------' + "\n")
    txtReceipt.insert(END, 'Jeans Jeggers\t\t\t\t' + priceofItem1 + "\n")
    txtReceipt.insert(END, 'Coats Jackets\t\t\t\t' + priceofItem2 + "\n")
    txtReceipt.insert(END, 'Sportwear\t\t\t\t' + priceofItem3 + "\n")
    txtReceipt.insert(END, 'Dresses\t\t\t\t' + priceofItem4 + "\n")
    txtReceipt.insert(END, 'Skirts\t\t\t\t' + priceofItem5 + "\n")
    txtReceipt.insert(END, 'Swimwear\t\t\t\t' + priceofItem6 + "\n")
    txtReceipt.insert(END, 'School Uniform\t\t\t\t' + priceofItem7 + "\n")
    txtReceipt.insert(END, 'Pyjamas Dressing\t\t\t\t' + priceofItem8 + "\n")
    txtReceipt.insert(END, 'Pyjamas Dressing\t\t\t\t' + priceofItem9 + "\n")
    txtReceipt.insert(END, 'Jackect Blazer\t\t\t\t' + priceofItem10 + "\n")
    txtReceipt.insert(END, 'Formal Shirts\t\t\t\t' + priceofItem11 + "\n")
    txtReceipt.insert(END, 'Men Boots\t\t\t\t' + priceofItem12 + "\n")
    txtReceipt.insert(END, 'Bed Sheet\t\t\t\t' + priceofItem13 + "\n")
    txtReceipt.insert(END, 'Pillow Cases\t\t\t\t' + priceofItem14 + "\n")
    txtReceipt.insert(END, 'Patterned Bedding\t\t\t\t' + priceofItem15 + "\n")
    txtReceipt.insert(END, 'Mattress Protectors\t\t\t\t' + priceofItem16 + "\n")
    txtReceipt.insert(END, '----------------------------------------------------------------------------' + "\n")
    txtReceipt.insert(END, 'Tax Paid:\t\t\t\t' + iTax + "\n")
    txtReceipt.insert(END, 'SubTotal:\t\t\t\t' + subTotalofITEMS + "\n")
    txtReceipt.insert(END, 'Total Cost:\t\t\t\t' + TotalCost + "\n")


#=========================================Frame====================================================

lblTitle = Label(ABC1, textvariable=Date1, font=('Arial', 32), padx=9, pady=9,
bd=14, bg="Cadet blue", fg="Cornsilk", justify=CENTER).grid(row=0,column=0)

lblTitle = Label(ABC1, text="\tSales Management Systems\t",font=('Arial', 32), padx=9, pady=9,
bd=14, bg="Cadet blue", fg="Cornsilk", justify=CENTER).grid(row=0,column=1)

lblTitle = Label(ABC1, textvariable=Time1, font=('Arial', 32), padx=9, pady=9,
bd=14, bg="Cadet blue", fg="Cornsilk", justify=CENTER).grid(row=0,column=2)

#=========================================Frame====================================================
lblWomen=Label(ABC2, text="Women", font=('Baskerville Old Face', 20,), pady=1, bd=8,bg="Green",
                 fg="Cornsilk", width=25, justify=CENTER).grid(row=0, column=0, columnspan=4)

lblJeansJeggers = Label(ABC2, text="Jeans & Jeggers", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=1, column=0, sticky=W)

lblCoatsJackets = Label(ABC2, text="Coats & Jackets", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=2, column=0, sticky=W)

lblSportwear = Label(ABC2, text="Sportwear", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=3, column=0, sticky=W)

lblDresses = Label(ABC2, text="Dresses", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=4, column=0, sticky=W)

lblSkirts = Label(ABC2, text="Skirts", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=6, column=0, sticky=W)

lblSwimwear = Label(ABC2, text="Swimwear", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=7, column=0, sticky=W)

lblSchoolUniform = Label(ABC2, text="School Uniform",
                         bg="Gold", font=('Arial', 18, 'bold'), justify=LEFT).grid(row=8, column=0, sticky=W)

lblPyjamasDressing = Label(ABC2, text="Pyjamas Dressing",
                         bg="Gold", font=('Arial', 18, 'bold'), justify=LEFT).grid(row=8, column=0, sticky=W)

#=========================================Text====================================================
txtJeansJeggers = Entry(ABC2,textvariable = Jeans_Jeggers, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=1, column=1, pady=1)

txtCoatsJackets = Entry(ABC2,textvariable = Coats_Jackets, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=2, column=1, pady=1)

txtSportwear = Entry(ABC2,textvariable = Sportwear, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=3, column=1, pady=1)

txtDresses = Entry(ABC2, textvariable = Dresses, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=4, column=1, pady=1)

lblKids=Label(ABC2,  text="Kids", font=('Baskerville Old Face', 20,), pady=1, bd=8,bg="Green",
                 fg="Cornsilk", width=25, justify=CENTER).grid(row=5, column=0, columnspan=4)

txtSkirts = Entry(ABC2, textvariable = Skirts, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=6, column=1, pady=1)

txtSwimwear = Entry(ABC2, textvariable = Swimwear, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=7, column=1, pady=1)

txtSchoolUniform = Entry(ABC2, textvariable = School_Uniform, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=8, column=1, pady=1)

txtPyjamasDressing = Entry(ABC2, textvariable = Pyjamas_Dressing, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=9, column=1, pady=1)
#=======================================Labels and Text Entry===========================================================
lblMens=Label(ABC3, text="Men", font=('Baskerville Old Face', 20,), pady=1, bd=8,bg="Green",
                 fg="Cornsilk", width=25, justify=CENTER).grid(row=0, column=1, columnspan=4)

lblJackectBlazers = Label(ABC3, text="Jackect & Blazers", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=1, column=1, sticky=W)

lblFormalTrousers = Label(ABC3, text="Formal Trousers", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=2, column=1, sticky=W)

lblFormalShirts = Label(ABC3, text="Formal Shirts", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=3, column=1, sticky=W)

lblMenBoots = Label(ABC3, text="Men Boots", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=4, column=1, sticky=W)

lblBedSheet = Label(ABC3, text="Bed Sheet", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=6, column=1, sticky=W)

lblPillowCases = Label(ABC3, text="Pillow Cases", bg="Gold",
                 font=('Arial', 18, 'bold'), justify=LEFT).grid(row=7, column=1, sticky=W)

lblPatternedBedding = Label(ABC3, text="Patterned Bedding",
                         bg="Gold", font=('Arial', 18, 'bold'), justify=LEFT).grid(row=8, column=1, sticky=W)

lblMattressProtector = Label(ABC3, text="Mattress Protector ",
                         bg="Gold", font=('Arial', 18, 'bold'), justify=LEFT).grid(row=8, column=1, sticky=W)

#=========================================Text==========================================================
txtJacket_Blazers = Entry(ABC3,textvariable = Jackect_Blazer, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=1, column=2, pady=1)

txtFormal_Trousers = Entry(ABC3, textvariable = Formal_Trousers, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=2, column=2, pady=1)

txtFormal_Shirts = Entry(ABC3, textvariable = Formal_Shirts, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=3, column=2, pady=1)

txtMen_Boots = Entry(ABC3, textvariable = Men_Boots, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=4, column=2, pady=1)

lblKids=Label(ABC3, text="Homeware", font=('Baskerville Old Face', 20,), pady=1, bd=8,bg="Green",
                 fg="Cornsilk", width=25, justify=CENTER).grid(row=5, column=1, columnspan=4)

txtBed_Sheet = Entry(ABC3, textvariable = Bed_Sheet, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=6, column=2, pady=1)

txtPillow_Cases= Entry(ABC3, textvariable = Pillow_Cases, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=7, column=2, pady=1)

txtPatterned_Bedding = Entry(ABC3, textvariable = Patterned_Bedding, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=8, column=2, pady=1)

txtMattress_Protectors = Entry(ABC3,textvariable = Mattress_Protectors, font=('Arial', 18, 'bold'), bd=8, bg="Cadet blue",
                         fg= "White", width=12, justify=CENTER).grid(row=9, column=2, pady=1)
#=========================================Text====================================================

txtReceipt = Text(ABC5, height =24, width =50, bd=20, font=('arial',11, 'bold') )
txtReceipt .grid(row=0, column=0)

#=========================================Text====================================================
btnTotal =Button(ABC6, padx=16, pady=1, bd=4, fg="Black", font=("Baskerville Old Face", 16, 'bold',), width=7, bg="powder blue",
                 text="Total", command =Total).grid(row=0, column =0)

btnReset =Button(ABC6, padx=16, pady=1, bd=4, fg="Black", font=("Baskerville Old Face", 16, 'bold',), width=7, bg="powder blue",
                 text="Reset", command = Reset).grid(row=0, column =1)

btnExit =Button(ABC6, padx=16, pady=1, bd=4, fg="Black", font=("Baskerville Old Face", 16, 'bold',), width=7, bg="powder blue",
                 text="Exit", command = iExit).grid(row=0, column =2)

root.mainloop()