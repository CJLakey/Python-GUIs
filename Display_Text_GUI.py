from tkinter import * # Import Tkinter
import tkinter.messagebox as box # Import Messagebox for displaying text
window = Tk() # Create main window
window.title( 'Entry Widget' ) # Create window title
frame = Frame( window ) # Set frame variable to equal Frame(window)
entry = Entry( frame ) # Set entry variable to equal Entry(frame)
def dialog():  # Create button command function
    box.showinfo( 'Display Text' , 'You entered, ' + entry.get()) # show pop up window with what was entered into box. 
b1=Button(frame , text = 'Enter Your text here.', command = dialog ) # Create button and with entry box.
b1.pack( side = RIGHT , padx = 6 ) # Place Button and entry box into main window
entry.pack( side = LEFT )
frame.pack( padx = 50 , pady = 50 )
mainloop()