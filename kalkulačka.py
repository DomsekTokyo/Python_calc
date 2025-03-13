from tkinter import *
okno = Tk()

okno.title("Kalkulačka")
okno.iconbitmap("ikonka.ico")
okno.geometry("500x500+500+300")
okno.resizable(False,False)
okno.config(bg = "#4C5958")
main_font = ("Helvetice",20)


davat = Entry(okno, width=30, borderwidth= 5, relief="sunken",font = main_font, justify="right", background="#10403B", fg = "white" )
davat.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10)

okno.mainloop()