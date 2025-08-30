
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define day order
day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def load_and_plot():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    try:
        # Read Excel
        df = pd.read_excel(file_path)
        df['Day'] = df['Day'].str.strip().str[:3]  # Normalize days
        df = df.set_index('Day').reindex(day_order).reset_index()

        # Set up figure
        fig, axes = plt.subplots(3, 1, figsize=(10, 12), constrained_layout=True)
        fig.suptitle(" Weather Report ", fontsize=20, fontweight='bold')

        # Temperature Plot
        axes[0].plot(df['Day'], df['Temperature'], color='red', marker='o', linewidth=2)
        axes[0].set_title("Temperature (°C)", fontsize=14, pad=10)
        axes[0].set_ylabel("Temp °C")
        axes[0].set_xticks(df['Day'])
        axes[0].grid(True)

        # Humidity Plot
        axes[1].plot(df['Day'], df['Humidity'], color='blue', marker='s', linewidth=2)
        axes[1].set_title("Humidity (%)", fontsize=14, pad=10)
        axes[1].set_ylabel("Humidity %")
        axes[1].set_xticks(df['Day'])
        axes[1].grid(True)

        # Rainfall Plot
        axes[2].bar(df['Day'], df['Rainfall'], color='green')
        axes[2].set_title("Rainfall (mm)", fontsize=14, pad=8)
        axes[2].set_ylabel("Rainfall mm")
        axes[2].set_xlabel("Days of the Week")
        axes[2].set_xticks(df['Day'])
        axes[2].grid(True)

        # Embed in Tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        print("Error:", e)

# Tkinter Window
window = tk.Tk()
window.title("Gilgit-Baltistan Weather Viewer")
window.geometry("900x700")

btn = tk.Button(window, text="📁 Select Weather Excel File", command=load_and_plot, font=("Arial", 13))
btn.pack(pady=20)

window.mainloop()



