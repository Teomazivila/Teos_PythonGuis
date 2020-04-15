from tkinter import*
import math, random, os
from tkinter import messagebox
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Teo's Billing System")
        bg_color = "#074463"
        bg_color2 = "gold" #"#074463"
        bg_color1 = "black"
        fg_color = "Dark Slate Grey" #"Dark Slate Grey" #lightgreen
        title=Label(self.root, text="Teo's Billing System", bd=12, relief=GROOVE, bg=bg_color, fg=bg_color2,
                    font=('Baskerville Old Face', 30, 'bold'), pady=12).pack(fill=X)


        #=========================================sample Variables==============================================================
        pdr1="Thunder Adt"
        pdr2 = "Apple Mouse"
        pdr3 = "Logitec M"
        pdr5 = "Mac Drone"
        pdr6 = "Cell Phone"
        pdr7 = "Laptop Battery"
        pdr8 = "M-stick"
        pdr9 = "Ext SSD"
        pdr10 = "Ext HDD"
        pdr11 = "LAN Cable"
        pdr12 = "Network Router"
        pdr13 = "HDMI Cable"
        pdr14 = "Hasee Gamer 1"
        pdr15 = "Acer Gamer"
        pdr16 = "Mac B Pro"
        pdr17 = "Hp proBook"
        pdr18 = "Dell Gamer"
        pdr19 = "Asus Gamer"

        # =========================================Variables declaration==============================================================
        self.thunder=IntVar()
        self.amouse = IntVar()
        self.logicm = IntVar()
        self.drone = IntVar()
        self.cphone = IntVar()
        self.laptopb = IntVar()

        self.mstick = IntVar()
        self.ssd = IntVar()
        self.hdd = IntVar()
        self.lan = IntVar()
        self.router = IntVar()
        self.hdmi = IntVar()

        self.hasee = IntVar()
        self.acer = IntVar()
        self.macb = IntVar()
        self.hp = IntVar()
        self.dell = IntVar()
        self.asus = IntVar()

        self.eletprice1 = StringVar()
        self.eletprice2 = StringVar()
        self.lapprice = StringVar()

        self.elettax1 = StringVar()
        self.elettax2 = StringVar()
        self.laptax = StringVar()

        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.c_bill = StringVar()
        x=random.randint(1000,9999)
        self.c_bill.set(str(x))

        self.search_bill = StringVar()




        #======================================Customer Detail Frame ===================================================
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text='Customer Details', font=('times new roman',15, 'bold'), fg=bg_color2, bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname1_lbl = Label(F1, text="Customer Name:", font=('Baskerville Old Face', 18, 'bold')).grid(row=0, column=0, padx=20, pady=5)
        cname_txt=Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn1_lbl = Label(F1, text="Phone No.", font=('Baskerville Old Face', 18, 'bold')).grid(row=0, column=2,
                                                                                                    padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phone, font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", font=('Baskerville Old Face', 18, 'bold')).grid(row=0, column=4,
                                                                                                    padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.c_bill, font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, bd=7, font='arial 12 bold').grid(row=0, column=6, padx=10, pady=10)


        #====================================================Products Frame=============================================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Teo's Electronics", font=('times new roman',15, 'bold'), fg=bg_color2, bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        mstick1_lbl=Label(F2, text=pdr8, font=('times new roman',16, 'bold'), bg=bg_color, fg=fg_color,).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        mstick_txt=Entry(F2, width=10, textvariable=self.mstick, font=('times new roman',16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10,pady=10)

        ssd1_lbl = Label(F2, text=pdr9, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=1,
                                              column=0, padx=10, pady=10, sticky=W)
        ssd_txt = Entry(F2, width=10, textvariable=self.ssd, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                              padx=10, pady=10)

        hdd1_lbl = Label(F2, text=pdr10, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=2,
                                            column=0, padx=10, pady=10, sticky=W)
        hdd_txt = Entry(F2, width=10,textvariable=self.hdd, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                            padx=10, pady=10)

        lan1_lbl = Label(F2, text=pdr11, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=3,
                                            column=0, padx=10, pady=10, sticky=W)
        lan_txt = Entry(F2, width=10,textvariable=self.lan, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                            padx=10, pady=10)

        router1_lbl = Label(F2, text=pdr12, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=4,
                                                 column=0, padx=10, pady=10, sticky=W)
        router_txt = Entry(F2, width=10, textvariable=self.router, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                 padx=10, pady=10)

        hdmi1_lbl = Label(F2, text=pdr13, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=5,
                                              column=0, padx=10, pady=10, sticky=W)
        hdmi_txt = Entry(F2, width=10, textvariable=self.hdmi, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                             padx=10, pady=10)

        # ====================================================Eletronics Frame=============================================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text='More Electronics', font=('times new roman', 15, 'bold'),
                        fg=bg_color2, bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        thunder1_lbl = Label(F3, text=pdr1, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=0,
                                                 column=0, padx=10, pady=10, sticky=W)
        thunder_txt = Entry(F3, width=10, textvariable=self.thunder, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                 padx=10, pady=10)

        amouse1_lbl = Label(F3, text=pdr2, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=1,
                                                 column=0, padx=10, pady=10, sticky=W)
        amouse_txt = Entry(F3, width=10, textvariable=self.amouse, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1,
                                                 column=1, padx=10, pady=10)

        logitecM1_lbl = Label(F3, text=pdr3, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=2,
                                                   column=0, padx=10, pady=10, sticky=W)
        logitecM_txt = Entry(F3, width=10, textvariable=self.logicm, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                padx=10, pady=10)


        drone1_lbl = Label(F3, text=pdr5, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(
                                            row=3, column=0, padx=10, pady=10,sticky=W)
        drone_txt = Entry(F3, width=10, textvariable=self.drone, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3,
                                             column=1, padx=10, pady=10)

        cphone1_lbl = Label(F3, text=pdr6, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=4,
                                                column=0, padx=10, pady=10, sticky=W)
        cphone_txt = Entry(F3, width=10, textvariable=self.cphone, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4,
                                                column=1, padx=10,  pady=10)



        laptopb1_lbl = Label(F3, text=pdr7, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=5,
                                                 column=0, padx=10, pady=10, sticky=W)
        laptopb_txt = Entry(F3, width=10, textvariable=self.laptopb, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5,
                                                column=1, padx=10,  pady=10)


        # ====================================================Laptops Frame=============================================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Teo's Laptops", font=('times new roman', 15, 'bold'),
                        fg=bg_color2, bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        hasee1_lbl = Label(F4, text=pdr14, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=0,
                                                column=0, padx=10,  pady=10, sticky=W)
        hasee_txt = Entry(F4, width=10, textvariable=self.hasee, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                            padx=10, pady=10)

        acer1_lbl = Label(F4, text=pdr15, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=1,
                                              column=0, padx=10, pady=10, sticky=W)
        acer_lotion_txt = Entry(F4, width=10, textvariable=self.acer, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1,
                                                column=1,  padx=10,  pady=10)


        macb1_lbl = Label(F4, text=pdr16, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=2,
                                              column=0, padx=10, pady=10,sticky=W)
        macb_txt = Entry(F4, width=10, textvariable=self.macb, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                             padx=10, pady=10)

        hp1_lbl = Label(F4, text=pdr17, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(
                                             row=3, column=0, padx=10, pady=10, sticky=W)
        hp_txt = Entry(F4, width=10, textvariable=self.hp, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3,
                                           column=1, padx=10, pady=10)

        dell1_lbl = Label(F4, text=pdr18, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=4,
                                                 column=0, padx=10, pady=10, sticky=W)
        dell_txt = Entry(F4, width=10, textvariable=self.dell, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4,
                                              column=1, padx=10, pady=10)

        asus1_lbl = Label(F4, text=pdr19, font=('times new roman', 16, 'bold'), bg=bg_color, fg=fg_color, ).grid(row=5,
                                                 column=0, padx=10, pady=10, sticky=W)
        asus_txt = Entry(F4, width=10, textvariable=self.asus, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5,
                                              column=1, padx=10, pady=10)

        #=============================================Display Frame====================================================

        F5 = Frame(self.root, bd=10, relief=GROOVE, bg='black')
        F5.place(x=1000, y=180, width=350, height=380)
        bill_title=Label(F5, text="Bill Display", font=('Baskerville Old Face', 15, 'bold'),fg='black', bg='light grey', bd=7, relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5, orient=VERTICAL)
        self.textarea=Text(F5,bg='white', font=('Baskerville Old Face' ,11, 'bold'), fg='black', yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #=============================================Button Frame==================================
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=('times new roman', 15, 'bold'),
                        fg=fg_color, bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl=Label(F6, text="Electronics1 Total P:", font=('times new roman', 14, 'bold'), fg=fg_color, bg=bg_color1)
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky=W)
        eletprice1_txt=Entry(F6, width=18, textvariable=self.eletprice1, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Electronics2 Total P: ", font=('times new roman', 14, 'bold'), fg=fg_color, bg=bg_color1)
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky=W)
        eletprice2_txt = Entry(F6, width=18,textvariable=self.eletprice2, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Laptop Total P:", font=('times new roman', 14, 'bold'), fg=fg_color, bg=bg_color1)
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky=W)
        lapprice_txt = Entry(F6, width=18, textvariable=self.lapprice, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Electronics1 Tax:", font=('times new roman', 14, 'bold'), fg=fg_color, bg=bg_color1)
        c1_lbl.grid(row=0, column=2, padx=20, pady=1, sticky=W)
        elettax1_txt = Entry(F6, width=18, textvariable=self.elettax1, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Electronics2 Tax: ", font=('times new roman', 14, 'bold'), fg=fg_color, bg=bg_color1)
        c2_lbl.grid(row=1, column=2, padx=20, pady=1, sticky=W)
        elettax2_txt = Entry(F6, width=18, textvariable=self.elettax2, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Laptop Tax:", font=('times new roman', 14, 'bold'), fg=fg_color, bg=bg_color1)
        c3_lbl.grid(row=2, column=2, padx=20, pady=1, sticky=W)
        laptax_txt = Entry(F6, width=18, textvariable=self.laptax, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6, bd=7, bg=bg_color, relief=GROOVE)
        btn_F.place(x=750, width=585, height=105)

        total1_btn=Button(btn_F,  command=self.total, text="Total", bg=bg_color2, fg="Gold", pady=15, bd=5, width=12,
                         font=('Baskerville Old Face', 12, 'bold')).grid(row=0, column=0, padx=5, pady=5)

        gbill_btn = Button(btn_F, text="Get Bill", command=self.bill_display, bg=bg_color2, fg="Gold", pady=15, bd=5, width=12,
                           font=('Baskerville Old Face', 12, 'bold')).grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg=bg_color2, fg="Gold", pady=15, bd=5, width=12,
                           font=('Baskerville Old Face', 12, 'bold')).grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_F, text="Exit", command=self.Exit, bg=bg_color2, fg="Gold", pady=15, bd=5, width=11,
                           font=('Baskerville Old Face', 12, 'bold')).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        self.c_t_p=self.thunder.get()*40
        self.c_a_p = self.amouse.get() * 50
        self.c_l_p = self.logicm.get() * 170
        self.c_d_p = self.drone.get() * 500
        self.c_c_p = self.cphone.get() * 400
        self.c_ll_p = self.laptopb.get() * 350

        self.total_eletprice1=float(
                                     self.c_t_p+
                                     self.c_a_p +
                                     self.c_l_p+
                                     self.c_d_p+
                                     self.c_c_p+
                                     self.c_ll_p
                                     )
        self.eletprice1.set("$. "+str(self.total_eletprice1))
        self.c_tax=round((self.total_eletprice1*0.05),2)
        self.elettax1.set("$. "+str(self.c_tax))

        self.d_m_p = self.mstick.get() * 30
        self.d_s_p = self.ssd.get() * 7500
        self.d_h_p = self.hdd.get() * 1700
        self.d_la_p = self.lan.get() * 500
        self.d_r_p = self.router.get() * 1400
        self.d_hdm_p = self.hdmi.get() * 350

        self.total_eletprice2 = float(
                                       self.d_m_p +
                                       self.d_s_p +
                                       self.d_h_p +
                                       self.d_la_p +
                                       self.d_r_p +
                                       self.d_hdm_p
                                      )
        self.eletprice2.set("$. "+str(self.total_eletprice2))
        self.d_tax=round((self.total_eletprice2 * 0.05),2)
        self.elettax2.set("$. " + str(self.d_tax))

        self.e_ha_p = self.mstick.get() * 7000
        self.e_ac_p = self.ssd.get() * 7500
        self.e_ma_p = self.hdd.get() * 17000
        self.e_hp_p = self.lan.get() * 5000
        self.e_de_p = self.router.get() * 9000
        self.e_as_p = self.hdmi.get() * 800

        self.total_lapprice = float(
                                     self.e_ha_p +
                                     self.e_ac_p +
                                     self.e_ma_p +
                                     self.e_hp_p +
                                     self.e_de_p +
                                     self.e_as_p
                                      )
        self.lapprice.set("$. "+str(self.total_lapprice))
        self.e_tax= round((self.total_lapprice * 0.05),2)
        self.laptax.set("$. " + str(self.e_tax))

        self.Grand_total=float(   self.total_eletprice1 +
                                  self.total_eletprice2 +
                                  self.total_lapprice +
                                  self.c_tax +
                                  self.d_tax +
                                  self.e_tax
                             )

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tTEOMAZIVILA'S IT-WORLD\n")
        self.textarea.insert(END,f"\n Bill Number: {self.c_bill.get()}")
        self.textarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number: {self.c_phone.get()}")
        self.textarea.insert(END, f"\n======================================")
        self.textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n======================================")

    def bill_display(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error", "Please Provide Customer Details!")
        elif self.eletprice1.get()=="$. 0.0" and self.eletprice2.get()=="$. 0.0" and self.lapprice.get()=="$. 0.0":
            messagebox.showerror("Error", "No Purchase Made!")
        else:
            self.welcome_bill()
            #=====================Eletronics1==============================
            if self.thunder.get()!=0:
                self.textarea.insert(END,f"\n Thunder Adt \t\t{self.thunder.get()}\t\t{self.c_t_p}")
            if self.amouse.get()!=0:
                self.textarea.insert(END,f"\n Apple Mouse\t\t{self.amouse.get()}\t\t{self.c_a_p}")
            if self.logicm.get()!=0:
                self.textarea.insert(END,f"\n Logitec M\t\t{self.logicm.get()}\t\t{self.c_l_p}")
            if self.drone.get()!=0:
                self.textarea.insert(END,f"\n Mac Drone\t\t{self.drone.get()}\t\t{self.c_d_p}")
            if self.cphone.get()!=0:
                self.textarea.insert(END,f"\n Cell Phone\t\t{self.cphone.get()}\t\t{self.c_c_p}")
            if self.laptopb.get()!=0:
                self.textarea.insert(END,f"\n Laptop Batt\t\t{self.laptopb.get()}\t\t{self.c_ll_p}")

            #=============================================Eletronics2============================
            if self.mstick.get()!=0:
                self.textarea.insert(END,f"\n M-Stick \t\t{self.mstick.get()}\t\t{self.d_m_p}")
            if self.ssd.get()!=0:
                self.textarea.insert(END,f"\n Ext SSD\t\t{self.ssd.get()}\t\t{self.d_s_p}")
            if self.hdd.get()!=0:
                self.textarea.insert(END,f"\n Ext HDD\t\t{self.hdd.get()}\t\t{self.d_h_p}")
            if self.lan.get()!=0:
                self.textarea.insert(END,f"\n LAN Cable\t\t{self.lan.get()}\t\t{self.d_la_p}")
            if self.router.get()!=0:
                self.textarea.insert(END,f"\n Net Router\t\t{self.router.get()}\t\t{self.d_r_p}")
            if self.hdmi.get()!=0:
                self.textarea.insert(END,f"\n HDMI Canle\t\t{self.hdmi.get()}\t\t{self.d_hdm_p}")

            #====================================Teo's Laptops==================================
            if self.hasee.get()!=0:
                self.textarea.insert(END,f"\n Hasee Gamer \t\t{self.hasee.get()}\t\t{self.e_ha_p}")
            if self.acer.get()!=0:
                self.textarea.insert(END,f"\n Acer Gamer\t\t{self.acer.get()}\t\t{self.e_ac_p}")
            if self.macb.get()!=0:
                self.textarea.insert(END,f"\n Mac B Pro\t\t{self.macb.get()}\t\t{self.e_ma_p}")
            if self.hp.get()!=0:
                self.textarea.insert(END,f"\n Hp proBook\t\t{self.hp.get()}\t\t{self.e_hp_p}")
            if self.dell.get()!=0:
                self.textarea.insert(END,f"\n Dell Gamer\t\t{self.dell.get()}\t\t{self.e_de_p}")
            if self.asus.get()!=0:
                self.textarea.insert(END,f"\n Asus Gamer\t\t{self.asus.get()}\t\t{self.e_as_p}")

            self.textarea.insert(END, f"\n-------------------------------------------------------------")
            if self.elettax1.get()!="$. 0.0":
                self.textarea.insert(END, f"\n Eletronics1 Tax\t\t\t{self.elettax1.get()}")
            if self.elettax2.get()!="$. 0.0":
                self.textarea.insert(END, f"\n Eletronics2 Tax\t\t\t{self.elettax2.get()}")
            if self.laptax.get()!="$. 0.0":
                self.textarea.insert(END, f"\n Laptop Tax\t\t\t{self.laptax.get()}")

            self.textarea.insert(END, f"\n Grand Total:\t\t\t $. {self.Grand_total}")
            self.textarea.insert(END, f"\n-------------------------------------------------------------")
            self.save_slip()

    def save_slip(self):
        op=messagebox.askyesno("RECEIPT", "Would you like to Save the Slip?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("customers/"+str(self.c_bill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("SAVED!", f"Receipt no: {self.c_bill} Saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("customers"):
            if i.split('.')[0]==self.c_bill.get():
                f1=open(f"customers/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
                if present=="no":
                    messagebox.showerror("Error", "Invalid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to CLEAR the Fields?")
        if op > 0:
            self.thunder.set(0)
            self.amouse.set(0)
            self.logicm.set(0)
            self.drone.set(0)
            self.cphone.set(0)
            self.laptopb.set(0)

            self.mstick.set(0)
            self.ssd.set(0)
            self.hdd.set(0)
            self.lan.set(0)
            self.router.set(0)
            self.hdmi.set(0)

            self.hasee.set(0)
            self.acer.set(0)
            self.macb.set(0)
            self.hp.set(0)
            self.dell.set(0)
            self.asus.set(0)

            self.eletprice1.set("")
            self.eletprice2.set("")
            self.lapprice.set("")

            self.elettax1.set("")
            self.elettax2.set("")
            self.laptax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.c_bill.set("")
            x = random.randint(1000, 9999)
            self.c_bill.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit(self):
        op=messagebox.askyesno("Exit", "Do you really want to EXIT?")
        if op>0:
            self.root.destroy()



root=Tk()
obj = Bill_App(root)
root.mainloop()