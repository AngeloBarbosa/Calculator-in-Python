from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

btn_sum = Button(frame, text = '+',
    width = 5
)
btn_sum.pack(side = RIGHT)

btn_sub = Button(frame, text = '-',
    width = 5
)
btn_sub.pack(side = LEFT)



root.mainloop()

