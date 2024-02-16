import platform
import psutil

def get_system_version():
    return f'Wersja systemu: {platform.platform()}'

def get_cpu_info():
    cores = psutil.cpu_count(logical=True)
    if cores is None:
        return "Nie można określić liczby rdzeni."
    return f"Liczba rdzeni: {cores}"

def get_memory_info():
    ram = psutil.virtual_memory().total / (1024 ** 3)  # GB
    return f"RAM: {ram:.2f} GB"

def get_host_name():
    return f"Host name: {platform.node()}"