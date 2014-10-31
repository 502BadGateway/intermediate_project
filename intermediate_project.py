from Tkinter import *
master = Tk()
arena = Canvas(window, width=100, height=500)
def callback_basic():
    basic()
def callback_intermediate():
	intermdiate() 
def callback_advanced():
	print ("Advanced modual not finshed")
a = Button(master, text="Basic", command=callback_basic)
a.pack()
b = Button(master, text="Intermdiate", command=callback_intermediate)
b.pack()
c = Button(master, text="Advanced", command=callback_advanced)
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

	window.mainloop() # runs the code
def intermdiate():
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