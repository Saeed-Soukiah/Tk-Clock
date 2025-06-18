"""
======================================================================
Created by: Saeed Soukiah
Date: 2025-06-18
======================================================================
"""

import tkinter as tk
from time import localtime, strftime, time

class Clock:
    def __init__(self, master):
        self.master = master
        self.master.title("Real-Time Clock")
        
        # Initial theme is dark mode
        self.is_dark_mode = True
        # Initial time format is 12-hour mode
        self.use_12_hour = True

        # Create the main time label
        self.time_label = tk.Label(master, font=("Arial", 50))
        self.time_label.pack()

        # Create the day label
        self.day_label = tk.Label(master, font=("Ink Free", 25, "bold"))
        self.day_label.pack()

        # Create the date label
        self.date_label = tk.Label(master, font=("Ink Free", 30))
        self.date_label.pack()

        # Button to toggle between 12-hour and 24-hour time formats
        self.toggle_format_button = tk.Button(master, text="Switch to 24-hour", command=self.toggle_format)
        self.toggle_format_button.pack(pady=10)

        # Button to toggle between dark mode and light mode
        self.toggle_theme_button = tk.Button(master, text="Switch to Light Mode", command=self.toggle_theme)
        self.toggle_theme_button.pack(pady=10)
        
        self.apply_theme()  # Apply initial theme settings
        self.update()       # Start the update loop

    def toggle_format(self):
        self.use_12_hour = not self.use_12_hour
        # Update the button text according to the new format
        if self.use_12_hour:
            self.toggle_format_button.config(text="Switch to 24-hour")
        else:
            self.toggle_format_button.config(text="Switch to 12-hour")
    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        # Update the toggle button text to indicate the other available theme
        if self.is_dark_mode:
            self.toggle_theme_button.config(text="Switch to Light Mode")
        else:
            self.toggle_theme_button.config(text="Switch to Dark Mode")
        # Apply theme changes to all widgets
        self.apply_theme()
    
    def apply_theme(self):
        # Define theme colors for dark and light modes
        if self.is_dark_mode:
            bg_color = "#000000"          # black background
            fg_time = "#00FF00"           # green for the time display
            fg_other = "#FFFFFF"          # white for day and date
            btn_bg = "#333333"            # dark gray for buttons
            btn_fg = "#FFFFFF"            # white text for buttons
        else:
            bg_color = "#FFFFFF"          # white background
            fg_time = "#000000"           # black time text
            fg_other = "#000000"          # black day and date text
            btn_bg = "#DDDDDD"            # light gray for buttons
            btn_fg = "#000000"            # black text for buttons
        
        # Set the background color of the main window
        self.master.configure(bg=bg_color)
        # Update all label colors
        self.time_label.config(bg=bg_color, fg=fg_time)
        self.day_label.config(bg=bg_color, fg=fg_other)
        self.date_label.config(bg=bg_color, fg=fg_other)
        # Update the button styling
        self.toggle_format_button.config(bg=btn_bg, fg=btn_fg,
                                           activebackground=btn_bg, activeforeground=btn_fg)
        self.toggle_theme_button.config(bg=btn_bg, fg=btn_fg,
                                          activebackground=btn_bg, activeforeground=btn_fg)
    
    def update(self):
        current_time = localtime()
        # Select the appropriate time format based on the toggle flag
        if self.use_12_hour:
            time_string = strftime("%I:%M:%S %p", current_time)
        else:
            time_string = strftime("%H:%M:%S", current_time)
            # Optionally add AM/PM in 24-hour mode by uncommenting these lines:
            # am_pm = "AM" if current_time.tm_hour < 12 else "PM"
            # time_string += f" {am_pm}"
        
        # Update the labels with the current time, day, and date
        self.time_label.config(text=time_string)
        self.day_label.config(text=strftime("%A", current_time))
        self.date_label.config(text=strftime("%B %d, %Y", current_time))
        
        # Calculate a precise delay until the next whole second
        delay_ms = int((1 - (time() % 1)) * 1000)
        self.master.after(delay_ms, self.update)

def main():
    root = tk.Tk()
    clock = Clock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
