from tkinter import *
okno = Tk()

okno.title("Kalkulačka")
okno.iconbitmap("ikonka.ico")
okno.geometry("500x550+500+300")
okno.resizable(False,False)
okno.config(bg = "#4C5958")
main_font = ("Helvetice",20)
number_font = ("helvetica",30)


frame1 = Frame(okno, bg = "#4C5958")
frame1.pack()
frame2 = Frame(okno, bg = "#4C5958")
frame2.pack()

davat = Entry(frame1, width=30, borderwidth= 5, relief="sunken",font = main_font, justify="right", background="#10403B", fg = "white" )
davat.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10)

button_1 = Button(frame2,text="1",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_1.grid(column=0, row = 2, padx=10, pady=10, ipadx=20, ipady=5)

button_2 = Button(frame2,text="2",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_2.grid(column=1, row = 2, padx=10, pady=10, ipadx=20, ipady=5)

button_3 = Button(frame2,text="3",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_3.grid(column=2, row = 2, padx=10, pady=10, ipadx=20, ipady=5)

button_4 = Button(frame2,text="4",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_4.grid(column=0, row = 1, padx=10, pady=10, ipadx=20, ipady=5)

button_5 = Button(frame2,text="5",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_5.grid(column=1, row = 1, padx=10, pady=10, ipadx=20, ipady=5)

button_6 = Button(frame2,text="6",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_6.grid(column=2, row = 1, padx=10, pady=10, ipadx=20, ipady=5)

button_7= Button(frame2,text="7",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_7.grid(column=0, row = 0, padx=10, pady=10, ipadx=20, ipady=5)

button_8 = Button(frame2,text="8",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_8.grid(column=1, row = 0, padx=10, pady=10, ipadx=20, ipady=5)

button_9 = Button(frame2,text="9",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_9.grid(column=2, row = 0, padx=10, pady=10, ipadx=20, ipady=5)

button_0 = Button(frame2,text="0",font = number_font, borderwidth= 5, relief="groove",activeforeground=  "white",activebackground="#03A688", fg="white",bg="#005C53")
button_0.grid(column=1, row = 3, padx=10, pady=10, ipadx=20, ipady=5)
okno.mainloop()