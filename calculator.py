
from tkinter import *

root = Tk()

class Application:

    
    def pressed_number(self, event):
        
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
    
    def __init__(self, master = None):
        display_var = ''
        num = [0, 0]
        result = 0
        operation = -1

        num_buttons = []
        operation_buttons = []

        self.frame = Frame()
        self.frame.pack()

        for index in range(10):

            num_buttons.append(Button(self.frame))
            
            num_buttons[-1]['font'] = 'Arial'
            num_buttons[-1]['width'] = 20
            num_buttons[-1]['text'] = str(index)
            
            num_buttons[-1].pack()
            num_buttons[-1].bind('<Button-1>', pressed_number)


        for index in range(4): # the order is +, -, *, /
            
            operation_buttons.append(Button(self.frame))

            operation_buttons[-1]['font'] = 'Montserrat'
            operation_buttons[-1]['width'] = 15

            operation_buttons[-1].pack()
            operation_buttons[-1].bind('<Button-1>', pressed_operation)

        operation_buttons[0]['text'] = '+'
        operation_buttons[1]['text'] = '-'
        operation_buttons[2]['text'] = '*'
        operation_buttons[3]['text'] = '/'


        self.display = Label(self.frame, text = 'display label is here')
        self.display['font'] = 'Montserrat'
        self.display.pack()
        

    


tela = Application(root)
root.mainloop()       

