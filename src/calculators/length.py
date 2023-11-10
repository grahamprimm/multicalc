import tkinter as tk

class InchesToFeetCalculator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()

        self.create_widgets()

    def create_widgets(self):
        self.inches_label = tk.Label(self, text="Enter Inches:")
        self.inches_label.grid(row=0, column=0)

        self.inches_entry = tk.Entry(self)
        self.inches_entry.grid(row=0, column=1)

        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.grid(row=1, columnspan=2)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=2, column=0)

        self.result = tk.Label(self)
        self.result.grid(row=2, column=1)

    def convert(self):
        try:
            inches = float(self.inches_entry.get())
            feet = inches / 12
            self.result.config(text=f"{feet} feet")
        except ValueError:
            self.result.config(text="Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = InchesToFeetCalculator(master=root)
    app.mainloop()
