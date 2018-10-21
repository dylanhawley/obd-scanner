from Tkinter import *
import ttk


class OBDCluster:

	def __init__(self, master):
		screen_width = master.winfo_screenwidth()
		screen_height = master.winfo_screenheight()
		
		leftframe = Frame(master)
		leftframe.pack(side=LEFT)

		topleftframe = Frame(leftframe)
		topleftframe.pack(side=TOP, padx=.1*screen_width, pady=.1*screen_height)

		bottomleftframe = Frame(leftframe)
		bottomleftframe.pack(side=BOTTOM, padx=.1*screen_width, pady=.1*screen_height)

		self.speedLabel = ttk.Label(topleftframe, text="84", font="Arial 100")
		self.speedLabel.pack(side=TOP)

		self.speedUnitsLabel = ttk.Label(topleftframe, text="MPH", font="Arial 15")
		self.speedUnitsLabel.pack(side=BOTTOM)

		self.RPMLabel = ttk.Label(bottomleftframe, text="3400", font="Arial 50")
		self.RPMLabel.pack(side=TOP)

		self.RPMUnitsLabel = ttk.Label(bottomleftframe, text="RPM", font="Arial 15")
		self.RPMUnitsLabel.pack(side=BOTTOM)

root = Tk()
obd = OBDCluster(root)
root.mainloop()