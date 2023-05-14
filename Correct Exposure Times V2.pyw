import tkinter as tk

def calculate():
    if use_saved_initial.get() == 1:
        layer_height = 0.03
        exposure_time = 2
        bottom_exposure_time = 14
    else:
        layer_height = float(layer_height_entry.get())
        exposure_time = float(exposure_time_entry.get())
        bottom_exposure_time = float(bottom_exposure_time_entry.get())

    new_layer_height = float(new_layer_height_entry.get())

    # calculate new exposure time
    percent_increase = (new_layer_height - layer_height) / layer_height * 100
    new_exposure_time = exposure_time + percent_increase / 2 / 100 * exposure_time

    # calculate new bottom exposure time
    new_bottom_exposure_time = bottom_exposure_time + percent_increase / 2 / 100 * bottom_exposure_time

    # update result text box
    result_text.delete("1.0", "end")
    result_text.insert("end", f"Layer height: {new_layer_height:.2f} mm\n")
    result_text.insert("end", f"Exposure time: {new_exposure_time:.2f} s\n")
    result_text.insert("end", f"Bottom exposure time: {new_bottom_exposure_time:.2f} s\n")

# create main window
window = tk.Tk()
window.title("3D Printer Calculation")
window.geometry("380x430")

# create widgets
use_saved_initial = tk.IntVar()
use_saved_initial_checkbox = tk.Checkbutton(window, text="Use saved initial values", variable=use_saved_initial)
use_saved_initial_checkbox.grid(row=0, column=0, sticky="w")

layer_height_label = tk.Label(window, text="Current Layer height (mm):")
layer_height_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
layer_height_entry = tk.Entry(window)
layer_height_entry.grid(row=1, column=1)

exposure_time_label = tk.Label(window, text="Exposure time (s):")
exposure_time_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
exposure_time_entry = tk.Entry(window)
exposure_time_entry.grid(row=2, column=1)

bottom_exposure_time_label = tk.Label(window, text="Bottom exposure time (s):")
bottom_exposure_time_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
bottom_exposure_time_entry = tk.Entry(window)
bottom_exposure_time_entry.grid(row=3, column=1)

new_layer_height_label = tk.Label(window, text="New layer height (mm):")
new_layer_height_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
new_layer_height_entry = tk.Entry(window)
new_layer_height_entry.grid(row=4, column=1)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

result_label = tk.Label(window, text="Result:")
result_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
result_text = tk.Text(window, width=30, height=6)
result_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# start main loop
window.mainloop()
