from tkinter import *


def button_clicked():
    print('I got clicked')
    my_label.config(text=input.get())


window = Tk()
window.title('My First GUI Program')
window.minsize(600, 360)
window.config(padx=30, pady=30)

# Label
my_label = Label(text='Miles', font=('Arial', 20, 'bold'))
my_label.grid(column=2, row=0)


# my_label['text'] = 'Salom men maqsadlarimga erishdim'
# my_label.config(text='This is function')


# Button
button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = Button(text='New button')
# new_button.grid(column=2, row=0

# Entry
input = Entry(width=12)
print(input.get())
input.grid(column=1, row=0)




window.mainloop()