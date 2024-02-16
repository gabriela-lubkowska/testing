import pytest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from ui.main_window import MainWindow

@pytest.fixture
def app(qtbot):
    test_app = QApplication.instance()
    if test_app is None:
        test_app = QApplication(sys.argv)
    return test_app

@pytest.fixture
def main_window(app, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window

def test_ipv4_button(main_window, qtbot):
    expected_button_text = 'Moje IPv4'
    qtbot.mouseClick(main_window.buttons[expected_button_text], Qt.LeftButton)
    assert "Twoje IP:" in main_window.text_view.toPlainText()

def test_proxy_button(main_window, qtbot):
    expected_button_text = 'Sprawdź Proxy'
    qtbot.mouseClick(main_window.buttons[expected_button_text], Qt.LeftButton)
    assert "Proxy enabled:" in main_window.text_view.toPlainText() or "No proxy configured." in main_window.text_view.toPlainText()

def test_system_version_button(main_window, qtbot):
    expected_button_text = 'Wersja Systemu'
    qtbot.mouseClick(main_window.buttons[expected_button_text], Qt.LeftButton)
    assert "Wersja systemu:" in main_window.text_view.toPlainText()

def test_cpu_info_button(main_window, qtbot):
    expected_button_text = 'Informacje o CPU'
    qtbot.mouseClick(main_window.buttons[expected_button_text], Qt.LeftButton)
    assert "Liczba rdzeni:" in main_window.text_view.toPlainText()

def test_memory_info_button(main_window, qtbot):
    expected_button_text = 'Informacje o Pamięci'
    qtbot.mouseClick(main_window.buttons[expected_button_text], Qt.LeftButton)
    assert "RAM:" in main_window.text_view.toPlainText()

def test_host_name_button(main_window, qtbot):
    expected_button_text = 'Host Name'
    qtbot.mouseClick(main_window.buttons[expected_button_text], Qt.LeftButton)
    assert "Host name:" in main_window.text_view.toPlainText()