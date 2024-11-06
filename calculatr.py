import tkinter as tk


class Calculator:
    expresion = ''

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.geometry('300x350')
        self.root.configure(background='#34e1bd')

        self.frame = tk.Frame(self.root, width=300, height=100, bg='#34e1bd')
        self.frame.grid(row=0, column=0)

        self.str_var = tk.StringVar()
        self.text = tk.Entry(self.frame, width=25, borderwidth=3, bg='#818e8b',
                             font=('Arial', 16, 'bold'), fg='white',
                             justify=tk.RIGHT, textvariable=self.str_var)

        self.text.grid(row=0, column=0, padx=2, pady=10, sticky=tk.W + tk.E)

        self.clear = tk.Button(
            self.frame,
            text='C',
            font=('Arial', 16, 'bold'),
            bg='#21d2d2',
            activebackground='grey',
            activeforeground='red',
            command=self.clear_text
        )
        self.clear.grid(row=1, column=0, padx=2, pady=10, sticky=tk.E + tk.W)

        self.button_frame = tk.Frame(self.root, width=300, height=250,
                                     bg='#579dbb')

        self.button_frame.grid(row=1, column=0, padx=2, pady=10, sticky=tk.W + tk.E)

        self.frame.grid_propagate(False)
        self.number_grid()  # Aici trebuie să fie apelată metoda corectă

        self.root.mainloop()

    def clear_text(self):
        Calculator.expresion = ''
        self.str_var.set(Calculator.expresion)

    def btn_click(self, strng):

        if strng == '=':
            try:

                Calculator.expresion = str(eval(Calculator.expresion))
                self.str_var.set(Calculator.expresion)
            except Exception as e:
                self.str_var.set("Error")
                Calculator.expresion = ''
        else:

            Calculator.expresion += strng
            self.str_var.set(Calculator.expresion)

    def add_number(self, btn_number):
        btn = tk.Button(self.button_frame,
                        text=btn_number,
                        width=4,
                        height=1,
                        font=('Arial', 16),
                        bg='#21d2d2',
                        fg='black',
                        command=lambda: self.btn_click(btn_number)
                        )
        return btn

    def number_grid(self):
        NUMBERS = [
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('%', '0', '/', '='),
        ]
        for i, item in enumerate(NUMBERS):
            for j, number in enumerate(item):
                btn = self.add_number(number)
                btn.grid(row=i, column=j, padx=1, pady=1)


if __name__ == '__main__':
    Calculator()
