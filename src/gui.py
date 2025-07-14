import tkinter as tk
from scripts import *
from utils import *

class App(tk.Tk):
    """Main application class for the FFDLP GUI."""
    def __init__(self):
        super().__init__()
        self.config = load_or_create_config()
        self.width = 300
        self.height = 210
        self.title("FFDLP GUI")
        self.geometry(f"{self.width}x{self.height}")

        # Input frame
        self.input_frame = tk.Frame(self)

        # Input field and Clipboard button
        self.input_label = tk.Label(self.input_frame, text="Input:")
        self.input_label.grid(row=1, column=1, padx=3, pady=0, sticky=(tk.W))
        self.input_entry = tk.Entry(self.input_frame, width=30)
        self.input_entry.grid(row=2, column=1, padx=(1, 10), pady=0, sticky=(tk.W))

        self.import_button = tk.Button(self.input_frame, text="clipboard", command=lambda: self.set_input(self.get_clipboard_data()))
        self.import_button.grid(row=2, column=2, padx=5, pady=10)

        self.input_frame.pack(pady=5)

        # Conditional input frame
        self.conditional_frame = tk.Frame(self, height=21)
        self.conditional_frame.pack(pady=5)

        # inner frame for conditional input
        self.conditional_inner_frame = tk.Frame(self.conditional_frame)

        # Dropdown menu for settings
        self.setting_label = tk.Label(self, text="Settings:")
        self.setting_label.pack()
        self.setting_var = tk.StringVar(self)
        self.options = ["Auto Name", "Custom Name", "Date Name", "Static Name", "Search", "Music"]
        self.setting_var.set(self.options[0])  # Default value
        self.setting_menu = tk.OptionMenu(self, self.setting_var, *self.options, command=self.on_option_change)
        self.setting_menu.pack(pady=(0, 10))

        # Conditional input field
        self.name_label = tk.Label(self.conditional_inner_frame, text="Filename:")
        self.name_label.grid(row=1, column=1, padx=3, pady=0, sticky=(tk.W))
        self.conditional_var = tk.StringVar()
        self.conditional_entry = tk.Entry(self.conditional_inner_frame, textvariable=self.conditional_var)
        self.conditional_entry.grid(row=1, column=2, padx=(1, 10), pady=0, sticky=(tk.W))
        # Initially hidden
        self.conditional_inner_frame.grid(row=1, column=1, sticky=(tk.W, tk.E))
        self.conditional_inner_frame.grid_remove()

        # Buttons frame
        self.buttons_frame = tk.Frame(self)
        
        # Settings button
        self.settings_button = tk.Button(self.buttons_frame, text="Settings", command=lambda: print("Settings clicked"))
        self.settings_button.pack(side=tk.LEFT, padx=5)

        # Start button
        self.start_button = tk.Button(self.buttons_frame, text="Start", command=self.start_action)
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Convert button
        self.convert_button = tk.Button(self.buttons_frame, text="Convert", command=lambda: print("Convert clicked"))
        self.convert_button.pack(side=tk.LEFT, padx=5)
        

        self.buttons_frame.pack(pady=5)

    def on_option_change(self, value):
        if value == self.options[1]:
            self.conditional_inner_frame.grid()
        else:
            self.conditional_inner_frame.grid_remove()

    def get_clipboard_data(self):
        try:
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            clipboard_data = root.clipboard_get()
            return clipboard_data
        except tk.TclError:
            return None
        
    def set_input(self, input_value):
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(tk.END, input_value)

    def start_action(self):

        if self.input_entry.get() == "":
            print("Input field is empty. Please enter a URL or search term.")
            return

        match self.setting_var.get():
            case "Auto Name":
                command = std_ytdlp(self.input_entry.get())
            case "Custom Name":
                command = auto_ytdlp(self.input_entry.get(), self.conditional_var.get())
            case "Date Name":
                command = auto_ytdlp(self.input_entry.get())
            case "Static Name":
                command = auto_ytdlp(self.input_entry.get(), self.config["STATICOUTPUTNAME"])
            case "Search":
                command = auto_ytdlp(self.input_entry.get(), '%(title)s')
            case "Music":
                command = audio_ytdlp(self.input_entry.get())
            case _:
                # this case is just a fallback, it should never be reached
                command = None
                print("No valid command selected.")
                return
            
        run_command(command)
        

        


if __name__ == "__main__":
    app = App()
    app.mainloop()

# TODO: Implement file conversion and settings management