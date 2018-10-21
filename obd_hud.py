from Tkinter import *
import ttk
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure
# import matplotlib.pyplot


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

		# self.canvas = Canvas(bottommidframe, width=430, height=400)
		# self.canvas.pack()

		# f = pyplot(figsize=(5,5), dpi=100)
		# f.plot([1,2,3],[1,3,5])
		# f.xlabel("sp")
		# f.ylabel("mpg")
        # a = f.add_subplot(111)
        # a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        # self.canvas = FigureCanvasTkAgg(f, bottommidframe)
        # self.canvas.show()
        # self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        # self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
		
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

		self.message = Message(toprightframe, text="Capture fuel consuption data at a constant speed", font="Arial 13", background="#dee0e4", width="300")
		self.message.pack(side=TOP, padx=5, pady=25)
		
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