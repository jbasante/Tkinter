from tkinter import *

class Amount():

    # declare variables
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        self.scaleValue = DoubleVar()
        self.principalValue = DoubleVar()
        self.nValue = StringVar()
        self.tValue = IntVar()
        self.tString = IntVar()
        self.totalAmount = DoubleVar()
        self.tOptions = ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Semi-Anual', 'Anual']
        self.nValue.set('Daily')  # set default value for drop down menu

        headerLabel = Label(frame, text="Compound Interest Calculator")
        headerLabel.grid(row=1, column=1)

        amountButton = Button(frame, text="Amount")
        amountButton.grid(row=2, column=1, padx=3, pady=3)

        interestButton = Button(frame, text="Interest")
        interestButton.grid(row=2, column=2, padx=3, pady=3)

        principalLabel = Label(frame, text="Principal $")
        principalLabel.grid(row=3, column=1, sticky=E, padx=5, pady=5)
        principalEntry = Entry(frame, textvariable=self.principalValue)
        principalEntry.grid(row=3, column=2, padx=5, pady=5)

        tLabel = Label(frame, text="Time in years (t)")
        tLabel.grid(row=4, column=1, sticky=E)
        tEntry = Entry(frame, textvariable=self.tValue)
        tEntry.grid(row=4, column=2, padx=5, pady=5)

        nLabel = Label(frame, text="Compound Interval (n)")
        nLabel.grid(row=5, column=1, sticky=E)
        nOptions = OptionMenu(frame, self.nValue, *self.tOptions)
        nOptions.grid(row=5, column=2, padx=5, pady=5)

        rateLabel = Label(frame, text="Interest Rate(%)")
        rateLabel.grid(row=6, column=1, sticky=E, padx=5, pady=5)
        rateScale = Scale(frame, from_=0, to=100, resolution=0.05, orient="horizontal",
                          variable=self.scaleValue)  # note: scale uses variable to store the scale value in a variable
        rateScale.grid(row=6, column=2, columnspan=3, padx=5, pady=5)

        calculateButton = Button(frame, text="Calculate", command=self.calculateInterest)
        calculateButton.grid(row=8, column=2, columnspan=2, padx=10, pady=10)
        # testLabel = Label(root, textvariable=tOptions[str(tValue.get())]) #Use textvariabl to update label value
        # testLabel.grid(row=6, column=2)

        resultLabel = Label(frame, text="Total Amount")
        resultLabel.grid(row=9, column=1, sticky=E)
        resultLabel1 = Label(frame, textvariable=self.totalAmount)
        resultLabel1.grid(row=9, column=2)

    def calculateInterest(self):
        principal = self.principalValue.get()
        interest_rate = self.scaleValue.get()
        t = self.tValue.get()
        interval = 0
        if self.nValue.get() == "Daily":
            interval = 365
        elif self.nValue.get() == "Weekly":
            interval = 52
        elif self.nValue.get() == "Monthly":
            interval = 12
        elif self.nValue.get() == "Quarterly":
            interval = 4
        elif self.nValue.get() == "Semi-Anual":
            interval = 2
        else:
            interval = 1

        nt = t*interval
        rate_over_interval = interest_rate/(interval*100)
        finalValue = principal*((1+rate_over_interval)**nt)
        self.totalAmount.set(finalValue)


root = Tk()
root.geometry("350x300+0+0")
root.title("Compund Interest Calculator")
root.resizable(0,0)
calculateAmount = Amount(root)
root.mainloop()

#to create an executable file, install pyinstaller and run pyinstaller file.py -F -w -i image.ico to get a single exec file with a preferred icon
