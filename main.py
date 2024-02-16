import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow  # Zakładam, że MainWindow jest zdefiniowane w ui.main_window

def print_help():
    help_text = """
Dostępne argumenty:
help - wyświetla ten komunikat
moje_ipv4 - wyświetla adres IP komputera
sprawdz_proxy - informuje, czy jest uruchomione proxy
wersja_systemu - wyświetla wersję systemu operacyjnego
informacje_o_cpu - wyświetla informacje o CPU
informacje_o_pamieci - wyświetla informacje o pamięci RAM
host_name - wyświetla nazwę hosta
"""
    print(help_text)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == 'help':
            print_help()
        else:
            action_map = {
                'moje_ipv4': window.show_ip,
                'sprawdz_proxy': window.show_proxy,
                'wersja_systemu': window.show_system_version,
                'informacje_o_cpu': window.show_cpu_info,
                'informacje_o_pamieci': window.show_memory_info,
                'host_name': window.show_host_name
            }
            action = action_map.get(arg)
            if action:
                print(action(cli_mode=True))
            else:
                print("Nieznany argument. Użyj 'help' dla listy dostępnych argumentów.")
        return
    else:
        window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()