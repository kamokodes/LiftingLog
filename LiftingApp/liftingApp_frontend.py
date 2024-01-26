# liftingApp_frontend.py

import tkinter as tk
from tkinter import messagebox
from liftingApp_backend import create_tables, record_lift, get_lift_history

class LiftingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lifting App")

        create_tables()

        self.exercise_label = tk.Label(self.master, text="Exercise:")
        self.exercise_label.grid(row=0, column=0, padx=10, pady=10)

        self.exercise_entry = tk.Entry(self.master)
        self.exercise_entry.grid(row=0, column=1, padx=10, pady=10)

        self.weight_label = tk.Label(self.master, text="Weight (kg):")
        self.weight_label.grid(row=1, column=0, padx=10, pady=10)

        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        self.record_button = tk.Button(self.master, text="Record Lift", command=self.record_lift)
        self.record_button.grid(row=2, columnspan=2, pady=10)

        self.history_button = tk.Button(self.master, text="View History", command=self.view_history)
        self.history_button.grid(row=3, columnspan=2, pady=10)

    def record_lift(self):
        exercise = self.exercise_entry.get()
        weight = self.weight_entry.get()

        if not exercise or not weight:
            messagebox.showwarning("Error", "Please fill in all fields.")
            return

        try:
            weight = float(weight)
        except ValueError:
            messagebox.showwarning("Error", "Invalid weight. Please enter a number.")
            return

        record_lift(exercise, weight)
        messagebox.showinfo("Success", "Lift recorded successfully.")

    def view_history(self):
        history = get_lift_history()

        if not history:
            messagebox.showinfo("Info", "No lift history available.")
        else:
            history_window = tk.Toplevel(self.master)
            history_window.title("Lift History")

            for i, (id, exercise, weight, timestamp) in enumerate(history):
                label_text = f"{i + 1}. {timestamp} - {exercise}: {weight} kg"
                tk.Label(history_window, text=label_text).pack(padx=10, pady=5)

def main():
    root = tk.Tk()
    app = LiftingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
