import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import serial
import threading


class FlipperZeroUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flipper Zero UI")
        self.setGeometry(100, 100, 400, 400)

        # Create a QLabel to display the live view
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setGeometry(50, 50, 300, 300)

        # Create a serial connection
        self.port = '/dev/ttyUSB0'  # Replace with the appropriate port name on your system
        self.baud_rate = 115200  # Replace with the baud rate supported by the Flipper Zero
        self.flipper_serial = serial.Serial(self.port, self.baud_rate)
        self.is_receiving = False

    def start_receiving(self):
        self.is_receiving = True
        while self.is_receiving:
            # Read image data from Flipper Zero and update the UI
            image_data = self.flipper_serial.read(1024)  # Adjust the buffer size according to your needs

            # Process the image_data and convert it to QPixmap format
            # You need to implement this part based on the format and encoding used by Flipper Zero

            # Update the image_label with the new QPixmap
            pixmap = QPixmap.fromImage(image_data)
            self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

    def closeEvent(self, event):
        # Stop the receiving thread and close the serial connection
        self.is_receiving = False
        self.flipper_serial.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    flipper_ui = FlipperZeroUI()
    flipper_ui.show()

    # Start a separate thread for receiving live view data
    receive_thread = threading.Thread(target=flipper_ui.start_receiving)
    receive_thread.start()

    sys.exit(app.exec_())
