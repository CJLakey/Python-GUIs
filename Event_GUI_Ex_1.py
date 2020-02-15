from tkinter import * # Import Tkinter
mainbox = Tk() # Create main display box

def hello(): # Create Function for button command
    print ('This will print in the IDE output') # Button command prints text

mainbox.title('Tkinter Widget') # Create title for main box display 
mainbox.geometry('400x200') # Size 400, 200
b1=Button(mainbox, text='Click to initiate event', command=hello)
b1.pack(expand=NO, fill=BOTH)

mainloop()
