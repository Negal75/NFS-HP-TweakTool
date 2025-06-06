# NFS: Hot Pursuit Configurator

[![Screenshot of the Configurator](https://github.com/Negal75/NFS-HP-TweakTool/blob/main/screenshot.jpg?raw=true)](https://github.com/YOUR_USERNAME/NFS-Hot-Pursuit-Configurator)

## Description

This Python application provides a user-friendly graphical interface for modifying the configuration file (`config.NFS11Save`) of Need for Speed: Hot Pursuit (2010). Instead of manually editing the often cryptic configuration file, this tool allows you to adjust settings like resolution, graphics quality, sound options, and more with intuitive sliders, checkboxes, and dropdown menus.

## Features

* **Intuitive GUI:** A clean and easy-to-use interface built with Tkinter.
* **Tabbed Interface:** Settings are organized into logical tabs (Display, Hardware, Graphics, Sound).
* **Common Settings:** Control over key settings including:
    * Resolution
    * Gamma Ramp
    * Anisotropic Filtering
    * Motion Blur
    * Depth of Field
    * Adapter Number
    * Shadow Map Level
    * Speaker Setup
    * High Quality Filters
* **Real-time Preview (Limited):** Some settings, like Gamma Ramp, are immediately reflected in the GUI.
* **Clean Config File Output:** Saves the configuration file in a standardized format *without* unnecessary whitespace.
* **Error Handling:** Checks for the existence of the configuration file and displays an error message if it's not found.

## Usage

1. Launch the application.
2. Adjust the settings using the provided controls.
3. Click the "Save Configuration" button.
4. The `config.NFS11Save` file in your Need for Speed: Hot Pursuit directory will be updated.  **Important: Back up your original `config.NFS11Save` file before making changes!**

## Contributing

Contributions are welcome!  If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

*   This project was inspired by the need for a more user-friendly way to configure Need for Speed: Hot Pursuit.
*   Thanks to the Need for Speed community for their support and feedback.
