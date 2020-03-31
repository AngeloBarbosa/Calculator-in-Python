
from tkinter import *



class Application:

    root = Tk()
    
    display_var = ''
    nums = [0, 0]
    result = 0
    operation = -1

    num_buttons = []
    operation_buttons = []
    
    def __init__(self, master = None):
        self.frame = Frame(master)
        self.frame.pack()

        self.btn0 = Button(self.frame)
        self.btn1 = Button(self.frame)
        self.btn2 = Button(self.frame)
        self.btn3 = Button(self.frame)
        self.btn4 = Button(self.frame)
        self.btn5 = Button(self.frame)
        self.btn6 = Button(self.frame)
        self.btn7 = Button(self.frame)
        self.btn8 = Button(self.frame)
        self.btn9 = Button(self.frame)
        self.btn0 = Button(self.frame)


        self.btn_sum = Button(self.frame)
        self.btn_sub = Button(self.frame)
        self.btn_mult = Button(self.frame)
        self.btn_div = Button(self.frame)

        num_buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        operation_buttons = [self.btn_sum, self.btn_sub, self.btn_mult, self.btn_div]

        operation_buttons[0]['text'] = '+'
        operation_buttons[1]['text'] = '-'
        operation_buttons[2]['text'] = '*'
        operation_buttons[3]['text'] = '/'

        for btn in operation_buttons:

            btn['font'] = 'Montserrat'
            btn['width'] = 15
            #btn['height'] = 15
            #btn.bind('<Button-1>', pressed_operation)

            btn.pack(self.frame)

        for btn in num_buttons:

            index = num_buttons.index(btn)
            
            btn['font'] = 'Arial'
            btn['width'] = 20
            #btn['heigth'] = 15
            btn['text'] = str(index)
            #btn.bind('<Button-1>', pressed_num)

            btn.pack(self.frame)

        self.display = Label(self.frame, text = 'display label is here')
        self.display['font'] = 'Montserrat'
        self.display.pack(self.frame)
        
    '''   
    def pressed_num(self, event):
        
        display_var += num_buttons.index(self)

    def pressed_operation(self, event):

        if display_var != '':
            nums[0] = int(display_var)
            display_var = ''
            operation = operation_buttons.index(self)

        refresh_display()
        
    def pressed_equals(self, event):
        nums[1] = int(display_var)

        if operation != -1:
            if operation == 0:
                result = num[1] + num[2]
            elif operation == 1:
                result = num[1] - num[2]
            elif operation == 2:
                result = num[1] * num[2]
            elif operation == 3:
                result = num[1] / num[2]

            display_var = str(result)
            operation = -1

        refresh_display()

    def refresh_display(self, event):

        self.display['text'] = display_var
    '''

    root.mainloop()       

    


