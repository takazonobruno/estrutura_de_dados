import sys
from tkinter import *
from infixposfix import *


# Create the GUI
tk = Tk()
tk.title('INSERIR EXPRESSÃO PRA CONVERTER PRA POSFIXO E VER O RESULTADO DO CALCULO')




inp = Entry(tk, text="Enter Expression Here", width=100)
inp.pack()


canvas = Canvas(tk, width=800, height=600)
canvas.pack()

btn = Button(tk, text="SAIR?")
btn.pack()

# Create callback functions
def end_program(event):
    '''Destroys the window and ends the program without needing
    to use global variables or a while loop'''
    tk.destroy()
    sys.exit() # Automatically ends any Python program

def update_canvas(event):
    '''Gets the input, tries to eval it, and displays it to the canvas'''
    expression = inp.get()
    posfixa = postfix(expression)
    try:
        solved = evaluate(posfixa)
    except SyntaxError:
        # The expression wasn't valid, (for example, try typing in "2 +")
        # so I defaulted to something else.
        solved = '??'

    canvas.delete('all') # remove old text to avoid overlapping
    canvas.create_text(95, 20, text='Expressão Infixa:', font=('Times', 12))
    canvas.create_text(350, 30, text=expression, font=('Times', 12))
    canvas.create_text(100, 70, text='Expressão Posfixa:', font=('Times', 12))
    canvas.create_text(285, 70, text=posfixa, font=('Times', 12))
    canvas.create_text(185, 120, text='Resultado do Calculo da Expressão Posfixada:', font=('Times', 12))
    canvas.create_text(370, 120, text=solved,font=('Times', 12))


# Bind callbacks to GUI elements
btn.bind('<Button-1>', end_program)
inp.bind('<KeyRelease>', update_canvas)


# Run the program
tk.mainloop()