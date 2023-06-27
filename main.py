import os


n = os.getenv('N')

if n is None:
    print("Змінна оточення N не задана.")
else:
    with open('шлях_до_файлу', 'r') as file:
        content = file.read()

        count = len(content)

        print(f"Кількість символів у рядку файлу: {count}")