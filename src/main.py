import tkinter as tk
from tkinter import ttk
from calculators.temperature import TemperatureCalculator
from calculators.compound_interest import CompoundInterestCalculator
from calculators.slope import SlopeCalculator
from calculators.currency import CurrencyCalculator
from calculators.length import InchesToFeetCalculator

class MultiCalc(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MultiCalc")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.TempCalc_APP = TemperatureCalculator(self.notebook)
        self.notebook.add(self.TempCalc_APP, text="Temperature")

        self.CompInt_APP = CompoundInterestCalculator(self.notebook)
        self.notebook.add(self.CompInt_APP, text="Compound Interest")

        self.Slope_APP = SlopeCalculator(self.notebook)
        self.notebook.add(self.Slope_APP, text="Slope")

        self.Currency_APP = CurrencyCalculator(self.notebook)
        self.notebook.add(self.Currency_APP, text="Currency")

        self.InchesFeet_APP = InchesToFeetCalculator(self.notebook)
        self.notebook.add(self.InchesFeet_APP, text="Inches to Feet")

    def calculate_temperature(self, temp):
        self.TempCalc_APP.temp_entry.delete(0, tk.END)  # Clear the entry
        self.TempCalc_APP.temp_entry.insert(0, str(temp))  # Set the new value
        self.TempCalc_APP.convert()  # Trigger the conversion
        return self.TempCalc_APP.result.cget('text')  # Return the result text
    
    def calculate_currency(self, amount, curr1, curr2):
        self.Currency_APP.amount_e.delete(0, tk.END)
        self.Currency_APP.amount_e.insert(0, str(amount))
        self.Currency_APP.unit_var1.set(curr1)
        self.Currency_APP.unit_var2.set(curr2)
        self.Currency_APP.convert()
        return self.Currency_APP.result.cget('text')
    
    def calculate_slope(self, p1, p2):
        self.Slope_APP.x1_entry.delete(0, tk.END)
        self.Slope_APP.x1_entry.insert(0, str(p1[0]))
        self.Slope_APP.x2_entry.delete(0, tk.END)
        self.Slope_APP.x2_entry.insert(0, str(p2[0]))
        self.Slope_APP.y1_entry.delete(0, tk.END)
        self.Slope_APP.y1_entry.insert(0, str(p1[1]))
        self.Slope_APP.y2_entry.delete(0, tk.END)
        self.Slope_APP.y2_entry.insert(0, str(p2[1]))
        self.Slope_APP.calculate_slope()
        return self.Slope_APP.result.cget('text')
       
    def calculate_inches_to_feet(self, inches):
        self.InchesFeet_APP.inches_entry.delete(0, tk.END)  
        self.InchesFeet_APP.inches_entry.insert(0, str(inches)) 
        self.InchesFeet_APP.convert()  
        return self.InchesFeet_APP.result.cget('text')   

    def get_widget_count(self):
        return len(self.winfo_children())  # Return the number of widgets

if __name__ == "__main__":
    app = MultiCalc()
    app.mainloop()