from tkinter import *


def button_clicked():
    print("I got clicked")
    answer = int(input.get()) * 1.609
    output['text'] = answer

window = Tk()
window.title("GUI program")
window.minsize(width="500", height="300")
window.config(padx=20, pady=20)



is_equal_to = Label(text="Is equal to", font=("Arial", 24, "bold"))
is_equal_to.grid(column=0, row=1)

output = Label(text="0", font=("Arial", 24, "bold"))
output.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)

miles = Label(text="Miles", font=("Arial", 24, "bold"))
miles.grid(column=2, row=0)


calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)


input = Entry(width=10)
input.grid(column=1, row=0)







window.mainloop()

