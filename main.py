import random
from tkinter import messagebox
import uuid
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from PIL import Image, ImageTk
import cx_Oracle
import pandas as pd
con = cx_Oracle.connect("C##Anjar/123456")
cur = con.cursor()
def paymentdetails(searchscreen):
    if (f.get() != '' and c.get() != ''):
        searchscreen.destroy()
        con = cx_Oracle.connect("C##Anjar/123456")
        cur = con.cursor()
        personaldetails = Tk()
        personaldetails.title("Personal details and Payment")
        personaldetails.resizable(0, 0)
        personaldetails.geometry("850x600+200+100")
        personaldetails.configure(bg="lavender")
        frame_personal = Frame(personaldetails).pack(side="top")
        gender = StringVar()
        pname = StringVar()
        page = StringVar()
        pnumber = StringVar()
        pemail = StringVar()
        pnameoncard = StringVar()
        pexpmon = StringVar()
        pcardno = StringVar()

        def price():
            if f.get() == '601':
                if c.get() == "Business":
                    rate = 4200
                elif c.get() == "Economy":
                    rate = 2670
                return rate
            elif f.get() == '602':
                if c.get() == "Business":
                    rate = 9560
                elif c.get() == "Economy":
                    rate = 6390
                return rate
            elif f.get() == '603':
                if c.get() == "Business":
                    rate = 11940
                elif c.get() == "Economy":
                    rate = 7340
                return rate
            elif f.get() == '604':
                if c.get() == "Business":
                    rate = 9780
                elif c.get() == "Economy":
                    rate = 6500
                return rate
            elif f.get() == '605':
                if c.get() == "Business":
                    rate = 13650
                elif c.get() == "Economy":
                    rate = 9300
                return rate
            elif f.get() == '606':
                if c.get() == "Business":
                    rate = 8220
                elif c.get() == "Economy":
                    rate = 4800
                return rate
        fno = f.get()
        stat1 = ''' select journey_from,destination from journey_details where flight_no = :y'''
        cur.execute(stat1, y=fno)
        var1 = cur.fetchone()
        stat2 = '''select flight_name from flight where flight_no = :z'''
        cur.execute(stat2, z=fno)
        var2 = cur.fetchone()
        from_label = Label(personaldetails, text="FROM", font=(
            "Consolas", 10), bg="lavender", fg="black", width=10).place(x=660, y=49)
        todestination_label = Label(personaldetails, text="TO", font=(
            "Consolas", 10), bg="lavender", fg="black", width=10).place(x=750, y=49)
        from_entrylabel = Label(personaldetails, text=var1[0], font=(
            "Consolas", 12), bg="#F6E7D8", fg="black", width=10).place(x=640, y=69)
        todestinatiion_entrylabel = Label(personaldetails, text=var1[1], font=(
            "Consolas", 12), bg="#F6E7D8", fg="black", width=10).place(x=740, y=69)

        Flightno_label = Label(personaldetails, text="FLIGHT ", font=(
            "Consolas", 10), bg="lavender", fg="black", width=10).place(x=700, y=115)

        flighno_entrylabel = Label(personaldetails, text=f.get(), font=(
            "Consolas", 12), bg="#F6E7D8", fg="black", width=10).place(x=640, y=140)
        flightname_entrylabel = Label(personaldetails, text=var2[0], font=(
            "Consolas", 12), bg="#F6E7D8", fg="black", width=10).place(x=740, y=140)

        Class_label = Label(personaldetails, text="CLASS", font=(
            "Consolas", 10), bg="lavender", fg="black", width=10).place(x=660, y=186)
        Classname_entrylabel = Label(personaldetails, text=c.get(), font=(
            "Consolas", 12), bg="#F6E7D8", fg="black", width=10).place(x=640, y=210)

        Price_label = Label(personaldetails, text="PRICE(Rs.)", font=(
            "Consolas", 10), bg="lavender", fg="black", width=10).place(x=750, y=186)
        Price_entrylabel = Label(personaldetails, text=price(), font=(
            "Consolas", 12), bg="#F6E7D8", fg="black", width=10).place(x=740, y=210)

        heading_color = Label(frame_personal, text="a", width=200, height=2,
                              bg="#120c6e", fg="#120c6e", relief='flat').pack(side="top")
        heading_label = Label(frame_personal, text="PERSONAL DETAILS", font=(
            "Sitka Small Semibold", 14), width=20, height=0, bg="#120c6e", fg="white").place(x=5, y=1)

        name_label = Label(personaldetails, text="Name:", font=(
            "Sitka Small Semibold", 12), bg="lavender", fg="black", width=10).place(x=20, y=57)
        age_label = Label(personaldetails, text="Age:", font=(
            "Sitka Small Semibold", 12), bg="lavender", fg="black", width=9).place(x=20, y=107)
        number_label = Label(personaldetails, text="Phone no:", font=(
            "Sitka Small Semibold", 12), bg="lavender", fg="black", width=10).place(x=20, y=157)
        email_label = Label(personaldetails, text="Email Id:", font=(
            "Sitka Small Semibold", 12), bg="lavender", fg="black", width=10).place(x=20, y=207)
        gender_label = Label(personaldetails, text="Gender:", font=(
            "Sitka Small Semibold", 13), bg="lavender", fg="black", width=10).place(x=19, y=257)

        name_entry = Entry(personaldetails, width=20, bg="#EEEEEE", font=(
            "Microsoft PhagsPa", 14), textvariable=pname).place(x=140, y=60)
        age_entry = Entry(personaldetails, width=20, bg="#EEEEEE", font=(
            "Microsoft PhagsPa", 14), textvariable=page).place(x=140, y=110)
        number_entry = Entry(personaldetails, width=17, bg="#EEEEEE", font=(
            "Microsoft PhagsPa", 14), textvariable=pnumber).place(x=170, y=160)
        numbernineone_label = Label(personaldetails, text="+91 ", bg="lavender",
                                    fg="black", font=("arial", 14), width=3).place(x=130, y=160)
        email_entry = Entry(personaldetails, width=23, bg="#EEEEEE", font=(
            "Consoals", 12), textvariable=pemail).place(x=140, y=210)
        male_radiobutton = Radiobutton(personaldetails, text="Male", font=(
            "Consoals", 13), width=10, bg="lavender", variable=gender, value=0, activebackground="lavender").place(x=120, y=260)
        female_radiobutton = Radiobutton(personaldetails, text="Female", font=(
            "Consoals", 13), width=10, bg="lavender", variable=gender, value=1, activebackground="lavender").place(x=220, y=260)

        heading_color = Label(frame_personal, text="a", width=200, height=2,
                              bg="#120c6e", fg="#120c6e", relief='flat').place(x=0, y=300)
        paymentdetails_label = Label(frame_personal, text="PAYMENT DETAILS", font=(
            "Sitka Small Semibold", 14), width=20, height=0, bg="#120c6e", fg="white").place(x=0, y=300)

        cardheading_label = Label(frame_personal, text="Credit/Debit/ATM Card", font=(
            "Microsoft YaHei UI", 11), bg="lavender").place(x=15, y=350)
        cardnumber_label = Label(personaldetails, text="Card Number:", font=(
            "Sitka Small Semibold", 11), bg="lavender", fg="black", width=12).place(x=15, y=390)
        cardnumber_entry = Entry(personaldetails, width=20, bg="#EEEEEE", textvariable=pcardno, font=(
            "Consoals", 14)).place(x=155, y=390)

        nameoncard_label = Label(personaldetails, text="Name on Card:", font=(
            "Sitka Small Semibold", 11), bg="lavender", fg="black", width=12).place(x=16, y=440)
        nameoncard_entry = Entry(personaldetails, width=20, textvariable=pnameoncard, bg="#EEEEEE", font=(
            "Consoals", 14)).place(x=155, y=440)

        expirymonth_label = Label(personaldetails, text="Exp.Month &\nYear(MM/YY)", font=(
            "Sitka Small Semibold", 11), bg="lavender", fg="black", width=12).place(x=15, y=490)
        expirymonth_entry = Entry(personaldetails, width=20, bg="#EEEEEE", textvariable=pexpmon, font=(
            "Consoals", 14)).place(x=155, y=500)

        def back():
            bookticket(personaldetails)

        def bookit():
            if (pname.get() == "" or page.get() == "" or gender.get() == "" or pemail.get() == "" or pnumber.get() == "" or pnameoncard.get() == ""
                    or pexpmon.get() == "" or pcardno.get() == ""):
                messagebox.showerror(
                    "Error", "PLEASE FILL ALL THE REQUIRED DETAILS !!")
            else:
                con = cx_Oracle.connect("C##Anjar/123456")
                cur = con.cursor()
                if gender.get() == "0":
                    gen = "male"
                elif gender.get() == "1":
                    gen = "female"
                ppname = pname.get()
                ppage = int(page.get())
                ppflight = int(f.get())
                ppemail = pemail.get()
                ppnumber = int(pnumber.get())
                pid = str(uuid.uuid4())
                pid = pid[:5]

                ticno = random.randint(10000, 99999)
                seatno = random.randint(100, 500)
                clas = c.get()
                fare = price()

                stat1 = '''insert into passanger_details values(:a,:b,:c,:d,:e,:f,:g)'''
                stat2 = '''insert into ticket_details values(:z,:y,:x,:w,:v)'''
                cur.execute(stat1, [pid, ppname, ppage,
                            gen, ppemail, ppnumber, ppflight])
                cur.execute(stat2, [ticno, seatno, clas, fare, pid])
                con.commit()
                response = messagebox.showinfo(
                    "Confirmation", "You have successfully booked the ticket.\n\nYour passangerid has been generated!\n\nclick ok to view!")
                if response == "ok":
                    messagebox.showinfo("Passanger id", pid)
                    if response == "ok":
                        ticketdetails(personaldetails)

        paynow_button = Button(personaldetails, text="PAY NOW", width=10, bd=3, font=(
            "Sitka Small Semibold", 10), bg="#035397", fg="white", activebackground="#B7CADB", command=bookit).place(x=730, y=550)
        cancel_button = Button(personaldetails, text="BACK", width=10, bd=3, font=(
            "Sitka Small Semibold", 10), bg="#035397", fg="white", activebackground="#B7CADB", command=back).place(x=620, y=550)

        con.close()
        personaldetails.mainloop()
    else:
        messagebox.showerror(
            "Error", "PLEASE SELECT BOTH FLIGHT NO. AND CLASS !")


def bookticket(root):
    root.destroy()
    searchscreen = Tk()
    searchscreen.title("Book Flight")
    searchscreen.geometry("970x600+200+100")
    searchscreen.resizable(0, 0)
    searchscreen.configure(bg="lavender")
    frame_search = Frame(searchscreen).pack(side="top")
    global f
    global c
    f = StringVar()
    c = StringVar()
    heading_color = Label(frame_search, text="a", width=200, height=2,
                          bg="#120c6e", fg="#120c6e", relief='flat').pack(side="top")
    heading_label = Label(frame_search, text="AVAILABLE  FLIGHTS", font=(
        "Sitka Small Semibold", 14), width=20, height=0, bg="#120c6e", fg="white").place(x=5, y=1)

    flightno_label = Label(frame_search, text="Flight no.", bg="#4d77ff", fg="white", font=(
        "Consolas", 12), width=11).place(x=30, y=60)
    flightname_label = Label(frame_search, text="Flight name", bg="#4d77ff", fg="white", font=(
        "Consolas", 12), width=11).place(x=160, y=60)
    flightfrom_label = Label(frame_search, text="From", bg="#4d77ff", fg="white", font=(
        "Consolas", 12), width=11).place(x=290, y=60)
    flightto_label = Label(frame_search, text="to", bg="#4d77ff", fg="white", font=(
        "Consolas", 12), width=11).place(x=420, y=60)
    flightdepttime_label = Label(frame_search, text="Dept. time", bg="#4d77ff", fg="white", font=(
        "Consolas", 12), width=11).place(x=550, y=60)
    flightarrtime_label = Label(frame_search, text="Arrival time", bg="#4d77ff", fg="white", font=(
        "Consolas", 12), width=13).place(x=680, y=60)
    fligthdate_label = Label(frame_search, text="Date", bg="#4d77ff", fg="white", font=(
        "Consolas", 12), width=11).place(x=830, y=60)

    flightno1 = Label(frame_search, text="601", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=30, y=100)
    flightname1 = Label(frame_search, text="Air India", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=160, y=100)
    flightfrom1 = Label(frame_search, text="Amritsar", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=290, y=100)
    flighto1 = Label(frame_search, text="New Delhi", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=420, y=100)
    flightdepttime1 = Label(frame_search, text="16:10", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=550, y=100)
    flightarrtime1 = Label(frame_search, text="18:05", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=13).place(x=680, y=100)
    flight1date = Label(frame_search, text="17-may-2022", bg="#F6E7D8",
                        fg="black", font=("Consolas", 12), width=12).place(x=825, y=100)

    flightno2 = Label(frame_search, text="602", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=30, y=140)
    flightname2 = Label(frame_search, text="Indigo", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=160, y=140)
    flightfrom1 = Label(frame_search, text="New Delhi", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=290, y=140)
    flighto2 = Label(frame_search, text="Bengaluru", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=420, y=140)
    flightdepttime2 = Label(frame_search, text="20:10", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=550, y=140)
    flightarrtime2 = Label(frame_search, text="23:15", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=13).place(x=680, y=140)
    flight2date = Label(frame_search, text="19-may-2022", bg="#F6E7D8",
                        fg="black", font=("Consolas", 12), width=12).place(x=825, y=140)

    flightno3 = Label(frame_search, text="603", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=30, y=180)
    flightname3 = Label(frame_search, text="GoAir", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=160, y=180)
    flightfrom3 = Label(frame_search, text="New Delhi", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=290, y=180)
    flighto3 = Label(frame_search, text="Mumbai", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=420, y=180)
    flightdepttime3 = Label(frame_search, text="08:10", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=550, y=180)
    flightarrtime3 = Label(frame_search, text="10:30", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=13).place(x=680, y=180)
    flight3date = Label(frame_search, text="21-may-2022", bg="#F6E7D8",
                        fg="black", font=("Consolas", 12), width=12).place(x=825, y=180)

    flightno4 = Label(frame_search, text="604", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=30, y=220)
    flightname4 = Label(frame_search, text="SpiceJet", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=160, y=220)
    flightfrom4 = Label(frame_search, text="Amritsar", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=290, y=220)
    flighto4 = Label(frame_search, text="Patna", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=420, y=220)
    flightdepttime4 = Label(frame_search, text="14:00", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=550, y=220)
    flightarrtime4 = Label(frame_search, text="16:20", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=13).place(x=680, y=220)
    flight4date = Label(frame_search, text="25-may-2022", bg="#F6E7D8",
                        fg="black", font=("Consolas", 12), width=12).place(x=825, y=220)

    flightno5 = Label(frame_search, text="605", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=30, y=260)
    flightname5 = Label(frame_search, text="Vistara", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=160, y=260)
    flightfrom5 = Label(frame_search, text="Amritsar", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=290, y=260)
    flighto5 = Label(frame_search, text="Hyderabad", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=420, y=260)
    flightdepttime5 = Label(frame_search, text="11:30", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=550, y=260)
    flightarrtime5 = Label(frame_search, text="15:10", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=13).place(x=680, y=260)
    flight6date = Label(frame_search, text="23-may-2022", bg="#F6E7D8",
                        fg="black", font=("Consolas", 12), width=12).place(x=825, y=260)

    flightno6 = Label(frame_search, text="606", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=30, y=300)
    flightname6 = Label(frame_search, text="Jet Airways", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=160, y=300)
    flightfrom6 = Label(frame_search, text="New Delhi", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=290, y=300)
    flighto6 = Label(frame_search, text="Kolkata", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=420, y=300)
    flightdepttime6 = Label(frame_search, text="17:45", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=11).place(x=550, y=300)
    flightarrtime6 = Label(frame_search, text="19:50", bg="#F6E7D8", fg="black", font=(
        "Consolas", 12), width=13).place(x=680, y=300)
    flight6date = Label(frame_search, text="26-may-2022", bg="#F6E7D8",
                        fg="black", font=("Consolas", 12), width=12).place(x=825, y=300)

    selectflightlabel = Label(frame_search, text="Select flight no.", font=(
        "Sitka Small Semibold", 12), width=13, bg="#120c6e", fg="white").place(x=150, y=380)
    flightno_combobox = Combobox(frame_search, values=[601, 602, 603, 604, 605, 606], font=(
        "Segoe UI Semibold", 10), textvariable=f).place(x=150, y=420)

    selectdatelabel = Label(frame_search, text="Select class", font=(
        "Sitka Small Semibold", 12), width=12, bg="#120c6e", fg="white").place(x=350, y=380)
    date_combobox = Combobox(frame_search, values=['Business', 'Economy'], font=(
        "Segoe UI Semibold", 10), textvariable=c).place(x=350, y=420)

    def back():
        searchscreen.destroy()
        frontscreen()
    flightbook_button = Button(frame_search, text="Proceed", width=9, font=("Sitka Small Semibold", 10), bd=3, bg="#035397",
                               fg="white", activebackground="#B7CADB", command=lambda: paymentdetails(searchscreen)).place(x=850, y=550)
    backhome_button = Button(frame_search, text="Back", width=9, font=("Sitka Small Semibold", 10),
                             bd=3, bg="#035397", fg="white", activebackground="#B7CADB", command=back).place(x=746, y=550)

    searchscreen.mainloop()


def frontscreen():
    root = Tk()
    root.title("Flight reservation system")
    root.geometry("800x533+200+100")
    root.resizable(0, 0)
    frame1 = Frame(root, bg="#E9D5DA").place(width=400, height=800, x=0, y=0)
    frame2 = Frame(root, bg="#827397").place(width=400, height=533, x=400, y=0)
    x = ImageTk.PhotoImage(Image.open("planewall.jpg"))
    y = Label(root, image=x).place(width=800, height=533)

    heading = Label(frame1, text="FLIGHT\t RESERVATION\tSYSTEM", width=60, fg="white",
                    bg='#120c6e', relief="sunken", font=("Source Serif Pro Semibold", 25)).pack()
    search_button = Button(frame2, text="BOOK FLIGHT", font=("Source Sans Pro Semibold", 13), relief="raised", bg="#035397",
                           fg='white', bd=5, activebackground="#B7CADB", width=14, command=lambda: bookticket(root)).place(x=50, y=440)
    ticketdetails_button = Button(frame2, text="TICKET DETAILS", font=("Source Sans Pro Semibold", 13), bd=5, bg="#035397",
                                  fg='white', activebackground="#B7CADB", relief="raised", width=14, command=lambda: ticketdetails(root)).place(x=320, y=440)
    admin_button = Button(frame2, text="ADMIN LOGIN", font=("Source Sans Pro Semibold", 13), relief="raised", bd=5,
                          bg="#035397", fg='white', activebackground="#B7CADB", width=14, command=lambda: adminlogin(root)).place(x=600, y=440)

    root.mainloop()


def ticketdetails(root):
    root.destroy()
    ticketroot = Tk()
    ticketroot.geometry("700x560+200+100")
    ticketroot.resizable(0, 0)
    ticketroot.title("TICKET DETAILS")

    ticketroot.config(bg="lavender")
    passid = StringVar()

    con = cx_Oracle.connect("C##Anjar/123456")
    cur = con.cursor()

    ticketframe = Frame(ticketroot, bg="white").place(
        width=640, height=340, x=30, y=170)

    ticketpic = ImageTk.PhotoImage(Image.open("2ticketpic.png"))
    ticketpiclabel = Label(ticketroot, image=ticketpic, bg="lavender").place(
        height=128, width=200, x=450, y=40)

    searchpic = ImageTk.PhotoImage(Image.open("2search.png"))
    searchpiclabel = Label(ticketroot, image=searchpic).place(
        height=15, width=15, x=160, y=130)

    profilepic = ImageTk.PhotoImage(Image.open("2profilepic.png"))
    profilepiclabel = Label(ticketframe, image=profilepic).place(
        height=130, width=130, x=40, y=180)

    ticketdetailsheading_label = Label(ticketroot, text="TICKET DETAILS", width=60,
                                       bg="#120c6e", fg="white", font=("Sitka Small Semibold", 15)).pack()

    enterpassangeid_label = Label(ticketroot, text="ENTER PASSANGER ID :", font=(
        "Source Serif Pro", 13), bg="lavender", fg="black").place(x=30, y=40)
    enterpassangeid_entry = Entry(ticketroot, font=(
        "Source Serif Pro", 14), bg="#EEEEEE", width=20, textvariable=passid).place(x=30, y=75)

    def filldetails():
        psid = passid.get()
        stat1 = '''select * from passanger_details where passanger_id = :a'''
        stat2 = '''select * from ticket_details where passanger_id = :b'''
        stat3 = '''select * from flight where flight_no = :c'''
        stat4 = ''' select * from journey_details where flight_no = :d'''
        cur.execute(stat1, a=psid)
        var1 = cur.fetchone()
        cur.execute(stat2, b=psid)
        var2 = cur.fetchone()
        if var1 == None and var2 == None:
            messagebox.showerror("error", "PASSANGER ID DOES NOT EXIST")
        else:
            passangeridentry_label = Label(ticketframe, text=passid.get(), bg="#F7E9D7", font=(
                "Source Serif Pro", 13), fg="black", width=10).place(x=219, y=205)
            ticketnoentry_label = Label(ticketframe, text=var2[0], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), fg="black", width=8).place(x=540, y=205)
            Flightnoentry_label = Label(ticketframe, text=var1[6], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=5).place(x=219, y=290)
            flno = var1[6]
            cur.execute(stat3, c=flno)
            var3 = cur.fetchone()
            Flightnameentry_label = Label(ticketframe, text=var3[1], bg="#F7E9D7", fg="black", font=(
                "Source Serif Pro", 13), width=9).place(x=540, y=290)
            Passangernameentry_label = Label(ticketframe, text=var1[1], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=13).place(x=215, y=380)
            classentry_label = Label(ticketframe, text=var2[2], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), fg="black", width=10).place(x=380, y=290)
            Passangerageentry_label = Label(ticketframe, text=var1[2], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=4).place(x=430, y=380)
            Passangersex_label = Label(ticketframe, text=var1[3], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=7).place(x=570, y=380)
            fromentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=10).place(x=120, y=450)
            destinationentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=10).place(x=360, y=450)
            seatnoentry_label = Label(ticketframe, text=var2[1], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=5).place(x=570, y=450)
            cur.execute(stat4, d=flno)
            var4 = cur.fetchone()
            fromentry_label = Label(ticketframe, text=var4[0], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=10).place(x=120, y=450)
            destinationentry_label = Label(ticketframe, text=var4[1], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), width=10).place(x=360, y=450)
            date = str(var4[2])
            x = date.split()
            dateentry_label = Label(ticketframe, text=x[0], bg="#F7E9D7", font=(
                "Source Serif Pro", 13), fg="black", width=10).place(x=380, y=205)
            passid.set('')

    search_button = Button(ticketroot, text="SEARCH", font=("Microsoft Sans Serif", 11), activebackground="#B7CADB",
                           width=12, bg="#035397", fg="white", bd=4, relief="raised", command=filldetails).place(x=30, y=118)

    passangeridheading_label = Label(ticketframe, text="Passanger Id:", bg="white", font=(
        "Source Serif Pro", 13)).place(x=220, y=175)
    passangeridentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), fg="black", width=10).place(x=219, y=205)

    dateheading_label = Label(ticketframe, text="Date:", bg="white", font=(
        "Source Serif Pro", 13)).place(x=400, y=175)
    dateentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), fg="black", width=10).place(x=380, y=205)

    ticketnoheading_label = Label(ticketframe, text="Ticket No:", bg="white", font=(
        "Source Serif Pro", 13)).place(x=540, y=175)
    ticketnoentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), fg="black", width=8).place(x=540, y=205)

    Flightnotitle_label = Label(ticketframe, text="Flight No:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=219, y=255)
    Flightnametitle_label = Label(ticketframe, text="Flight Name:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=540, y=255)

    classheading_label = Label(ticketframe, text="Class:", bg="white", font=(
        "Source Serif Pro", 13)).place(x=400, y=255)
    classentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), fg="black", width=10).place(x=380, y=290)

    Flightnoentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), width=5).place(x=219, y=290)
    Flightnameentry_label = Label(ticketframe, text="", bg="#F7E9D7", fg="black", font=(
        "Source Serif Pro", 13), width=9).place(x=540, y=290)

    separation_label = Label(
        ticketframe, text="--------------------------------------------------------------------------------------------------------------------------", bg="white").place(x=40, y=340)

    PassNametitle_label = Label(ticketframe, text="Passanger name:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=60, y=380)
    Passangernameentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), width=13).place(x=215, y=380)

    PassAgetitle_label = Label(ticketframe, text="Age:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=380, y=380)
    Passangerageentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), width=4).place(x=430, y=380)

    Passsextitle_label = Label(ticketframe, text="Sex:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=520, y=380)
    Passangersex_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), width=7).place(x=570, y=380)

    fromorigin_label = Label(ticketframe, text="From:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=60, y=450)
    fromentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), width=10).place(x=120, y=450)

    destinationtitle_label = Label(ticketframe, text="Destination:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=250, y=450)
    destinationentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), width=10).place(x=360, y=450)

    seatnotitle_label = Label(ticketframe, text="Seat No:", font=(
        "Source Serif Pro", 13), bg="white", fg="black").place(x=490, y=450)
    seatnoentry_label = Label(ticketframe, text="", bg="#F7E9D7", font=(
        "Source Serif Pro", 13), width=5).place(x=570, y=450)

    def back():
        ticketroot.destroy()
        frontscreen()
    backbuttn = Button(ticketroot, text="Back", font=("Microsoft Sans Serif", 10), activebackground="#B7CADB",
                       width=8, bg="#035397", fg="white", bd=4, relief="raised", command=back).place(x=600, y=519)
    ticketroot.mainloop()


def adminlogin(root):
    root.destroy()
    adminroot = Tk()
    adminroot.geometry("500x550+400+100")
    adminroot.resizable(0, 0)
    adminroot.title("ADMIN LOGIN")
    adminroot.config(bg="lavender")
    global usrnme
    global pswd
    usrnme = StringVar()
    pswd = StringVar()
    adminframe = Frame(adminroot, bg="white").place(
        width=300, height=420, x=100, y=90)

    adminloginheading_label = Label(adminroot, text="Admin Login", font=(
        "Sitka Small Semibold", 14), bg="#120c6e", fg="white", width=60).pack()

    admindp = ImageTk.PhotoImage(Image.open("2admindpnew.png"))
    admindp_label = Label(adminframe, image=admindp).place(x=200, y=100)

    Username_label = Label(adminframe, text="User name", font=(
        "Microsoft YaHei UI", 12), fg="black", bg="white").place(x=115, y=210)
    username_entry = Entry(adminframe, width=25, bg="#EEEEEE", font=(
        "Microsoft PhagsPa", 14), textvariable=usrnme).place(x=120, y=240)

    password_label = Label(adminframe, text="Password", font=(
        "Microsoft YaHei UI", 12), fg="black", bg="white").place(x=115, y=300)
    password_entry = Entry(adminframe, width=25, show="*", bg="#EEEEEE",
                           font=("Microsoft PhagsPa", 14), textvariable=pswd).place(x=115, y=330)

    login_button = Button(adminframe, text="Login", font=("Sitka Small Semibold", 11), activebackground="#B7CADB", width=11,
                          bg="#035397", fg="white", bd=4, relief="raised", command=lambda: bookingdetails(adminroot)).place(x=185, y=400)
    
    def back():
        adminroot.destroy()
        frontscreen()

    backbutton = Button(adminroot, text="Back", font=("Microsoft Sans Serif", 9), activebackground="#B7CADB",
                        width=8, bg="#035397", fg="white", bd=4, command=back).place(x=5, y=40)

    adminroot.mainloop()


def bookingdetails(adminroot):
    if usrnme.get() == "admin" and pswd.get() == "admin":
        adminroot.destroy()
        passroot = Tk()
        passroot.title("All Bookings")
        passroot.geometry("900x600+200+100")
        passroot.configure(bg="lavender")
        passroot.resizable(0, 0)

        bookingdetails_label = Label(passroot, text="All Bookings", font=(
            "Sitka Small Semibold", 14), bg="#120c6e", fg="white", width=90).pack()

        con = cx_Oracle.connect("C##Anjar/123456")
        cur = con.cursor()

        Quote = pd.read_sql_query("select * from passanger_details", con)
        Quote = Quote.set_index('PASSANGER_ID')
        T = Text(passroot, height=60, width=200)
        T.pack()

        T.insert(tk.END, Quote)

        T.config(state='disabled')

        def back():
            passroot.destroy()
            frontscreen()

        backbutton = Button(passroot, text="Home", font=("Microsoft Sans Serif", 11), activebackground="#B7CADB",
                            width=8, bg="#035397", fg="white", bd=4, command=back).place(x=800, y=550)

        passroot.mainloop()
    elif usrnme.get() == "" or pswd.get() == "":
        messagebox.showerror("Error!", "missing credentials !")

    else:
        messagebox.showerror("Error!", "Bad credentials !")


frontscreen()
