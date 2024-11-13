import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def is_palindrome(s):
    # Видаляємо пробіли та перетворюємо в нижній регістр для коректної перевірки
    s = ''.join(s.split()).lower()
    return s == s[::-1]

def submit(text):
    # Очищаємо область результатів
    result_ax.clear()
    result_ax.axis('off')
    # Перевіряємо, чи є введений текст паліндромом
    if is_palindrome(text):
        result = 'Це паліндром'
    else:
        result = 'Це не паліндром'
    # Відображаємо результат
    result_ax.text(0.5, 0.5, result, fontsize=14, ha='center', va='center')
    plt.draw()

# Створюємо фігуру та осі для текстового поля та результату
fig, (input_ax, result_ax) = plt.subplots(2, 1, figsize=(6, 4))
plt.subplots_adjust(hspace=0.5)

# Приховуємо осі
input_ax.axis('off')
result_ax.axis('off')

# Створюємо текстове поле для введення рядка на існуючій осі
text_box = TextBox(input_ax, 'Введіть рядок: ')
text_box.on_submit(submit)

plt.show()
