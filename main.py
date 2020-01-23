import tkinter as tk
import tkinter.ttk

class Application(tkinter.ttk.Frame):
	"""Simple calculator only two values"""
	def __init__(self, master = None):
		super().__init__(master)

		self.value1 = tk.IntVar(value = 0)
		self.value2 = tk.IntVar(value = 0)
		self.text_in_lbl = tk.StringVar(value="")

		self.pack()
		self.create_widgets()
		self.master.title("Simple calculator on tkinter")
		self.master.geometry("450x150+200+200")


#column столбец row строка
	def create_widgets(self):
		self.entr = tkinter.ttk.Entry(self,textvariable = self.text_in_lbl, width = 52)
		self.entr.grid(row = 0,column = 0, columnspan = 4)

		self.btn1 = tkinter.ttk.Button(self,text = "1", command = self.one)
		self.btn1.grid(row = 1, column = 0)

		self.btn2 = tkinter.ttk.Button(self,text = "2", command = self.two)
		self.btn2.grid(row = 1, column = 1)

		self.btn3 = tkinter.ttk.Button(self,text = "3", command = self.three)
		self.btn3.grid(row = 1, column = 2)

		self.btn4 = tkinter.ttk.Button(self,text = "4", command = self.four)
		self.btn4.grid(row = 2, column = 0)

		self.btn5 = tkinter.ttk.Button(self,text = "5", command = self.five)
		self.btn5.grid(row = 2, column = 1)

		self.btn6 = tkinter.ttk.Button(self,text = "6", command = self.six)
		self.btn6.grid(row = 2, column = 2)

		self.btn7 = tkinter.ttk.Button(self,text = "7", command = self.seven)
		self.btn7.grid(row = 3, column = 0 )

		self.btn8 = tkinter.ttk.Button(self,text = "8", command = self.eigth)
		self.btn8.grid(row = 3, column = 1)

		self.btn9 = tkinter.ttk.Button(self,text = "9", command = self.nine)
		self.btn9.grid(row = 3, column = 2)

		self.btn0 = tkinter.ttk.Button(self,text = "0", command = self.zero)
		self.btn0.grid(row = 4, column = 1)

		self.btn_plus = tkinter.ttk.Button(self,text = "+", command = self.plus)
		self.btn_plus.grid(row = 1, column = 3)

		self.btn_minus = tkinter.ttk.Button(self,text = "-", command = self.minus)
		self.btn_minus.grid(row = 2, column = 3)

		self.btn_multiply = tkinter.ttk.Button(self,text = "*", command = self.multiply)
		self.btn_multiply.grid(row = 3, column = 3)

		self.btn_devide = tkinter.ttk.Button(self,text = "/", command = self.devide)
		self.btn_devide.grid(row = 4, column = 3)

		self.btn_result = tkinter.ttk.Button(self, text = "=", command = self.result)
		self.btn_result.grid(row = 4, column = 2)

		self.btn_dot = tkinter.ttk.Button(self, text = ".", command = self.dot)
		self.btn_dot.grid(row = 4, column = 0)

		self.btn_clear = tkinter.ttk.Button(self, text = "CE", command = self.clear)
		self.btn_clear.grid(row = 1, column = 5)

	def dot(self):
		text = self.entr.get()+"."
		self.text_in_lbl.set(text)

	def zero(self):
		text = self.entr.get()+"0"
		self.text_in_lbl.set(text)

	def one(self):
		text = self.entr.get()+"1"
		self.text_in_lbl.set(text)

	def two(self):
		text = self.entr.get()+"2"
		self.text_in_lbl.set(text)

	def three(self):
		text = self.entr.get()+"3"
		self.text_in_lbl.set(text)

	def four(self):
		text = self.entr.get()+"4"
		self.text_in_lbl.set(text)

	def five(self):
		text = self.entr.get()+"5"
		self.text_in_lbl.set(text)

	def six(self):
		text = self.entr.get()+"6"
		self.text_in_lbl.set(text)

	def seven(self):
		text = self.entr.get()+"7"
		self.text_in_lbl.set(text)

	def eigth(self):
		text = self.entr.get()+"8"
		self.text_in_lbl.set(text)

	def nine(self):
		text = self.entr.get()+"9"
		self.text_in_lbl.set(text)

	def plus(self):
		text = self.entr.get()+"+"
		self.text_in_lbl.set(text)

	def minus(self):
		text = self.entr.get()+"-"
		self.text_in_lbl.set(text)

	def multiply(self):
		text = self.entr.get()+"*"
		self.text_in_lbl.set(text)

	def devide(self):
		text = self.entr.get()+"/"
		self.text_in_lbl.set(text)

	def clear(self):
		self.text_in_lbl.set("")

	def result(self):
		text = self.entr.get()
		result = 0.0
		if "+" in text:
			index = text.index("+")
			result= float(text[:index])+float(text[index+1:])
		elif "-" in text:
			index = text.index("-")
			result= float(text[:index])-float(text[index+1:])
		elif "*" in text:
			index = text.index("*")
			result= float(text[:index])*float(text[index+1:])
		elif "/" in text:
			index = text.index("/")
			result= float(text[:index])/float(text[index+1:])
		self.text_in_lbl.set(text+"="+str(result))


root = tk.Tk()
app = Application(master = root)
root.mainloop()
