from tkinter import *
from tkinter import messagebox,filedialog

def main():
	import pymsgbox
	root = Tk()

	root.geometry("200x200")
	root.resizable(0,0)
	root.title("Notes")
	root.wm_iconbitmap('notes.ico')

	##################################Function############################

	def new(event=None):
		text.delete(1.0,END)

	def more(event=None):
		return main()	

	def save():
		file = filedialog.asksaveasfile(defaultextension='.txt',
										filetypes=[
											("Text file",".txt")])
		filetext = str(text.get(1.0,END))
		file.write(filetext)
		file.close()

	f = Frame(root, bg="yellow")

	Button(f, text="More", activebackground="yellow", activeforeground="red", bg="yellow", fg="red", font=(20), command=more).pack(side=LEFT, padx=10)
	Button(f, text="New", activebackground="yellow", activeforeground="red", bg="yellow", fg="red", font=(20), command=new).pack(side=LEFT, padx=10)
	Button(f, text="Save", activebackground="yellow", activeforeground="red", bg="yellow", fg="red", font=(20), command=save).pack(side=LEFT, padx=10)

	f.pack(side=TOP)

	text = Text(root, bg="yellow", fg="black", font=("bold", 15))
	text.pack(fill=Y)

	def message():
		a =  pymsgbox.confirm("Do you want to close?","Close")
		if a=="OK":
			print(a)
			root.destroy()

	root.protocol("WM_DELETE_WINDOW",message)

	root.mainloop()

main()
