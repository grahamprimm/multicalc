import tkinter as tk

class SlopeCalculator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()
        
        self.create_widgets()

    def create_widgets(self):
        self.point1_label = tk.Label(self, text="Point 1 (x1, y1):")
        self.point1_label.grid(row=0, column=0)

        self.x1_entry = tk.Entry(self)
        self.x1_entry.grid(row=0, column=1)

        self.y1_entry = tk.Entry(self)
        self.y1_entry.grid(row=0, column=2)

        self.point2_label = tk.Label(self, text="Point 2 (x2, y2):")
        self.point2_label.grid(row=1, column=0)

        self.x2_entry = tk.Entry(self)
        self.x2_entry.grid(row=1, column=1)

        self.y2_entry = tk.Entry(self)
        self.y2_entry.grid(row=1, column=2)

        self.calculate_button = tk.Button(self, text="Calculate Slope", command=self.calculate_slope)
        self.calculate_button.grid(row=2, columnspan=3)

        self.result_label = tk.Label(self, text="Slope:")
        self.result_label.grid(row=3, column=0)

        self.result = tk.Label(self)
        self.result.grid(row=3, column=1, columnspan=2)

    def calculate_slope(self):
        try:
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())

            if x1 == x2:
                self.result.config(text="Undefined (vertical line)")
            else:
                slope = (y2 - y1) / (x2 - x1)
                self.result.config(text=f"Slope: {slope}")
        except ValueError:
            self.result.config(text="Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = SlopeCalculator(master=root)
    app.mainloop()
