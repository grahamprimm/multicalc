import tkinter as tk

class TemperatureCalculator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()
        
        self.create_widgets()

    def create_widgets(self):
        self.temp_label = tk.Label(self, text="Enter Temperature:")
        self.temp_label.grid(row=0, column=0)

        self.temp_entry = tk.Entry(self)
        self.temp_entry.grid(row=0, column=1)

        self.unit_var = tk.StringVar(value="Celsius")
        self.unit_menu = tk.OptionMenu(self, self.unit_var, "Celsius", "Fahrenheit")
        self.unit_menu.grid(row=0, column=2)

        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.grid(row=1, columnspan=3)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=2, column=0)

        self.result = tk.Label(self)
        self.result.grid(row=2, column=1, columnspan=2)

    def convert(self):
        try:
            temp = float(self.temp_entry.get())
            unit = self.unit_var.get()
            if unit == "Celsius":
                result = temp * 9/5 + 32
                self.result.config(text=f"{result} Fahrenheit")
            else:
                result = (temp - 32) * 5/9
                self.result.config(text=f"{result} Celsius")
        except ValueError:
            self.result.config(text="Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureCalculator(master=root)
    app.mainloop()
