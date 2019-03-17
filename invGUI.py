# Team: Vijay Balaji, Jacob Ryan, Pierce McKelvey
# Inventory

import tkinter

class invGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title("Inventory Manager")

        #Frames
        self.title_frame = tkinter.Frame()     # Title
        self.input_frame = tkinter.Frame()        
        self.but1_frame = tkinter.Frame()
        self.but2_frame = tkinter.Frame()
        self.but3_frame = tkinter.Frame()        
        self.bottom_frame = tkinter.Frame()


        #TitleLabel
        self.titleLabel = tkinter.Label(self.title_frame,
                                                text="Inventory Manager",
                                                bg='blue',
                                                fg='white',
                                                font=('Impact', 36))
        #pack
        self.titleLabel.pack()

        # widgets for top frame
        self.temp_prompt_label = tkinter.Label(self.input_frame,
                                          text="Enter in format item name, quantity")
        self.temp_entry = tkinter.Entry(self.input_frame,
                                        width=20)
        # pack top frame
        self.temp_prompt_label.pack(side="left")
        self.temp_entry.pack(side="left")

        self.value = tkinter.StringVar()
        
        # but 1
        self.button1 = tkinter.Button(self.but1_frame,
                                     text="Add to Inventory",
                                     command=self.add)
        
        # pack but1
        self.button1.pack()

        # but 2
        self.button2 = tkinter.Button(self.but2_frame,
                                     text="Delete from Inventory",
                                     command=self.remove)

        # pack but 2
        self.button2.pack()

        # but 3
        self.button3 = tkinter.Button(self.but3_frame,
                                     text="Show Inventory",
                                     command=self.display)
        # pack but 3
        self.button3.pack()

        # widgets for bottom frame
        # set the output variable
        self.value = tkinter.StringVar()
        # set the
        self.output = tkinter.Label(self.bottom_frame,
                                      textvariable=self.value)
        # pack bottom frame
        self.output.pack()

        # pack all of the frame
        self.title_frame.pack()
        self.input_frame.pack()
        self.but1_frame.pack()
        self.but2_frame.pack()
        self.but3_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
        

    def add(self):
        yeet = self.temp_entry.get()
        yeet = str(yeet)
        yeet= yeet.split(', ')
        print(yeet)
        thing = yeet[0]
        amount = int(yeet[1])
        if thing in dck:
           dck[thing] += amount
        else:
           dck[thing] = amount
        output = '{} {} ADDED'.format(amount, thing)

        self.value.set(output)


    def remove(self):  # We could either remove all or just one.
        yeet = self.temp_entry.get()
        yeet = str(yeet)
        yeet = yeet.split(',')
        print(yeet)
        thing = yeet[0]
        amountRemoved = int(yeet[1])

        if amountRemoved == dck[thing]:
           del dck[thing]
        else:
           dck[thing] -= amountRemoved
        output = '{} {} REMOVED'.format(amountRemoved, thing)
        self.value.set(output)


   
    def display(self):
        output = str(dck)
        self.value.set(output)

    
dck = {}
invGUI()
