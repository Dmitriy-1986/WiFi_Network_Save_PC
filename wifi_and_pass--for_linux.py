import os
import re

try:
    # Найти файлы конфигурации сети
    config_files = [f for f in os.listdir('/etc/NetworkManager/system-connections') if f.endswith('.nmconnection')]

    pass_wifi = ""

    for config_file in config_files:
        try:
            with open(os.path.join('/etc/NetworkManager/system-connections', config_file), 'r') as file:
                content = file.read()
                ssid_match = re.search(r'ssid=(.+)', content)
                if ssid_match:
                    ssid = ssid_match.group(1).strip('"')
                    psk_match = re.search(r'psk=(.+)', content)
                    if psk_match:
                        password = psk_match.group(1).strip('"')
                        pass_wifi += f"--------------------------------\n\nНазвание сети: {ssid}\nПароль: {password}\n\n"
        except Exception as e:
            print(f"Ошибка при получении пароля для сети из файла {config_file}: {e}")

    if not pass_wifi:
        print("Нет сохраненных паролей WiFi.")
    else:
        print(pass_wifi)

except Exception as ex:
    print(f'Ошибка: {ex}')
