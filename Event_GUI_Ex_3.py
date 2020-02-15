from tkinter import * # Import Tkinter
import tkinter.messagebox as box # Import message box for second display box 
window = Tk() # Create main Window
window.title( 'Unit 5 Listbox' ) # Title main window
frame = Frame( window ) # set frame variable to equal Frame(window)
label = Label(window, text = 'What are you going to eat today?') # Create label
label.pack(padx = 5, pady = 5) # Position label
listbox = Listbox( frame ) # Add list box to main window
listbox.insert( 1, 'Tacos' ) # Listbox choice 1
listbox.insert( 2, 'Spaghetti' ) # List Box choioce 2
listbox.insert( 3, 'Cheeseburger' ) # Listbox choice 3
listbox.insert( 4, 'Salad' ) # List Box choice 4
def dialog() :   # Create button function to initiate event
    box.showinfo( 'Selection Made' , 'Your Choice: ' + \
    listbox.get( listbox.curselection() ) ) # Display second display box when event intiated, Second display box shows selection made with list box.
btn = Button( frame, text = 'Choose', command=dialog )  # Create button to start event
btn.pack( side = RIGHT , padx = 6 )  # Position Button
listbox.pack( side = LEFT )  # Position Listbox
frame.pack( padx = 60, pady = 60 ) # Position frame
mainloop()