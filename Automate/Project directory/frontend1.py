from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("AUTOMATE")
root.iconbitmap("Project directory\Icons\3xhumed-Mega-Games-Pack-38-Prey-logo-1.ico")

img1 = ImageTk.PhotoImage(Image.open("twilio-logomark-black.png"))

def window3():
    top2 = Toplevel()
    top2.title("AUTOMATE")
    top2.iconbitmap("Project directory\Icons\3xhumed-Mega-Games-Pack-38-Prey-logo-1.ico")
    label=Label(top2,text="how many minutes before you want to recieve a notification for every class?")
    label.grid(row=0,column=0)
    notifytime=Entry(top2,borderwidth=5,width=5)
    notifytime.insert(0,"5")
    notifytime.grid(row=1,column=0)
    def twiliowindow():
        top3 = Toplevel()
        top3.title("AUTOMATE")
        top3.iconbitmap("Project directory\Icons\3xhumed-Mega-Games-Pack-38-Prey-logo-1.ico")
        

        global img1
        img1 = ImageTk.PhotoImage(Image.open("twilio-logomark-black.png"))
        icon1 = Label(image=img)
        icon1.grid(row=0, column=0)

        label=Label(top3,text="Attach Your Twilio Account")
        label.grid(row=1,column=0)

        account_sid = Entry(top3, borderwidth=2, width=25)
        account_sid.insert(0, "account sid")
        account_sid.grid(row=2,column=0)

        auth_token = Entry(top3, borderwidth=2, width=25)
        auth_token.insert(0, "authorization token")
        auth_token.grid(row=3,column=0)

        twilio_num = Entry(top3, borderwidth=2, width=25)
        twilio_num.insert(0, "twilio number")
        twilio_num.grid(row=4,column=0)

        phone_no = Entry(top3, borderwidth=2, width=25)
        phone_no.insert(0, "enter your mobile number")
        phone_no.grid(row=5,column=0)

        def fun1():
            label3=Label(top3,text="your twilio account is succesfully attached!")
            label3.grid(row=7,column=0)

        submitbtn1=Button(top3,text="Attach",command=fun1)
        submitbtn1.grid(row=6,column=0)

        status = Label(top3, text="Twilio Account Page", bd=2, relief=SUNKEN, anchor=E)
        status.grid(row=8, column=0, sticky=W+E)

    def fun():
        label=Label(top2,text="you are successfully submitted")
        label1 = Label(top2, text="Return To The Home Screen")
        label.grid(row=4, column=0)
        label1.grid(row=5, column=0)
    submitbtn=Button(top2,text="Submit",command=fun)
    submitbtn.grid(row=2,column=0)
    twiliobtn = Button(top2, text="Attach Your Twilio Account",command=twiliowindow)
    twiliobtn.grid(row=3, column=0)
    status = Label(root, text="page 3 of 3", bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=6, column=0, sticky=W+E)




def window2():
   
    top1=Toplevel()
    top1.title("AUTOMATE")
    top1.iconbitmap("Project directory\Icons\3xhumed-Mega-Games-Pack-38-Prey-logo-1.ico")
    
    
    label=Label(top1,text="schedule your classes here")
    label.grid(row=0, column=0, columnspan=3)
    subjectname1=Entry(top1,borderwidth=2)
    subjectname1.insert(0,"Mathematics")
    subjectname1.grid(row=1, column=0)
    subjectname2 = Entry(top1, borderwidth=2)
    subjectname2.insert(0,"Mathematics")
    subjectname2.grid(row=2, column=0)
    subjectname3 = Entry(top1, borderwidth=2)
    subjectname3.insert(0, "Mathematics")
    subjectname3.grid(row=3, column=0)
    subjectname4 = Entry(top1, borderwidth=2)
    subjectname4.insert(0, "Mathematics")
    subjectname4.grid(row=4, column=0)
    subjectname5 = Entry(top1, borderwidth=2)
    subjectname5.insert(0, "Mathematics")
    subjectname5.grid(row=5, column=0)
    subjectname6 = Entry(top1, borderwidth=2)
    subjectname6.insert(0, "Mathematics")
    subjectname6.grid(row=6, column=0)
    subjectname7 = Entry(top1, borderwidth=2)
    subjectname7.insert(0, "Mathematics")
    subjectname7.grid(row=7, column=0)
    subjectname8 = Entry(top1, borderwidth=2)
    subjectname8.insert(0, "Mathematics")
    subjectname8.grid(row=8, column=0)
    subjectname9 = Entry(top1, borderwidth=2)
    subjectname9.insert(0, "Mathematics")
    subjectname9.grid(row=9, column=0)
    subjectname10 = Entry(top1, borderwidth=2)
    subjectname10.insert(0, "Mathematics")
    subjectname10.grid(row=10, column=0)

    subjecttime1 = Entry(top1, borderwidth=2,width=5)
    subjecttime1.insert(0, "08:00")
    subjecttime1.grid(row=1, column=1)
    subjecttime2 = Entry(top1, borderwidth=2, width=5)
    subjecttime2.insert(0, "08:00")
    subjecttime2.grid(row=2, column=1)
    subjecttime3 = Entry(top1, borderwidth=2, width=5)
    subjecttime3.insert(0, "08:00")
    subjecttime3.grid(row=3, column=1)
    subjecttime4 = Entry(top1, borderwidth=2, width=5)
    subjecttime4.insert(0, "08:00")
    subjecttime4.grid(row=4, column=1)
    subjecttime5 = Entry(top1, borderwidth=2, width=5)
    subjecttime5.insert(0, "08:00")
    subjecttime5.grid(row=5, column=1)
    subjecttime6 = Entry(top1, borderwidth=2, width=5)
    subjecttime6.insert(0, "08:00")
    subjecttime6.grid(row=6, column=1)
    subjecttime7 = Entry(top1, borderwidth=2, width=5)
    subjecttime7.insert(0, "08:00")
    subjecttime7.grid(row=7, column=1)
    subjecttime8 = Entry(top1, borderwidth=2, width=5)
    subjecttime8.insert(0, "08:00")
    subjecttime8.grid(row=8, column=1)
    subjecttime9 = Entry(top1, borderwidth=2, width=5)
    subjecttime9.insert(0, "08:00")
    subjecttime9.grid(row=9, column=1)
    subjecttime10 = Entry(top1, borderwidth=2, width=5)
    subjecttime10.insert(0, "08:00")
    subjecttime10.grid(row=10, column=1)
    
    googlemeetlink1 = Entry(top1, borderwidth=2,width=50)
    googlemeetlink1.insert(0, "classmeetlink")
    googlemeetlink1.grid(row=1, column=2)
    googlemeetlink2 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink2.insert(0, "classmeetlink")
    googlemeetlink2.grid(row=2, column=2)
    googlemeetlink3 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink3.insert(0,"classmeetlink")
    googlemeetlink3.grid(row=3, column=2)
    googlemeetlink4 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink4.insert(0, "classmeetlink")
    googlemeetlink4.grid(row=4, column=2)
    googlemeetlink5 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink5.insert(0, "classmeetlink")
    googlemeetlink5.grid(row=5, column=2)
    googlemeetlink6 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink6.insert(0, "classmeetlink")
    googlemeetlink6.grid(row=6, column=2)
    googlemeetlink7 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink7.insert(0,"classmeetlink")
    googlemeetlink7.grid(row=7, column=2)
    googlemeetlink8 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink8.insert(0,"classmeetlink")
    googlemeetlink8.grid(row=8, column=2)
    googlemeetlink9 = Entry(top1, borderwidth=2, width=50)
    googlemeetlink9.insert(0,"classmeetlink")
    googlemeetlink9.grid(row=9, column=2)
    googlemeetlink10 = Entry(top1, borderwidth=2,width=50)
    googlemeetlink10.insert(0, "classmeetlink")
    googlemeetlink10.grid(row=10, column=2)

    btn = Button(top1, text="Next", command=window3)
    btn.grid(row=11,column=1)

    status1 = Label(top1, text="page 2 of 3", bd=1, relief=SUNKEN, anchor=E)
    status1.grid(row=12,column=2,)








img= ImageTk.PhotoImage(Image.open("Project directory\Icons\3xhumed-Mega-Games-Pack-38-Prey-logo-1.ico"))
icon = Label(image=img)
icon.grid(row=0,column=0)


label1 = Label(root, text="schedule your complete week")
label2 = Label(root, text="schedule your every day with simple three step process")
frame=LabelFrame(root,text="FIRST STEP",padx=20,pady=20)
label1.grid(row=1,column=0)
label2.grid(row=2, column=0)
frame.grid(row=3,column=0)
day = StringVar()

day.set("Monday")
drop = OptionMenu(frame, day, "Monday", "Tuesday",
                  "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
drop.pack()

button=Button(frame,text="Next",command=window2)
button.pack()


status = Label(root,text="page 1 of 3",bd=2,relief=SUNKEN,anchor=E)
status.grid(row=4,column=0,sticky=W+E)


root.mainloop()
