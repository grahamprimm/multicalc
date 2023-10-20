import tkinter as tk

class CurrencyCalculator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()

        self.conversiontable = [[1, 0.95, 7.32],
                                [1.06, 1, 7.74],
                                [0.14, 0.13, 1]]

        self.create_widgets()

    def create_widgets(self):
        self.amount_label = tk.Label(self, text="Enter Amount:")
        self.amount_label.grid(row=0, column=0)

        self.amount_e = tk.Entry(self)
        self.amount_e.grid(row=0, column=1)

        self.unit_var1 = tk.StringVar(value="Select unit")
        self.unit_menu1 = tk.OptionMenu(self, self.unit_var1, "Dollar ($)", "Euro (€)", "Yuan (¥)")
        self.unit_menu1.grid(row=0, column=2)

        self.unit_var2 = tk.StringVar(value="Convert to")
        self.unit_menu2 = tk.OptionMenu(self, self.unit_var2, "Dollar ($)", "Euro (€)", "Yuan (¥)")
        self.unit_menu2.grid(row=1, column=2)

        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.grid(row=1, column=0, columnspan=2)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=2, column=0)

        self.result = tk.Label(self)
        self.result.grid(row=2, column=1, columnspan=2)

    def convert(self):
        try:
            amount = float(self.amount_e.get())
            amount_unit = self.unit_var1.get()
            convert_to = self.unit_var2.get()
            label = convert_to
            if '$' in amount_unit:
                amount_unit = 0
            elif '€' in amount_unit:
                amount_unit = 1
            else:
                amount_unit = 2
            if '$' in convert_to:
                convert_to = 0
            elif '€' in convert_to:
                convert_to = 1
            else:
                convert_to = 2
            amount = float(amount) * self.conversiontable[amount_unit][convert_to]
            self.result.config(text=f"{label[-2]} {amount}")
        except Exception as e:
            self.result.config(text="Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyCalculator(master=root)
    app.mainloop()
