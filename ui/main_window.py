from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from functions.network import get_ip_address, check_proxy
from functions.system_info import get_system_version, get_cpu_info, get_memory_info, get_host_name

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MyTest App')
        self.setGeometry(100, 100, 800, 600)
        self.buttons = {}  # Dodajemy słownik przechowujący przyciski
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        layout.addWidget(self.text_view)
        
        # Zdefiniowanie stylu przycisku
        button_style = "background-color: yellow; font-size: 16px;"
        
        buttons = {
            'Moje IPv4': self.show_ip,
            'Sprawdź Proxy': self.show_proxy,
            'Wersja Systemu': self.show_system_version,
            'Informacje o CPU': self.show_cpu_info,
            'Informacje o Pamięci': self.show_memory_info,
            'Host Name': self.show_host_name
        }
        
        for btn_text, btn_action in buttons.items():
            btn = QPushButton(btn_text)
            btn.clicked.connect(btn_action)
            btn.setStyleSheet(button_style)  # Stosowanie zdefiniowanego stylu
            layout.addWidget(btn)
            self.buttons[btn_text] = btn  # Dodajemy przyciski do słownika
        
        central_widget.setLayout(layout)
    
    def show_ip(self, cli_mode=False):
        result = get_ip_address()
        if cli_mode:
            return result
        self.text_view.setText(result)

    def show_proxy(self, cli_mode=False):
        result = check_proxy()
        if cli_mode:
            return result
        self.text_view.setText(result)

    def show_system_version(self, cli_mode=False):
        result = get_system_version()
        if cli_mode:
            return result
        self.text_view.setText(result)

    def show_cpu_info(self, cli_mode=False):
        result = get_cpu_info()
        if cli_mode:
            return result
        self.text_view.setText(result)

    def show_memory_info(self, cli_mode=False):
        result = get_memory_info()
        if cli_mode:
            return result
        self.text_view.setText(result)

    def show_host_name(self, cli_mode=False):
        result = get_host_name()
        if cli_mode:
            return result
        self.text_view.setText(result)