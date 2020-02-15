from tkinter import * # import Tkinter
import tkinter.messagebox as box # Import messagebox for second display  box
window = Tk() # Create main window
window.title( 'Choose the game you want to play.' ) # Create Window Title
frame = Frame( window ) # Set frame variable as Frame( window )
game = StringVar() # set game variable a stringvar
radio_1 = Radiobutton( frame , text = 'RPG' , variable = game , value = 'You chose an RPG game.' ) # Create radio button 1
radio_2 = Radiobutton( frame , text = 'Fighting' , variable = game , value = 'You chose a fighting game' ) # Create radio button 2
radio_3 = Radiobutton( frame , text = 'Racing' , variable = game , value = 'You chose a Racing game' ) # Create radio button 3
radio_4 = Radiobutton( frame , text = 'Puzzle' , variable = game , value = 'You chose a Puzzle game' ) # Create radio button 4
radio_1.select() # Create selection functionality
def dialog() : # Create button command function
    box.showinfo( 'You Selected' , 'Game Choice: \n' + game.get()) # Button takes your selection and displays it in new window
btn = Button( frame , text = 'Choose a game' , command = dialog ) # Create button
btn.pack( side = RIGHT , padx = 5 ) # Position Button
radio_1.pack( side = LEFT ) # Position radio button 1
radio_2.pack( side = LEFT ) # Position radio button 2
radio_3.pack( side = LEFT ) # Position radio button 3
radio_4.pack( side = LEFT ) # Position radio button 4
frame.pack( padx = 30 , pady = 30 ) #Position frame
mainloop() # Loop main porgram to prevent from closing