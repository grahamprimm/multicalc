import tkinter as tk
from tkinter import ttk
from calculators.temperature import TemperatureCalculator
from calculators.compound_interest import CompoundInterestCalculator
from calculators.slope import SlopeCalculator

class MultiCalc(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MultiCalc")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.temp_calc = TemperatureCalculator(self.notebook)
        self.notebook.add(self.temp_calc, text="Temperature")

        self.compound_interest_calc = CompoundInterestCalculator(self.notebook)
        self.notebook.add(self.compound_interest_calc, text="Compound Interest")

        self.slope_calc = SlopeCalculator(self.notebook)
        self.notebook.add(self.slope_calc, text="Slope")

    def calculate_temperature(self, temp):
        self.temp_calc.temp_entry.delete(0, tk.END)  # Clear the entry
        self.temp_calc.temp_entry.insert(0, str(temp))  # Set the new value
        self.temp_calc.convert()  # Trigger the conversion
        return self.temp_calc.result.cget('text')  # Return the result text

    def get_widget_count(self):
        return len(self.winfo_children())  # Return the number of widgets

if __name__ == "__main__":
    app = MultiCalc()
    app.mainloop()