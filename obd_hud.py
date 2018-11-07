#import matplotlib.pyplot as plt
import Tkinter as tk
import ttk
import obd
import time


class OBDCluster:

	def __init__(self, master):
		speed = connection.query(obd.commands.RPM)
		rpm = connection.query(obd.commands.SPEED)
		efficient_speed = 45

		# speed_vector = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75]
		# eff_vector = [12,14,20.3,26.2,27.3,28.7,29.4,30.1,30.9,31.3,32.1,29.9,26.6,24.8,23.5]

		# plt.plot(speed_vector, eff_vector)
		# plt.xlabel("speed")
		# plt.ylabel("mpg")
		# plt.savefig("figureOBD.png", format="png")

		root.update()
		screen_width = master.winfo_screenwidth()
		screen_height = master.winfo_screenheight()

		def close(event):
			exit()

		root.bind("<Escape>", close)
		
		leftframe = tk.Frame(master)
		leftframe.pack(side=tk.LEFT)
		leftframe.configure(background="#d0d0d4")

		topleftframe = tk.Frame(leftframe)
		topleftframe.pack(side=tk.TOP, padx=.05*screen_width, pady=0.1*screen_height)
		topleftframe.configure(background="#d0d0d4")

		bottomleftframe = tk.Frame(leftframe)
		bottomleftframe.pack(side=tk.BOTTOM, padx=.05*screen_width, pady=.1*screen_height)
		bottomleftframe.configure(background="#d0d0d4")

		self.speedLabel = ttk.Label(topleftframe, text=speed, font="Arial 90", background="#d0d0d4")
		self.speedLabel.pack(side=tk.TOP)

		self.speedUnitsLabel = ttk.Label(topleftframe, text="MPH", font="Arial 15", background="#d0d0d4")
		self.speedUnitsLabel.pack(side=tk.BOTTOM)

		self.RPMLabel = ttk.Label(bottomleftframe, text=rpm, font="Arial 50", background="#d0d0d4")
		self.RPMLabel.pack(side=tk.TOP)

		self.RPMUnitsLabel = ttk.Label(bottomleftframe, text="RPM", font="Arial 15", background="#d0d0d4")
		self.RPMUnitsLabel.pack(side=tk.BOTTOM)

		midframe = tk.Frame(master)
		midframe.pack(side=tk.LEFT)
		midframe.configure(background="#d0d0d4")

		topmidframe = tk.Frame(midframe)
		topmidframe.pack(side=tk.TOP, padx=0.1*screen_width, pady=.1*screen_height)
		topmidframe.configure(background="#d0d0d4")

		bottommidframe = tk.Frame(midframe)
		bottommidframe.pack(side=tk.BOTTOM, padx=0.1*screen_width, pady=.1*screen_height)
		bottommidframe.configure(background="#d0d0d4")

		self.titleLabel = ttk.Label(topmidframe, text="Fuel Economy", font="Arial 40", background="#d0d0d4")
		self.titleLabel.pack(side=tk.TOP)

		# self.img = ImageTk.PhotoImage(Image.open("figureOBD.png"))
		# self.panel = tk.Label(root, image = img)
		# self.panel.pack(side = "bottom", fill = "both", expand = "yes")
		
		def recordData():
			print("button clicked..")

		rightframe = tk.Frame(master)
		rightframe.pack(expand=tk.YES, fill=tk.BOTH)
		rightframe.configure(background="#dee0e4")

		toprightframe = tk.Frame(rightframe)
		toprightframe.pack(side=tk.TOP, padx=6, pady=65)
		toprightframe.configure(background="#dee0e4")

		bottomrightframe = tk.Frame(rightframe)
		bottomrightframe.pack(side=tk.BOTTOM, padx=.04*screen_width, pady=.1*screen_height)
		bottomrightframe.configure(background="#dee0e4")

		self.message = tk.Message(toprightframe, text="Capture fuel consuption data at a constant speed", font="Arial 13", background="#dee0e4", width="300")
		self.message.pack(side=tk.TOP, padx=5, pady=25)
		
		self.recordButton = ttk.Button(toprightframe, text="Cruise", command=recordData())
		self.recordButton.pack(side=tk.BOTTOM)

		self.efficiencyLabel = ttk.Label(bottomrightframe, text="Most Fuel Efficient Speed", font="Arial 13", background="#dee0e4")
		self.efficiencyLabel.pack(side=tk.TOP)

		self.bestSpeedLabel = ttk.Label(bottomrightframe, text=efficient_speed, font="Arial 60", background="#dee0e4")
		self.bestSpeedLabel.pack(side=tk.TOP)

		self.bestSpeedUnitsLabel = ttk.Label(bottomrightframe, text="MPH", font="Arial 15", background="#dee0e4")
		self.bestSpeedUnitsLabel.pack(side=tk.BOTTOM)


connection = obd.Async(fast=False)

connection.watch(obd.commands.RPM)
connection.watch(obd.commands.SPEED)
connection.start()

connection.stop()

root = tk.Tk()
obd = OBDCluster(root)
root.configure(background="#d0d0d4")
root.attributes('-fullscreen', True)
root.mainloop()