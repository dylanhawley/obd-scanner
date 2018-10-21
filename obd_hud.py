from Tkinter import *
import ttk
import matplotlib as mpl
import numpy as np
import sys
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

def draw_figure(canvas, figure, loc=(0, 0)):
	figure_canvas_agg = FigureCanvasAgg(figure)
	figure_canvas_agg.draw()
	figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
	figure_w, figure_h = int(figure_w), int(figure_h)
	photo = PhotoImage(master=canvas, width=figure_w, height=figure_h)

	# Position: convert from top-left anchor to center anchor
	canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

	# Unfortunately, there's no accessor for the pointer to the native renderer
	tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

	# Return a handle which contains a reference to the photo object
	# which must be kept live or else the picture disappears
	return photo

class OBDCluster:

	def __init__(self, master):
		speed = 85;
		rpm = 3200;
		efficient_speed = 54;

		root.update()
		screen_width = master.winfo_screenwidth()
		screen_height = master.winfo_screenheight()

		def close(event):
			exit()

		root.bind("<Escape>", close)
		
		leftframe = Frame(master)
		leftframe.pack(side=LEFT)
		leftframe.configure(background="#d0d0d4")

		topleftframe = Frame(leftframe)
		topleftframe.pack(side=TOP, padx=.05*screen_width, pady=0.1*screen_height)
		topleftframe.configure(background="#d0d0d4")

		bottomleftframe = Frame(leftframe)
		bottomleftframe.pack(side=BOTTOM, padx=.05*screen_width, pady=.1*screen_height)
		bottomleftframe.configure(background="#d0d0d4")

		self.speedLabel = ttk.Label(topleftframe, text=speed, font="Arial 90", background="#d0d0d4")
		self.speedLabel.pack(side=TOP)

		self.speedUnitsLabel = ttk.Label(topleftframe, text="MPH", font="Arial 15", background="#d0d0d4")
		self.speedUnitsLabel.pack(side=BOTTOM)

		self.RPMLabel = ttk.Label(bottomleftframe, text=rpm, font="Arial 50", background="#d0d0d4")
		self.RPMLabel.pack(side=TOP)

		self.RPMUnitsLabel = ttk.Label(bottomleftframe, text="RPM", font="Arial 15", background="#d0d0d4")
		self.RPMUnitsLabel.pack(side=BOTTOM)

		midframe = Frame(master)
		midframe.pack(side=LEFT)
		midframe.configure(background="#d0d0d4")

		topmidframe = Frame(midframe)
		topmidframe.pack(side=TOP, padx=0.1*screen_width, pady=.1*screen_height)
		topmidframe.configure(background="#d0d0d4")

		bottommidframe = Frame(midframe)
		bottommidframe.pack(side=BOTTOM, padx=0.1*screen_width, pady=.1*screen_height)
		bottommidframe.configure(background="#d0d0d4")

		self.titleLabel = ttk.Label(topmidframe, text="Fuel Economy", font="Arial 40", background="#d0d0d4")
		self.titleLabel.pack(side=TOP)

		self.canvas = Canvas(bottommidframe, width=430, height=400)
		self.canvas.pack()

		X = np.linspace(0, 2 * np.pi, 50)
		Y = np.sin(X)

		# Create the figure we desire to add to an existing canvas
		fig = mpl.figure.Figure(figsize=(2, 1))
		ax = fig.add_axes([0, 0, 1, 1])
		ax.plot(X, Y)

		# Keep this handle alive, or else figure will disappear
		fig_x, fig_y = 100, 100
		fig_photo = draw_figure(self.canvas, fig, loc=(fig_x, fig_y))
		fig_w, fig_h = fig_photo.width(), fig_photo.height()

		# Add more elements to the canvas, potentially on top of the figure
		self.canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
		self.canvas.create_text(200, 50, text="Zero-crossing", anchor="s")

		def recordData():
			print("button clicked..")

		rightframe = Frame(master)
		rightframe.pack(expand=YES, fill=BOTH)
		rightframe.configure(background="#dee0e4")

		toprightframe = Frame(rightframe)
		toprightframe.pack(side=TOP, padx=6, pady=65)
		toprightframe.configure(background="#dee0e4")

		bottomrightframe = Frame(rightframe)
		bottomrightframe.pack(side=BOTTOM, padx=.04*screen_width, pady=.1*screen_height)
		bottomrightframe.configure(background="#dee0e4")

		# w = Canvas(toprightframe, width = screen_width, height=20, bg="#dee0e4")
		# w.pack(expand=YES, fill=X)

		# root.update()
		# w.create_line(10, 150, w.winfo_width()-10, 150, fill="#7a7a7a", width=3)

		self.message = Message(toprightframe, text="Capture fuel consuption data at a constant speed", font="Arial 13", background="#dee0e4", width="300")
		self.message.pack(side=TOP, padx=5, pady=35)

		# style = ttk.Style()
		# style.configure("S.TButton", foreground="#6e6e6e", background="white")
		
		self.recordButton = ttk.Button(toprightframe, text="Cruise", command=recordData())
		self.recordButton.pack(side=BOTTOM)

		self.efficiencyLabel = ttk.Label(bottomrightframe, text="Most Fuel Efficient Speed", font="Arial 13", background="#dee0e4")
		self.efficiencyLabel.pack(side=TOP)

		self.bestSpeedLabel = ttk.Label(bottomrightframe, text=efficient_speed, font="Arial 60", background="#dee0e4")
		self.bestSpeedLabel.pack(side=TOP)

		self.bestSpeedUnitsLabel = ttk.Label(bottomrightframe, text="MPH", font="Arial 15", background="#dee0e4")
		self.bestSpeedUnitsLabel.pack(side=BOTTOM)


root = Tk()
obd = OBDCluster(root)
root.configure(background="#d0d0d4")
root.attributes('-fullscreen', True)
root.mainloop()