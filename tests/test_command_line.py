import subprocess
import pytest

TEST_CASES = [
    ('help', ['Dostępne argumenty:']),
    ('moje_ipv4', ['Twoje IP:']),
    ('sprawdz_proxy', ['Proxy enabled:', 'No proxy configured.']),
    ('wersja_systemu', ['Wersja systemu:']),
    ('informacje_o_cpu', ['Liczba rdzeni:']),
    ('informacje_o_pamieci', ['RAM:']),
    ('host_name', ['Host name:'])
]

@pytest.mark.parametrize("arg,expected_outputs", TEST_CASES)
def test_app_with_args(arg, expected_outputs):
    result = subprocess.run(['python', './main.py', arg], capture_output=True, text=True)
    stdout = result.stdout
    stderr = result.stderr

    assert any(expected_output in stdout for expected_output in expected_outputs), f"Oczekiwano, że argument '{arg}' wywoła odpowiedź zawierającą jedno z '{expected_outputs}', ale otrzymano: {stdout}"

    if stderr:
        pytest.fail(f"Wystąpił błąd podczas wykonania testu dla argumentu '{arg}': {stderr}")

