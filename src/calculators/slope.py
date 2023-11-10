import tkinter as tk

class SlopeCalculator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()
        self.ERROR_STR = "Invalid input"
        self.create_widgets()

    def create_widgets(self):
        self.create_point_entry("Point 1 (x1, y1):", 0)
        self.create_point_entry("Point 2 (x2, y2):", 1)

        self.calculate_button = tk.Button(self, text="Calculate Slope", command=self.calculate_slope)
        self.calculate_button.grid(row=2, columnspan=3)

        self.result_label = tk.Label(self, text="Slope:")
        self.result_label.grid(row=3, column=0)

        self.result = tk.Label(self)
        self.result.grid(row=3, column=1, columnspan=2)

    def create_point_entry(self, text, row):
        label = tk.Label(self, text=text)
        label.grid(row=row, column=0)

        x_entry = tk.Entry(self)
        x_entry.grid(row=row, column=1)

        y_entry = tk.Entry(self)
        y_entry.grid(row=row, column=2)

        setattr(self, f"x{row + 1}_entry", x_entry)
        setattr(self, f"y{row + 1}_entry", y_entry)
        setattr(self, f"point{row + 1}_label", label)  # Store label as an attribute

    def calculate_slope(self):
        try:
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())

            if x1 == x2:
                self.result.config(text="Undefined (vertical line)")
            else:
                slope = round((y2 - y1) / (x2 - x1), 2)
                self.result.config(text=f"Slope: {slope}")
        except ValueError:
            self.result.config(text=self.ERROR_STR)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlopeCalculator(master=root)
    app.mainloop()
