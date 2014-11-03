from Tkinter import *
import time # imports the time moduale
master = Tk()
def callback_basic(): # calls the bacis function when the user clicks the button
    basic()
def callback_intermediate(): # calls the intermidiate function  when user clicks the button 
	intermdiate() 
def callback_advanced():
	print ("Advanced modual not finshed")
a = Button(master, text="Basic", command=callback_basic) # creates a button that will take the user to the basic task
a.pack()
b = Button(master, text="Intermdiate", command=callback_intermediate) #  creates a button that will take the user to the intermidiate task
b.pack()
c = Button(master, text="Advanced", command=callback_advanced) # creates a button that willl take the user to the adanced task
c.pack()
def basic():
	window = Tk() # generates a window 
	arena = Canvas(window, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena
	arena.pack()
	key = Canvas(window, width = 500, height = 100, bg = 'grey') # generates a canvas for our key and UI area
	key.pack()

	obstacle_rectangle1 = arena.create_rectangle(350, 50, 400, 200, fill = "red") # creates a obstacle to avoid
	obstacle_rectangle2 = arena.create_rectangle(150, 200, 300, 250, fill = "red")
	obstacle_rectangle3 = arena.create_rectangle(400, 250, 500, 300, fill = "red")
	obstacle_rectangle4 = arena.create_rectangle(0, 350, 250, 400, fill = "red")
	obstacle_rectangle5 = arena.create_rectangle(400, 350, 450, 400, fill = "red")
	obstacle_rectangle6 = arena.create_rectangle(0, 0, 100, 200, fill = "red")
	start_area = arena.create_rectangle(0, 450, 50, 500, fill = "#00FF99") # uses a Hexidecimal code for light green

	#flag gif
	gif1 = PhotoImage(file = 'flag.gif')
	arena.create_image(500, 0, image = gif1, anchor = NE,)
	#create triangle robot

	robot = arena.create_polygon([(10, 450), (10, 500), (40, 475)], fill="#366605")
	arena.pack()
	arena.update_idletasks()

	for t in range(0,450): # moves the robot right 450 pixals 
		arena.move(robot , 1 , 0)
    	arena.update()
    	time.sleep(0.1)

	window.mainloop() # runs everything


def intermdiate():
	print ("this is a test")
	window = Tk() # generates a window 
	arena = Canvas(window, width = 500, height = 500, bg = 'white') # generates a canvas of 500px x 500px for the arena
	arena.pack()
	key = Canvas(window, width = 500, height = 100, bg = 'grey') # generates a canvas for our key and UI area
	key.pack()

	obstacle_rectangle1 = arena.create_rectangle(350, 50, 400, 200, fill = "red") # creates a obstacle to avoid
	obstacle_rectangle2 = arena.create_rectangle(150, 200, 300, 250, fill = "red")
	obstacle_rectangle3 = arena.create_rectangle(400, 250, 500, 300, fill = "red")
	obstacle_rectangle4 = arena.create_rectangle(0, 350, 250, 400, fill = "red")
	obstacle_rectangle5 = arena.create_rectangle(400, 350, 450, 400, fill = "red")
	obstacle_rectangle6 = arena.create_rectangle(0, 0, 100, 200, fill = "red")
	start_area = arena.create_rectangle(0, 450, 50, 500, fill = "#00FF99") # uses a Hexidecimal code for light green

	window.mainloop() # runs the code
mainloop()