from tkinter import *
global unit, choice1, choice2, ans, ans_result
options = ['Miles',
           'Feet',
           'Inches',
           'Kilometers',
           'Meters',
           'Centimeters']

root = Tk()
root.geometry('420x280')
root.title('Distance Convertor')


def btn_convert():              # Conversion Button
    choice1 = clicked1.get()
    choice2 = clicked2.get()
    input_num = entry.get()
    ans = calculate(choice1, choice2, int(input_num))
    ans_result.set((str(ans), choice2))


# Clear Button
def btn_clear():
    entry.delete(0, END)


title = Label(root, width=30, justify='right', font=('Monaco', 20, 'bold'), text='Distance Convertor')
title.grid(row=0, column=0, columnspan=2)

entry = Entry(root, width=40, justify='right', font=('Monaco', 15, 'bold'))
entry.grid(row=1, column=0, columnspan=2)

clicked1 = StringVar()
clicked1.set('Miles')
clicked2 = StringVar()
clicked2.set('Miles')

orig_unit = OptionMenu(root, clicked1, *options)
orig_unit.grid(row=2, column=0)
orig_unit.config(height=1, width=14, font=('Monaco', 15, 'bold'))
menu = root.nametowidget(orig_unit.menuname)                        #Use nametowidget to change font of whole menu
menu.config(font='Monaco')

new_unit = OptionMenu(root, clicked2, *options)
new_unit.grid(row=2, column=1)
new_unit.config(height=1, width=14, font=('Monaco', 15, 'bold'))
menu2 = root.nametowidget(new_unit.menuname)
menu2.config(font='Monaco')

convert_btn = Button(root, fg='blue', height=4, width=15, text='Convert',font=('Monaco', 15, 'bold'), command=btn_convert)
convert_btn.config(background='blue', activeforeground='white')
convert_btn.grid(row=3, column=0)

clear_btn = Button(root, height=4, width=15, text='Clear', font=('Monaco', 15, 'bold'), activeforeground='red', command=btn_clear)
clear_btn.config(fg='blue')
clear_btn.grid(row=3, column=1)

ans_result = StringVar()
result = Entry(root, width=40, textvariable=ans_result, font=('Monaco', 15, 'bold'))
result.grid(row=4, column=0, columnspan=2)
result.config(width=40, justify='right')

close_btn = Button(root, height = 2, width =18, text='Close', font=('Monaco', 10, 'bold'), command=root.destroy)
close_btn.grid(row=5, column=1)

def calculate(unit1, unit2, n):
    """Convert n (int) from unit type unit1 to unit type unit 2"""
    ans = 0
    if unit2 == 'Miles':
        ans = conversion_dict[unit1][0] * n
    elif unit2 == 'Feet':
        ans = conversion_dict[unit1][1] * n
    elif unit2 == 'Inches':
        ans = conversion_dict[unit1][2] * n
    elif unit2 == 'Kilometers':
        ans = conversion_dict[unit1][3] * n
    elif unit2 == 'Meters':
        ans = conversion_dict[unit1][4] * n
    elif unit2 == 'Centimeters':
        ans = conversion_dict[unit1][5] * n
    return ans


conversion_dict = {'Miles': [1, 5280, 63360, 1.60934, 1609.34, 160934],
                   'Feet': [0.000189394, 1, 12, 0.0003048, 0.3048, 30.48],
                   'Inches': [0.00001578282828, 0.0833333, 1, 0.0000254000508, 0.0254, 2.54],
                   'Kilometers': [0.621371, 3280.84, 39370.1, 1, 1000, 100000],
                   'Meters': [0.000621371, 3.28084, 39.37008, 0.001, 1, 100],
                   'Centimeters': [0.000006213727366, 0.0328084, 0.3937008, 0.00001, 0.01, 1]}

root.mainloop()