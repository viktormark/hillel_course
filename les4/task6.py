# Створіть багаторівневий словник subjects навчальних предметів.
# Використайте наступні рядки для ключів верхнього рівня: 'science', 'humanities' і 'public'.
# Зробіть так, щоб ключ 'science' був ім’ям іншого словника, який має ключі 'physics', 'computer science' і 'biology'.
# Зробіть так, щоб ключ 'physics' посилався на список рядків зі значеннями 'nuclear physics', 'optics' і 'thermodynamics'.
# Решта ключів повинні посилатися на порожні словники. Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics'].



subjects = {}
subjects['science'] = {}
subjects['science']['physics'] = ['nuclear physics', 'optics', 'thermodynamics']
subjects['science']['computer science'] = {}
subjects['science']['biology'] = {}
subjects['humanities'] = {}
subjects['public'] = {}
print(subjects)
print(subjects['science'].keys())
print(subjects['science']['physics'])