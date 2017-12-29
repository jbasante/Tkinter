from tkinter import *


#create a main class that inhetits tkinter
class MainMenu(Tk):

    def __init__(self):
        Tk.__init__(self)

        container = Frame(self)
        container.grid(row=2, column=0)

        self.frames = {}
        self.frameNamesNValues = {Amount: 1, Interest: 2}

        #create a frame for the description of gui and buttons to press
        constantFrame = Frame(self)
        constantFrame.grid(row=0, column=0, sticky="w")

        headerLabel = Label(constantFrame, text="Compound Interest Calculator", anchor="w")
        headerLabel.grid(row=0, column=0)

        interestButton = Button(constantFrame, text="Interest", command=lambda: self.show_frame(Interest))
        interestButton.grid(row=1, column=0)

        amountButton = Button(constantFrame, text="Amount", command=lambda: self.show_frame(Amount))
        amountButton.grid(row=1, column=1)

        exitButton = Button(constantFrame, text="Exit", command=quit)
        exitButton.grid(row=1, column=7, padx=50, pady=3)

        # store the frame for each computation (created as a class) to be made in a dictionary
        frame = Amount(self, container, self.frameNamesNValues[Amount])
        self.frames[Amount] = frame
        frame.grid(row=3, column=0, sticky="nsew")

        frame = Interest(self, container, self.frameNamesNValues[Interest])
        self.frames[Interest] = frame
        frame.grid(row=3, column=0, sticky="nsew")

        self.show_frame(Interest)

    #function to show a particular frame
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class Amount(Frame):

    def __init__(self, master, controller, controlValue):
        Frame.__init__(self, master)
        self.controlValue = controlValue #will be used to check if amount or interest is to be calculated
        self.scaleValue = DoubleVar()
        self.principalValue = DoubleVar()
        self.nValue = StringVar()
        self.tValue = IntVar()
        self.tString = IntVar()
        self.totalAmount = DoubleVar()
        self.nValue.set("Daily")  # set default value for drop down menu
        self.tOptions = {"Daily": 365, "Weekly": 52, "Monthly":12, "Quarterly": 4, "Semi-Anual": 2, "Anual": 1}

        if self.controlValue == 1:
            description = Label(self, text="Total Amount Calculator")
            description.grid(row=3, column=1, sticky="E", padx=5, pady=5)
        else:
            description = Label(self, text="Interest Calculator")
            description.grid(row=3, column=1, sticky="E", padx=5, pady=5)

        principalLabel = Label(self, text="Principal $")
        principalLabel.grid(row=4, column=1, sticky=E, padx=5, pady=5)
        principalEntry = Entry(self, textvariable=self.principalValue)
        principalEntry.grid(row=4, column=2, padx=5, pady=5)

        tLabel = Label(self, text="Time in years (t)")
        tLabel.grid(row=5, column=1, sticky=E)
        tEntry = Entry(self, textvariable=self.tValue)
        tEntry.grid(row=5, column=2, padx=5, pady=5)

        nLabel = Label(self, text="Compound Interval (n)")
        nLabel.grid(row=6, column=1, sticky=E)
        nOptions = OptionMenu(self, self.nValue, *self.tOptions)
        nOptions.grid(row=6, column=2, padx=5, pady=5)

        rateLabel = Label(self, text="Interest Rate(%)")
        rateLabel.grid(row=7, column=1, sticky=E, padx=5, pady=5)
        rateScale = Scale(self, from_=0, to=100, resolution=0.05, orient="horizontal",
                          variable=self.scaleValue)  # note: scale uses variable to store the scale value in a variable
        rateScale.grid(row=7, column=2, columnspan=3, padx=5, pady=5)

        calculateButton = Button(self, text="Calculate", command=self.calculateInterest)
        calculateButton.grid(row=9, column=2, columnspan=2, padx=10, pady=10)

        if self.controlValue == 1:
            resultLabel = Label(self, text="Total Amount")
            resultLabel.grid(row=10, column=1, sticky=E)
        else:
            resultLabel = Label(self, text="Interest")
            resultLabel.grid(row=10, column=1, sticky=E)

        resultLabel1 = Label(self, textvariable=self.totalAmount)
        resultLabel1.grid(row=10, column=2)

    def calculateInterest(self):
        principal = self.principalValue.get()
        interest_rate = self.scaleValue.get()
        t = self.tValue.get()
        interval = self.tOptions[self.nValue.get()]
        nt = t*interval
        rate_over_interval = interest_rate/(interval*100)
        if self.controlValue == 1:
            finalValue = principal*((1+rate_over_interval)**nt)
        else:
           finalValue = (principal * ((1 + rate_over_interval) ** nt)) - principal
        self.totalAmount.set(finalValue)


#Create the class (frame) for calculating the interest
class Interest(Amount):
    pass


app = MainMenu()
app.geometry("330x320+0+0")
app.title("Compund Interest Calculator")
app.resizable(0,0) #will cause window not to be expandable
app.mainloop()