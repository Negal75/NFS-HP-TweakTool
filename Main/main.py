import os
import tkinter as tk
from tkinter import ttk, messagebox
import configparser

CONFIG_PATH = os.path.expanduser(r"~\Documents\Criterion Games\Need for Speed(TM) Hot Pursuit\config.NFS11Save")

class NFSTweakTool:
    def __init__(self, root):
        self.root = root
        self.root.title("NFS: Hot Pursuit TweakTool")
        self.config = configparser.ConfigParser()
        self.load_config()
        self.create_widgets()

    def load_config(self):
        if os.path.exists(CONFIG_PATH):
            self.config.read(CONFIG_PATH)
        else:
            messagebox.showerror("Error", "Config file not found!")
            self.root.destroy()

    def create_widgets(self):
        notebook = ttk.Notebook(self.root)

        # Display Settings Tab
        display_frame = ttk.Frame(notebook)
        self.add_resolution_selector(display_frame)
        self.add_slider(display_frame, "GammaRamp", "Display", 1.0, 2.0, 0.01)
        self.add_checkboxes(display_frame, "Display", ["ForceAniso", "HiResTextures", "MotionBlur", "DepthOfField"])
        notebook.add(display_frame, text="Display")

        # Hardware Settings Tab
        hardware_frame = ttk.Frame(notebook)
        self.add_combobox(hardware_frame, "AdapterNumber", "Hardware", [0, 1, 2, 3, 4])
        notebook.add(hardware_frame, text="Hardware")

        # Graphics Settings Tab
        graphics_frame = ttk.Frame(notebook)
        self.add_combobox(graphics_frame, "ShadowMapLevel", "Settings", [0, 1, 2, 3])
        self.add_entry(graphics_frame, "Webcam", "Settings")
        notebook.add(graphics_frame, text="Graphics")

        # Sound Settings Tab
        sound_frame = ttk.Frame(notebook)
        self.add_combobox(sound_frame, "SpeakerSetup", "Sound", [0, 1, 2, 3, 4, 5])
        self.add_combobox(sound_frame, "HighQualFilters", "Sound", [0, 1])
        notebook.add(sound_frame, text="Sound")

        notebook.pack(expand=1, fill="both")

        save_btn = ttk.Button(self.root, text="Save Configuration", command=self.save_config)
        save_btn.pack(pady=10)

    def add_resolution_selector(self, parent):
        resolutions = [
            (512, 384), (640, 480), (800, 600), 
            (1024, 768), (1280, 720), (1920, 1080)
        ]
        current_width = int(self.config["Display"]["Width"])
        current_height = int(self.config["Display"]["Height"])
        resolution_frame = ttk.LabelFrame(parent, text="Display Resolution")
        ttk.Label(resolution_frame, text="Select Resolution:").pack(pady=5)
        self.res_var = tk.StringVar()
        res_combobox = ttk.Combobox(resolution_frame, 
                                   values=[f"{w}x{h}" for w, h in resolutions],
                                   textvariable=self.res_var)
        res_combobox.set(f"{current_width}x{current_height}")
        res_combobox.pack(pady=5)
        resolution_frame.pack(fill="x", padx=10, pady=5)

    def add_slider(self, parent, option, section, min_val, max_val, resolution):
        frame = ttk.LabelFrame(parent, text=option)
        current_val = float(self.config[section][option])
        var = tk.DoubleVar(value=current_val)
        slider = ttk.Scale(frame, 
                          from_=min_val,
                          to=max_val,
                          value=current_val,
                          orient="horizontal",
                          variable=var,
                          command=lambda v, s=section, o=option: 
                              self.config.set(s, o, f"{float(v):.3f}"))
        value_label = ttk.Label(frame, text=f"Current: {current_val}")
        slider.pack(padx=10, pady=5)
        value_label.pack()
        frame.pack(fill="x", padx=10, pady=5)

    def add_checkboxes(self, parent, section, options):
        frame = ttk.LabelFrame(parent, text=f"{section} Options")
        for option in options:
            var = tk.BooleanVar(value=self.config.getboolean(section, option))
            cb = ttk.Checkbutton(frame, 
                                text=option,
                                variable=var,
                                command=lambda v=var, s=section, o=option: 
                                    self.config.set(s, o, str(v.get()).lower()))
            cb.pack(anchor="w", padx=5, pady=2)
        frame.pack(fill="x", padx=10, pady=5)

    def add_combobox(self, parent, option, section, values):
        frame = ttk.LabelFrame(parent, text=option)
        ttk.Label(frame, text=f"{option}:").pack(pady=5)
        var = tk.StringVar(value=self.config[section][option])
        cb = ttk.Combobox(frame, values=values, textvariable=var)
        cb.pack(padx=10, pady=5)
        frame.pack(fill="x", padx=10, pady=5)
        # Update config when selection changes
        def update_config(event=None):
            self.config[section][option] = var.get()
        var.trace_add("write", lambda *args: update_config())

    def add_entry(self, parent, option, section):
        frame = ttk.LabelFrame(parent, text=option)
        ttk.Label(frame, text=f"{option}:").pack(pady=5)
        var = tk.StringVar(value=self.config[section][option])
        entry = ttk.Entry(frame, textvariable=var)
        entry.pack(padx=10, pady=5)
        frame.pack(fill="x", padx=10, pady=5)
        # Update config when text changes
        def update_config(event=None):
            self.config[section][option] = var.get()
        var.trace_add("write", lambda *args: update_config())

    def save_config(self):
        # Update resolution from selector
        width, height = map(int, self.res_var.get().split("x"))
        self.config.set("Display", "Width", str(width))
        self.config.set("Display", "Height", str(height))

        # Remove spaces around = and between lines
        config_string = ""
        for section in self.config.sections():
            config_string += f"[{section}]\n"
            for key, value in self.config.items(section):
                config_string += f"{key}={value}\n"
            config_string += "\n"

        with open(CONFIG_PATH, "w") as configfile:
            configfile.write(config_string)

        messagebox.showinfo("Success", "Configuration saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NFSTweakTool(root)
    root.geometry("600x500")
    root.mainloop()
