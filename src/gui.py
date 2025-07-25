import tkinter as tk
from src.scripts import *
from src.utils import *

class App(tk.Tk):
    """Main application class for the FFDLP GUI."""
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)  # Handle window close
        self.width = 300
        self.height = 210
        self.title("FFDLP")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        try:
            self.iconbitmap("logo.ico")
        except tk.TclError:
            print("Icon file not found. Using default icon.")

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
        self.options = ["Auto Name", "Custom Name", "Date Name", "Static Name", "Search", "Music", "Compress"]
        self.setting_var.set(self.options[check_config("DEFAULTOPTION")])
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
        if self.setting_var.get() != "Custom Name":
            self.conditional_inner_frame.grid_remove()

        # Buttons frame
        self.buttons_frame = tk.Frame(self)
        
        # Settings button
        self.settings_button = tk.Button(self.buttons_frame, text="Settings", command=lambda: self.open_settings())
        self.settings_button.pack(side=tk.LEFT, padx=5)

        # Start button
        self.start_button = tk.Button(self.buttons_frame, text="Start", command=lambda: self.start_action())
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Convert button
        self.convert_button = tk.Button(self.buttons_frame, text="Convert", command=lambda: self.convert_action())
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

    def convert_action(self):
        files = get_file_names(check_config("TEMPFILEPATH"))
        if files == []:
            print("No files to convert.")
            return
        for file in files:
            command = video_convert_mp4(f"{check_config('TEMPFILEPATH')}/{file}")
            print(f"Running command: {command.encode('utf-8')}")
            run_command(command)
            print(f"Converted {file.encode('utf-8')} to mp4 format.")
        print("Conversion completed.\nDeleting temporary files...")
        delete_temp_files(check_config("TEMPFILEPATH"))

    def move_temp_files(self):
        files = get_file_names(check_config("TEMPFILEPATH"))
        if files == []:
            print("No files to move.")
            return
        for file in files:
            source = f"{check_config('TEMPFILEPATH')}/{file}"
            destination = f"{check_config('DEFAULTOUTPUTPATH')}/{file}"
            os.rename(source, destination)
            print(f"Moved {file.encode('utf-8')} to {check_config('DEFAULTOUTPUTPATH')}.")
        print("All temporary files moved.")

    def start_action(self):

        runnable = True
        if self.input_entry.get() == "" and not self.setting_var.get() == "Compress":
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
                command = auto_ytdlp(self.input_entry.get(), check_config("STATICOUTPUTNAME"))
            case "Search":
                command = auto_ytdlp(self.input_entry.get(), '%(title)s')
            case "Music":
                command = audio_ytdlp(self.input_entry.get())
            case "Compress":
                files = get_file_names(check_config("TEMPFILEPATH"))
                for file in files:
                    command = video_compress(f"{check_config('TEMPFILEPATH')}/{file}")
                runnable = False 
            case _:
                # this case is just a fallback, it should never be reached
                command = None
                print("No valid command selected.")
                runnable = False
                return
        
        print(f"Running command: {command.encode('utf-8')}")
        if runnable:
            run_command(command)
        if check_config("AUTOCONVERT") and not self.setting_var.get() == "Music":
            self.convert_action()
        
        # Music files can be moved to the output folder as they will already be in the correct format
        if self.setting_var.get() == "Music":
            self.move_temp_files()
    
    def on_exit(self):
        print("Exiting FFDLP...")
        self.destroy()
    
    def open_settings(self):
        subwindow = tk.Toplevel(self)
        subwindow.title("Settings")
        subwindow.geometry("350x250")
        subwindow.resizable(False, False)
        subwindow.iconbitmap("logo.ico")

        # Options dropdown menu
        dropdown_label = tk.Label(subwindow, text="Option:")
        dropdown_label.pack(anchor="w", padx=10, pady=(10, 0))
        dropdown_var = tk.StringVar(subwindow)
        dropdown_options = ["Auto Name", "Custom Name", "Date Name", "Static Name", "Search", "Music"]
        dropdown_var.set(dropdown_options[check_config("DEFAULTOPTION")])
        dropdown_menu = tk.OptionMenu(subwindow, dropdown_var, *dropdown_options)
        dropdown_menu.pack(fill="x", padx=10, pady=2)

        # Default output path
        output_label = tk.Label(subwindow, text="Default Output Path:")
        output_label.pack(anchor="w", padx=10, pady=(10, 0))
        output_entry = tk.Entry(subwindow)
        output_entry.insert(0, check_config("DEFAULTOUTPUTPATH"))
        output_entry.pack(fill="x", padx=10, pady=2)

        # Default Static Name
        default_label = tk.Label(subwindow, text="Default Static Name:")
        default_label.pack(anchor="w", padx=10, pady=(10, 0))
        default_entry = tk.Entry(subwindow)
        default_entry.insert(0, check_config("STATICOUTPUTNAME"))
        default_entry.pack(fill="x", padx=10, pady=2)

        # Auto convert checkbox
        checkbox_var = tk.BooleanVar()
        checkbox_var.set(check_config("AUTOCONVERT"))
        checkbox = tk.Checkbutton(subwindow, text="Auto Convert", variable=checkbox_var)
        checkbox.pack(anchor="w", padx=10, pady=(10, 0))

        # Buttons frame
        buttons_frame = tk.Frame(subwindow)

        cancel_btn = tk.Button(buttons_frame, text="Cancel", command=subwindow.destroy)
        cancel_btn.pack(side="left", padx=10)

        apply_btn = tk.Button(buttons_frame, text="Apply", command=lambda: apply_settings())
        apply_btn.pack(side="left", padx=10)

        save_btn = tk.Button(buttons_frame, text="Save", command=lambda: save_settings())
        save_btn.pack(side="left", padx=10)

        buttons_frame.pack(side="bottom", fill="x", pady=5)
        
        def apply_settings():
            # Save the settings to the config
            config = load_or_create_config()
            setting = {
                "DEFAULTOPTION": dropdown_options.index(dropdown_var.get()),
                "DEFAULTOUTPUTPATH": output_entry.get(),
                "STATICOUTPUTNAME": default_entry.get(),
                "AUTOCONVERT": checkbox_var.get()
            }
            for key, value in setting.items():
                edit_config(config, key, value)
            print("Settings applied.")
        
        def save_settings():
            apply_settings()
            subwindow.destroy()

# TODO: add wait cursor when running commands