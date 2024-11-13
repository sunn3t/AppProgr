import re
from datetime import datetime

input_file = 'dgsd.txt'
output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Регулярні вирази для пошуку дат і підкреслень
date_pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
underscore_pattern = r'_{2}\._{2}\._{4}'

# Знаходимо всі дати у тексті
dates_found = re.findall(date_pattern, text)

# Поточна дата у форматі dd.mm.yyyy
current_date = datetime.now().strftime('%d.%m.%Y')

# Замінюємо підкреслення на поточну дату
updated_text = re.sub(underscore_pattern, current_date, text)

# Зберігаємо оновлений текст у файл
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(updated_text)

# Виводимо знайдені дати
print("Знайдені дати у тексті:")
for date in dates_found:
    print(date)
