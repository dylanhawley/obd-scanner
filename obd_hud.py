from Tkinter import *
import ttk


class OBDCluster:

	def __init__(self, master):
		screen_width = master.winfo_screenwidth()
		screen_height = master.winfo_screenheight()
		
		leftframe = Frame(master)
		leftframe.pack(side=LEFT, padx=.125*screen_width, pady=0.1*screen_height)

		topleftframe = Frame(leftframe)
		topleftframe.pack(side=TOP, pady=.05*screen_height)

		bottomleftframe = Frame(leftframe)
		bottomleftframe.pack(side=BOTTOM, pady=.05*screen_height)

		self.speedLabel = ttk.Label(topleftframe, text="84", font="Arial 20")
		self.speedLabel.pack(side=TOP)

		self.speedUnitsLabel = ttk.Label(topleftframe, text="MPH")
		self.speedUnitsLabel.pack(side=BOTTOM)

		self.RPMLabel = ttk.Label(bottomleftframe, text="3400", font="Arial 20")
		self.RPMLabel.pack(side=TOP)

		self.RPMUnitsLabel = ttk.Label(bottomleftframe, text="RPM")
		self.RPMUnitsLabel.pack(side=BOTTOM)

		# self.printButton = Button(frame, text="70 Print Message", command=self.printMessage, font = "Helvetica 20")
		# #self.printButton.tk_setPalette(background='#40E0D0', foreground='black', activeBackground='black', activeForeground="green")
		# self.printButton.pack(side=LEFT)

		# self.testButton = Button(frame, text="70 Test Message", command=self.printMessage, font = "Arial 20")
		# self.testButton.pack(side=LEFT)

		# photo = PhotoImage(file='m2.gif')
		# self.label = Label(root, image=photo)
		# self.label.pack(side=LEFT)

		# canvas = Canvas(root, width = 200, height = 200)
		# canvas.pack()
		# canvas.create_image(0, 0, anchor=SE, image=photo)

	def printMessage(self):
		print("function printMessage called...")

root = Tk()
obd = OBDCluster(root)
root.mainloop()

# from Tkinter import *

# root = Tk()
# root.attributes('-fullscreen', True)
# root.configure(background='white')

# def close(event):
# 	print("closing window...")
# 	exit()

# root.bind("<Escape>", close)

# mlogo = PhotoImage(file="m2.gif")

# # lbl_mlogo = Label(root, image = img_mlogo)
# # lbl_mlogo.pack()
# canvas = Canvas(root, width = 200, height = 150)
# canvas.pack()
# canvas.create_image(0, 0, anchor = SE, image = mlogo)

# root.mainloop()

# class Example(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)

#         label = tk.Label(self, text="Example of using place")
#         label.pack(side="top", fill="both", expand=True)

#         self.image = tk.PhotoImage(file = "m2.gif")

#         self.nw = tk.Label(self, image=self.image)
#         self.ne = tk.Label(self, image=self.image)
#         self.sw = tk.Label(self, image=self.image)
#         self.se = tk.Label(self, image=self.image)

#         self.nw.place(relx=0.0, rely=0.0, anchor="nw")
#         self.ne.place(relx=1.0, rely=0.0, anchor="ne")
#         self.sw.place(relx=0.0, rely=1.0, anchor="sw")
#         self.se.place(relx=1.0, rely=1.0, anchor="se")

# if __name__ == "__main__":
#     root = tk.Tk()
# 	root.attributes('-fullscreen', True)
#     # root.wm_geometry("400x400")
#     Example(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()