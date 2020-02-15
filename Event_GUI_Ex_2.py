from tkinter import * #Import TKinter
import tkinter.messagebox as newwin # Import Tkinter messagebox to display button event output
window = Tk() # Create main display winmdow
window.title('Unit 5 Submission 2') # Title main window
window.geometry('800x400') # Set main window size

def d1(): # Create function for button event
    mbox = newwin.askyesno('Look, a new window appears!', 'Continue?') # Create message box that appears after button is clicked
    if mbox == 1: # If steatment when yes is clicked display info window with text
        newwin.showinfo('Yes','Great Choice!')
    else: # If no is clicked show a warning box with text
        newwin.showwarning('No','Goodbye')
    display.pack() # Pack text in message windows.

btn_end = Button(window,text='Exit', command = window.quit) # Create button to exit program
btn_clickhere = Button(window,text='Click Here for a new window.', command=d1) #Create button to initiate event
btn_end.pack(padx = 140 , pady = 30 ) # Position exit button in window
btn_clickhere.pack(padx = 100, pady = 40) # Position event button in window
mainloop() # Loop program to keep it open
