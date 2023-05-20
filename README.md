# Flipper Zero UI Application

This Python application provides a graphical user interface (GUI) that displays the UI of a Flipper Zero device and provides live viewing. It utilizes the `PyQt5` library to create the GUI and the `pyserial` library to establish communication with the Flipper Zero device.

## Prerequisites

- Python 3.x
- PyQt5 library (`pip install PyQt5`)
- pyserial library (`pip install pyserial`)

## How to Use

1. Connect your Flipper Zero device to your computer via USB.
2. Open the `main.py` file in a Python editor or IDE.
3. Modify the `port` and `baud_rate` variables in the code to match the appropriate values for your system and Flipper Zero device.
4. Run the `main.py` file to start the application.

## Functionality

- The application creates a GUI window that displays the UI of the Flipper Zero device.
- It establishes a serial connection with the Flipper Zero device using the specified port and baud rate.
- The live view from the Flipper Zero device is continuously received and displayed in the GUI.
- The application runs until the GUI window is closed.
- The serial connection is closed and resources are released upon closing the GUI window.

## Customization

- The code provided is a basic template that you can modify and extend based on your specific requirements.
- You need to implement the logic for reading and processing the image data according to the format and encoding used by the Flipper Zero device.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or create an issue in the GitHub repository.

## License

This code is licensed under the [APACHE License](LICENSE).
