import tkinter as tk
#JENELYN LANG SAKALAM
from tkinter import *
from PIL import ImageTk, Image
import os
import os.path
import datetime
from tkcalendar import Calendar

#Title Bar
storage = Tk()
storage.geometry("1285x651")
storage.title("Student's Savings Tracker")
storage.iconbitmap("Student's_Savings_Tracker.ico")

#Boss Jc Jamela lang malakas

def endWindow():

    frameForThirdFrame.place_forget()
    a=""
    for i in files[1:2]:
        if i.isdigit():
            a = a + i

    if currentNumber < int(a):
        lastFrame = Frame(storage, bg='gold', relief=RIDGE, bd=15)
        lastFrame.place(x=150, y=25, width=1000, height=600)

        lastPart = Label(lastFrame, text="Keep it up! \n Your current savings for today is:",
                         font=('arial', 28, 'bold'), bg="gold")
        lastPart.place(x=200, y=20)
        number = Label(lastFrame, text=currentNumber, fg="red",
                    font=('arial', 60, 'bold'), bg="gold")
        number.place(x=400, y=150)

        class Students:

            def __init__(self):
                self.__updateSoftware()

            def drive(self):
                print('Exit Program')

            def __updateSoftware(self):
                print("")

        working = Students()
        working.drive()
    else:
        lastFrame = Frame(storage, bg='gold', relief=RIDGE, bd=15)
        lastFrame.place(x=150, y=25, width=1000, height=600)

        lastPart = Label(lastFrame, text="Congratulations!\nYou have reached:",
                         font=('arial', 28, 'bold'), bg="gold")
        lastPart.place(x=360, y=20)
        number = Label(lastFrame, text=currentNumber, fg="red",
                       font=('arial', 60, 'bold'), bg="gold")
        number.place(x=400, y=150)
        file.close()
        file2.close()
        os.remove("Student_Savings.txt")

        class Students:

            def __init__(self):
                self.__updateSoftware()

            def drive(self):
                print('Exit Program')

            def __updateSoftware(self):
                print("")

        working = Students()
        working.drive()

def exitWindow():
    global currentNumber
    global file2
    file2 = open("Student_Savings.txt","a")
    a = ""
    for m in files[-1:]:
        if m.isdigit():
            a = a + m
    b = ""
    for m in files[2:3]:
        if m.isdigit():
            b = b + m
    if a == "":
        currentNumber = eval(b + a)
        file2.write("\n" + str(currentNumber))
        endWindow()
    else:
        currentNumber = int(b) + int(a)
        file2.write("\n" + str(currentNumber))
        endWindow()

def lastWindow():
    global frameForThirdFrame
    frameForThirdFrame = Frame(storage, bg='gold', relief=RIDGE, bd=15)
    frameForThirdFrame.place(x=150, y=25, width=1000, height=600)
    targetDate = files[3:4]
    lastPart = Label(frameForThirdFrame, text="Estimated Date to Complete Goal:\nyyyy-mm-dd",
                     font=('arial', 25), bg="gold")
    lastPart.place(x=230, y=20)
    etd = Label(frameForThirdFrame, text=targetDate,
                font=('arial', 30, 'bold'), bg="gold")
    etd.place(x=370, y=100)
    current = "Current Amount:"
    currentAmount = Label(frameForThirdFrame, text=current, font=('arial', 25), bg="gold")
    currentAmount.place(x=200, y=190)
    currentAmountNumber = Label(frameForThirdFrame, text=files[-1:], font=('arial', 25), bg="gold")
    currentAmountNumber.place(x=500, y=190)
    goalAm = "Goal Amount:"
    goalAmount = Label(frameForThirdFrame, text=goalAm, font=('arial', 25), bg="gold")
    goalAmount.place(x=200, y=250)
    goalAmountNumber = Label(frameForThirdFrame, text=files[1:2], font=('arial', 25), bg="gold")
    goalAmountNumber.place(x=420, y=250)
    moneyToday = f"I have inserted {files[2:3]} pesos today"
    lastButton = Button(frameForThirdFrame, text=moneyToday, font='arial 20 bold', bg='red',
                        fg='white', command=exitWindow, relief=RAISED)
    lastButton.place(x=260, y=350)

def checkAmountPerDay():
    apd = containsAmountPerDay.get()
    if apd.isspace() or len(apd) == 0:
        storage.bell()
        notification = Label(anotherFrame, text="      Invalid input. This area can't be blank.                 ",
                             font=('arial', 20), bg="gold", fg="red")
        notification.place(x=200, y=500)
        return
    elif apd == "00000" or apd == "0000" or apd == "000" or apd == "00" or apd == "0":
        storage.bell()
        notification = Label(anotherFrame, text="      Invalid input. Please input number/s higher than 0.               ",
                             font=('arial', 20), bg="gold", fg="red")
        notification.place(x=200, y=500)
        return
    elif containsAmountPerDay.get().isdigit():
        if int(containsAmountPerDay.get()) > (int(setMoneyGoal.get())/2):
            storage.bell()
            notification = Label(anotherFrame, text="Invalid input. Please input up to 50% of your money goal only.     ",
                                 font=('arial', 20), bg="gold", fg="red")
            notification.place(x=150, y=500)
            return
        else:
            file1.write("\n" + containsAmountPerDay.get())
            date = datetime.date.today()
            numberOfDays = int(setMoneyGoal.get()) / int(containsAmountPerDay.get())
            end_date = date + datetime.timedelta(days=int(numberOfDays))
            file1.write("\n" + str(end_date) + "\n 0")
            lastWindow()

    else:
        storage.bell()
        notification = Label(anotherFrame, text="             Invalid input. Please input numbers only.              ",
                             font=('arial', 20), bg="gold", fg="red")
        notification.place(x=150, y=500)



def computeAmount():
    anotherFrame.place_forget()
    frameForThirdFrame = Frame(storage, bg='gold', relief=RIDGE, bd=15)
    frameForThirdFrame.place(x=150, y=25, width=1000, height=600)

    if int(year) >= 1:
        global yearToMonth
        yearToMonth = int(year) * 365
        print(yearToMonth)
    else:
        yearToMonth = 0

    if float(month) >= 1:
        global monthToDays
        monthToDays = int(month) * 30
        print(monthToDays)
    elif float(month) < 0:
        monthToDays = 350 - (int(month) * 30)
    else:
        monthToDays = 0

    computedDays = int(day) + int(monthToDays) + int(yearToMonth)
    amountPerDay = int(setMoneyGoal.get()) / int(computedDays)
    file1.write("\n" + str(int(amountPerDay)))
    end_date = datetime.date.today() + datetime.timedelta(days=int(computedDays))
    file1.write("\n" + str(end_date) + "\n 0")

def target():
    windowFrame.place_forget()
    global anotherFrame
    global containsAmountPerDay
    global selectedDate

    containsAmountPerDay = StringVar()
    anotherFrame = Frame(storage, bg='gold', relief=RIDGE, bd=15)
    anotherFrame.place(x=150, y=25, width=1000, height=600)

    if v0.get() == 1: #target day
        selectDate = tk.Label(anotherFrame, text="Please select your target date.",
                            font=('arial', 25, 'bold'),
                            bg="gold")
        selectDate.place(x=280, y=20)
        today = datetime.date.today()
        # Add Calendar
        cal = Calendar(anotherFrame, selectmode='day',
                       year=today.year, month=today.month,
                       day=today.day,date_pattern="yyyy-mm-dd")
        cal.pack(pady=100)

        def grad_date():
            selectedDate = cal.get_date()
            print(selectedDate)
            selectedYear = selectedDate[0:4]
            currentYear = today.year
            selectedDay = selectedDate[-2:]
            currentDay = today.day
            selectedMonth = selectedDate[5:7]
            currentMonth = today.month

            if int(selectedYear) < currentYear:
                storage.bell()
                wrong = Label(anotherFrame,text="Invalid Input. Enter the correct date.", fg="Red", font="arial 20", bg="gold")
                wrong.place(x=200, y=500)
            else:
                global year
                global day
                global month
                year = int(selectedYear) - int(currentYear)
                day = int(selectedDay) - int(currentDay)
                month = int(selectedMonth) - int(currentMonth)
                print(month, day, year)
                computeAmount()

        # Add Button and Label
        Button(anotherFrame, text="Done", font='arial 20 bold', bg='red',
                         fg='white', relief=RAISED, command=grad_date).pack(pady=10)
    else:
        textQuestion = tk.Label(anotherFrame, text="Please input the target amount per day.",
                              font=('arial', 25, 'bold'),bg="gold")
        textQuestion.place(x=200, y=30)
        amountInput = tk.Entry(storage, font=("times new", 18, 'bold'), relief=FLAT, bd=7,
                                 textvariable=containsAmountPerDay)
        amountInput.place(x=500, y=200)
        goButton = Button(anotherFrame, text='Next', font='arial 20 bold', bg='red',
                            fg='white', command=checkAmountPerDay, relief=RAISED)
        goButton.place(x=600, y=300)

def options():
    texts.pack_forget()
    moneyGoalInput.place_forget()
    OKButton.place_forget()
    myImageLabel.pack_forget()
    moneyGoal.place_forget()
    notification.place_forget()

    global v0

    v0 = IntVar()
    v0.set(1)
    r1 = Radiobutton(windowFrame, text="target date",font='arial 18', bg="gold", variable=v0, value=1)
    r2 = Radiobutton(windowFrame, text="target amount", font='arial 18',bg="gold", variable=v0, value=2)
    r1.place(x=300, y=250)
    r2.place(x=490, y=250)

    question = tk.Label(windowFrame, text="Do you have a target date or \na target amount per day?", font=('arial', 35, 'bold'),
                     bg="gold")
    question.place(x=180, y=100)
    doneButton = Button(windowFrame, text='Next', font='arial 20 bold', bg='red',
                      fg='white', command=target, relief=RAISED)
    doneButton.place(x=600, y=400)

def checkGoal():
    set = setMoneyGoal.get()

    if set.isalpha():
        storage.bell()
        notification.config(text="Invalid input. Please type numbers only.", fg="Red")
        return
    elif set.isspace() or len(set) == 0:
        storage.bell()
        notification.config(text="The area can't be blank.", fg="Red")
        return
    elif int(set) > 10000:
        storage.bell()
        notification.config(text="Invalid input. Please input numbers 1 to 10000 only.", fg="red")
        return
    elif int(len(set)) > 5:
        storage.bell()
        notification.config(text="Invalid input. Please input numbers 1 to 10000 only.", fg="red")
        return
    elif set == "00000" or set == "0000" or set == "000" or set == "00" or set == "0":
        storage.bell()
        notification.config(text="Invalid input. Please input numbers 1 to 10000 only.", fg="Red")
        return
    elif set.isdigit():
        file1.write("\n" + set)
        options()
    else:
        storage.bell()
        notification.config(text="Invalid input. Please type numbers only.\n eg.1000", fg="red")
        return

def byDay():
    #notification.place_forget()
    password.place_forget()
    passwordInput.place_forget()
    confirmPassword.place_forget()
    confirmPasswordInput.place_forget()
    signUp.place_forget()

    global setMoneyGoal
    global moneyGoalInput
    global OKButton
    global moneyGoal
    global files
    global file

    file = open("Student_Savings.txt","r")
    files = file.read()
    files = files.split("\n")

    setMoneyGoal = StringVar()

    moneyGoal = Label(windowFrame, text="Goal", font=('arial', 20), bg="gold")
    moneyGoal.place(x=300, y=310)
    moneyGoalInput = tk.Entry(storage, font=("times new", 18, 'bold'), textvariable=setMoneyGoal,
                                            relief=FLAT, bd=7)
    moneyGoalInput.place(x=600, y=340)
    OKButton = Button(windowFrame, text='OK', font='arial 20 bold', bg='red',
                         fg='white', command=checkGoal, relief=RAISED)
    OKButton.place(x=600, y=400)

def new(): #check if username and password are correct
    global files
    global file
    registeredPassword = logInPassword.get()
    file = open("Student_Savings.txt","r")
    files = file.read()
    files = files.split("\n")
    if registeredPassword in files[:1]:
        notifications = Label(windowFrame, text="Log in successfully!",
                              font=('arial', 20), fg="green", bg="gold")
        notifications.place(x=200, y=450)
        lastWindow()
    else:
        notifications = Label(windowFrame, text="Incorrect Password. \nPlease try again.",
                                font=('arial', 20), fg="red", bg="gold")
        notifications.place(x=200, y=450)
        return

def registered(): #checks password on sign up
    password2 = containsPassword.get()
    passwordConfirmation = containsConfirmPassword.get()
    global file1
    if len(password2)==0: #empty entry
        storage.bell()
        notification.config(fg="red", bg="gold", text="Note: All fields required.")
        return
    elif password2.isspace():
        storage.bell()
        notification.config(fg="red", bg="gold", text="Note: Please input characters.")
        return
    elif len(password2) > 8:
        storage.bell()
        notification.config(fg="red", bg="gold", text="Note: Password should only contain 8 characters.")
        return
    elif password2 == passwordConfirmation:
        file1 = open("Student_Savings.txt","w")
        file1.write(password2)
        notification.config(fg="green", bg="gold", text="Account saved successfully!")
        byDay()
    else: #passwords don't match
        storage.bell()
        notification.config(fg="red", bg="gold",text="Note: Passwords don't match.")
        return

def logIn(): #triggered when log in button was clicked
    logInButton.pack_forget()
    signUpButton.pack_forget()

    global logInPassword
    global notification

    logInPassword = StringVar()
    password = Label(windowFrame, text="Password", font=('arial', 20), bg="gold")
    password.place(x=305, y=370)
    passwordInput = tk.Entry(storage, font=("times new", 18, 'bold'), textvariable=logInPassword,
                                            show="*", relief=FLAT, bd=7)
    passwordInput.place(x=600, y=400)
    logIn = Button(windowFrame, text='Log In', font='arial 20 bold', bg='red', fg='white', command=new,
                    relief=RAISED)
    logIn.place(x=600, y=450)
    #notification if feilds are empty
    notification = Label(windowFrame, font=('arial', 20), bg="gold")
    notification.place(x=300, y=460)

def signUp(): #triggered when sign up button was clicked
    #removes log in and sign up button
    logInButton.pack_forget()
    signUpButton.pack_forget()

    global containsPassword
    global containsConfirmPassword
    global notification
    global password
    global passwordInput
    global confirmPassword
    global confirmPasswordInput
    global signUp

    containsPassword = StringVar()
    containsConfirmPassword = StringVar()
    password = Label(windowFrame, text="Password", font=('arial', 20), bg="gold")
    password.place(x=305, y=360)
    passwordInput = tk.Entry(storage, font=("times new", 18, 'bold'), show="*", relief=FLAT, bd=7, textvariable=containsPassword)
    passwordInput.place(x=600, y=390)
    confirmPassword = Label(windowFrame, text="Confirm Password", font=('arial', 20), bg="gold")
    confirmPassword.place(x=200, y=420)
    confirmPasswordInput = tk.Entry(storage, font=("times new", 18, 'bold'), show="*", relief=FLAT, bd=7,textvariable=containsConfirmPassword)
    confirmPasswordInput.place(x=600, y=450)
    signUp = Button(windowFrame, text='Sign Up', font='arial 20 bold', bg='red', fg='white', command=registered,
                         relief=RAISED)
    signUp.place(x=600, y=480)
    # notification if fields are empty
    notification = Label(windowFrame, font=('arial', 20),bg="gold")
    notification.place(x=200, y=500)

def button(): #sign up and log in buttons
    global logInButton
    global signUpButton
    # log in Button
    logInButton = Button(windowFrame, text='Log In', font='arial 20 bold', bg='red',
                             fg='white',command=logIn, relief=RAISED)
    logInButton.pack()
    # sign up Button
    signUpButton = Button(windowFrame, text='Sign Up', font='arial 20 bold', bg='red',
                              fg='white', command=signUp, relief=RAISED)
    signUpButton.pack()
    if os.path.exists('Student_Savings.txt') == True:
        signUpButton.pack_forget()
    else:
        logInButton.pack_forget()

#Window Frame
bg = ImageTk.PhotoImage(Image.open("moneyBG.jpeg"))
label1 = Label(storage, image=bg)
label1.pack()
windowFrame = Frame(storage, bg='gold', relief=RIDGE, bd=15)
windowFrame.place(x=150, y=20, width=1000, height=600)

#First window design (logo and name)
myImage = ImageTk.PhotoImage(Image.open("Student's_Savings_Tracker.jpg")) #logo
myImageLabel = tk.Label(windowFrame,image=myImage, bg='gold', fg="gold")
myImageLabel.pack()
texts= tk.Label(windowFrame, text="Student's Savings Tracker", font=('arial', 35, 'bold'), bg="gold") #name under logo
texts.pack()
button()


storage.mainloop()
