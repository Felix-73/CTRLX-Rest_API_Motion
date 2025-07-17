from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
from api.client import ApiClient

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("REST API Client")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.ip_input = QLineEdit(self)
        self.ip_input.setPlaceholderText("Enter IP Address")
        self.ip_input.setText("192.168.1.1")  # Valeur par défaut
        self.layout.addWidget(self.ip_input)

        self.axis_input = QLineEdit(self)
        self.axis_input.setPlaceholderText("Enter Axis Name")
        self.axis_input.setText("Axis_1")  # Valeur par défaut
        self.layout.addWidget(self.axis_input)

        self.position_input = QLineEdit(self)
        self.position_input.setPlaceholderText("Enter Position")
        self.layout.addWidget(self.position_input)

        self.vel_input = QLineEdit(self)
        self.vel_input.setPlaceholderText("Enter Velocity")
        self.layout.addWidget(self.vel_input)

        self.acc_input = QLineEdit(self)
        self.acc_input.setPlaceholderText("Enter Acceleration")
        self.layout.addWidget(self.acc_input)

        self.dec_input = QLineEdit(self)
        self.dec_input.setPlaceholderText("Enter Deceleration")
        self.layout.addWidget(self.dec_input)

        self.power_state = False  # Initial state
        self.power_button = QPushButton("Toggle Power", self)
        self.power_button.clicked.connect(self.toggle_power)
        self.layout.addWidget(self.power_button)

        self.move_button = QPushButton("Move Absolute", self)
        self.move_button.clicked.connect(self.activate_move_absolute)
        self.layout.addWidget(self.move_button)

        self.reset_button = QPushButton("Reset Axis Error", self)
        self.reset_button.clicked.connect(self.activate_reset_error)
        self.layout.addWidget(self.reset_button)

        self.io_name_input = QLineEdit(self)
        self.io_name_input.setPlaceholderText("Enter IO Name")
        self.io_name_input.setText("XI211116")  # Valeur par défaut
        self.layout.addWidget(self.io_name_input)

        self.rainbow_button = QPushButton("Rainbow", self)
        self.rainbow_button.clicked.connect(self.activate_rainbow)
        self.layout.addWidget(self.rainbow_button)


        self.response_label = QLabel(self)
        self.layout.addWidget(self.response_label)

        self.central_widget.setLayout(self.layout)

    def create_api_client(self):
        ip_address = self.ip_input.text()
        axis_name = self.axis_input.text()
        return ApiClient(ip_address, axis_name)

    def toggle_power(self):
        api_client = self.create_api_client()
        self.power_state = not self.power_state  # Toggle the state
        response = api_client.power(self.power_state)
        self.response_label.setText(response)

    def activate_move_absolute(self):
        api_client = self.create_api_client()
        axs_pos = float(self.position_input.text())
        vel = float(self.vel_input.text())
        acc = float(self.acc_input.text())
        dec = float(self.dec_input.text())
        response = api_client.move_absolute(axs_pos, vel, acc, dec)
        self.response_label.setText(response)

    def activate_reset_error(self):
        api_client = self.create_api_client()
        response = api_client.reset_error()
        self.response_label.setText(response)

    def activate_rainbow(self):
        api_client = self.create_api_client()
        response = api_client.rainbow(self.io_name_input.text())
        self.response_label.setText(response)