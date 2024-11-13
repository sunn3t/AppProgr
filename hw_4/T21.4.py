import re
from datetime import datetime

input_file = 'dgsd.txt'
output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

date = r'\b\d{2}\.\d{2}\.\d{4}\b'
underscore_p = r'_{2}\._{2}\._{4}'

dates_found = re.findall(date, text)
current_date = datetime.now().strftime('%d.%m.%Y')
updated_text = re.sub(underscore_p, current_date, text)
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(updated_text)

print("Знайдені дати у тексті:")
for date in dates_found:
    print(date)
