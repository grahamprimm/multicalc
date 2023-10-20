import tkinter as tk
from tkinter import ttk
from calculators.temperature import TemperatureCalculator
from calculators.compound_interest import CompoundInterestCalculator
from calculators.slope import SlopeCalculator
from calculators.currency import CurrencyCalculator

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

        self.currency_calc = CurrencyCalculator(self.notebook)
        self.notebook.add(self.currency_calc, text="Currency")

        self.inches_to_feet_calc = InchesToFeetCalculator(self.notebook)
        self.notebook.add(self.inches_to_feet_calc, text="Inches to Feet")

    def calculate_temperature(self, temp):
        self.temp_calc.temp_entry.delete(0, tk.END)  # Clear the entry
        self.temp_calc.temp_entry.insert(0, str(temp))  # Set the new value
        self.temp_calc.convert()  # Trigger the conversion
        return self.temp_calc.result.cget('text')  # Return the result text
    
    def calculate_currency(self, amount, curr1, curr2):
        self.currency_calc.amount_e.delete(0, tk.END)
        self.currency_calc.amount_e.insert(0, str(amount))
        self.currency_calc.unit_var1.set(curr1)
        self.currency_calc.unit_var2.set(curr2)
        self.currency_calc.convert()
        return self.currency_calc.result.cget('text')
    
    def calculate_slope(self, p1, p2):
        self.slope_calc.x1_entry.delete(0, tk.END)
        self.slope_calc.x1_entry.insert(0, str(p1[0]))
        self.slope_calc.x2_entry.delete(0, tk.END)
        self.slope_calc.x2_entry.insert(0, str(p2[0]))
        self.slope_calc.y1_entry.delete(0, tk.END)
        self.slope_calc.y1_entry.insert(0, str(p1[1]))
        self.slope_calc.y2_entry.delete(0, tk.END)
        self.slope_calc.y2_entry.insert(0, str(p2[1]))
        self.slope_calc.calculate_slope()
        return self.slope_calc.result.cget('text')
       
    def calculate_inches_to_feet(self, inches):
        feet = inches / 12.0
        self.inches_to_feet_calc.inches_entry.delete(0, tk.END)  
        self.inches_to_feet_calc.inches_entry.insert(0, str(inches)) 
        self.inches_to_feet_calc.convert()  
        return self.inches_to_feet_calc.result.cget('text')   

    def get_widget_count(self):
        return len(self.winfo_children())  # Return the number of widgets

if __name__ == "__main__":
    app = MultiCalc()
    app.mainloop()