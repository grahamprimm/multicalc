import tkinter as tk

class CompoundInterestCalculator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()
        
        self.create_widgets()

    def create_widgets(self):
        self.principal_label = tk.Label(self, text="Principal Amount ($):")
        self.principal_label.grid(row=0, column=0)

        self.principal_entry = tk.Entry(self)
        self.principal_entry.grid(row=0, column=1)

        self.rate_label = tk.Label(self, text="Annual Interest Rate (%):")
        self.rate_label.grid(row=1, column=0)

        self.rate_entry = tk.Entry(self)
        self.rate_entry.grid(row=1, column=1)

        self.times_compounded_label = tk.Label(self, text="Times Compounded Annually:")
        self.times_compounded_label.grid(row=2, column=0)

        self.times_compounded_entry = tk.Entry(self)
        self.times_compounded_entry.grid(row=2, column=1)

        self.years_label = tk.Label(self, text="Years:")
        self.years_label.grid(row=3, column=0)

        self.years_entry = tk.Entry(self)
        self.years_entry.grid(row=3, column=1)

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, columnspan=2)

        self.result_label = tk.Label(self, text="Amount ($):")
        self.result_label.grid(row=5, column=0)

        self.result = tk.Label(self)
        self.result.grid(row=5, column=1)

    def calculate(self):
        try:
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get()) / 100
            times_compounded = int(self.times_compounded_entry.get())
            years = float(self.years_entry.get())

            amount = principal * (1 + rate / times_compounded)**(times_compounded * years)
            self.result.config(text=f"${amount:.2f}")
        except ValueError:
            self.result.config(text="Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompoundInterestCalculator(master=root)
    app.mainloop()
