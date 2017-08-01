#dvjPageGenerators.py - Generates Pages 10,11,20,21 based on filament lenghts
#Copyright (C) 2017  Mark Ferrick
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at my option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from Tkinter import *

def flip_it(s):
	return s[8:10] + s[6:8] + s[4:6] + s[2:4] 

def pad_it(some_length):
	zero_str ='0'

	for x in range(1,10 - len(hex(int(some_length)))):
		zero_str = zero_str + '0'

	xlen =  hex(int(some_length))
	full_x =  xlen[:2] + zero_str + xlen[2:]

	return full_x

def doit(e2, e3, e4, e5, e6):
	length = e2.get()
	if len(length)==0:
		return
	e4.delete(0,END)
	e5.delete(0,END)
	e6.delete(0,END)

	fullxlen = pad_it(length)
	Page10 = flip_it(fullxlen)
	what2xor = fullxlen

	Page11 = Page10
	if len(e3.get()) != 0:
		rem_len = e3.get()
		fullxrem = pad_it(rem_len)
		Page20 = flip_it(fullxrem)
		what2xor = fullxrem
	else:
		Page20 = Page10

	Page21 = flip_it(hex(int(what2xor,16)^int('0x54321248', 16))) # 0x54321248 is a magic number 

	e4.insert(0,Page10)
	e5.insert(0,Page20)
	e6.insert(0,Page21)


window = Tk()
window.title("DaVinci Jr Page Generator")
window.geometry("350x150")
#Original Spool size
l2=Label(window, text="Spool Lenght")
l2.grid(row=2, column=1, sticky=E)
l2a=Label(window, text="Decimal, in mm")
l2a.grid(row=2, column=3, sticky=W)
# Remaining Length
l3=Label(window, text="Remaining Lenght")
l3.grid(row=3, column=1, sticky=E)
l3a=Label(window, text="Decimal, in mm")
l3a.grid(row=3, column=3, sticky=W)
#Page10 and Page 11
l4=Label(window, text="Page10, 11")
l4.grid(row=4, column=1, sticky=E)
l4a=Label(window, text="Hexadecmal")
l4a.grid(row=4, column=3, sticky=W)
#Page 20 ( amount used )
l5=Label(window, text="Page 20")
l5.grid(row=5, column=1, sticky=E)
l5a=Label(window, text="Hexadecmal")
l5a.grid(row=5, column=3, sticky=W)
#Page 21 Checksum
l6=Label(window, text="Page 21")
l6.grid(row=6, column=1, sticky=E)
l6a=Label(window, text="Hexadecmal")
l6a.grid(row=6, column=3, sticky=W)

len_text=StringVar()
e2=Entry(window, textvariable=len_text)
e2.grid(row=2, column=2)

rem_text=StringVar()
e3=Entry(window, textvariable=rem_text)
e3.grid(row=3, column=2)

page10_text=StringVar()
e4=Entry(window, textvariable=page10_text)
e4.grid(row=4, column=2)

page20_text=StringVar()
e5=Entry(window, textvariable=page20_text)
e5.grid(row=5, column=2)

page21_text=StringVar()
e6=Entry(window, textvariable=page21_text)
e6.grid(row=6, column=2)

b1=Button(window, text="Generate Page Data", bg='green', width=16, command=lambda: doit(e2, e3, e4, e5, e6))
b1.grid(row=1, column=2, sticky=W)

#end of window object
window.mainloop()

