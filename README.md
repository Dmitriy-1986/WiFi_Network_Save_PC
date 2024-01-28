# WiFi_Network_Save_PC / Получение данных wifi сети
 Получение название сети и паролей сохраненных на компьютере
```python
import subprocess

try:
    data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')
    profiles = [i.split(":")[1].strip() for i in data if "Все профили пользователей" in i]
    pass_wifi = ""

    for i in profiles:
        if i.strip():
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')
                for j in results:
                    if "Содержимое ключа" in j:
                        password = j.split(':')[1].strip()
                        pass_wifi += f"--------------------------------\n\nНазвание сети: {i} \nПароль: {password}\n\n"
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при получении пароля для профиля {i}: {e}")

    if not pass_wifi:
        print("Нет сохраненных паролей WiFi.")
    else:
        print(pass_wifi)

except Exception as ex:
    print(f'Ошибка: {ex}')
```
