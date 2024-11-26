import csv
import re
from collections import defaultdict

# Функция для стандартизации номеров телефонов
def clean_phone_number(phone):
    pattern = re.compile(
        r"(\+7|8)?\s*\(?(\d{3})\)?[-.\s]*(\d{3})[-.\s]*(\d{2})[-.\s]*(\d{2})(?:\s*доб\.\s*(\d+))?"
    )
    return pattern.sub(r"+7(\2)\3-\4-\5 доб.\6" if "доб." in phone else r"+7(\2)\3-\4-\5", phone).strip()

# Функция для обработки адресной книги
def process_phonebook(input_path, output_path):
    # Читаем исходный файл
    with open(input_path, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # Используем словарь для объединения дубликатов
    contacts_dict = defaultdict(lambda: ["", "", "", "", "", "", ""])

    # Обрабатываем записи
    for contact in contacts_list:
        # Объединяем и разбиваем ФИО
        full_name = " ".join(contact[:3]).split()
        lastname = full_name[0] if len(full_name) > 0 else ""
        firstname = full_name[1] if len(full_name) > 1 else ""
        surname = full_name[2] if len(full_name) > 2 else ""

        # Чистим телефон
        phone = clean_phone_number(contact[5]) if contact[5] else ""

        # Ключ - Фамилия и Имя
        key = (lastname, firstname)
        existing_entry = contacts_dict[key]

        # Объединяем данные
        contacts_dict[key] = [
            lastname or existing_entry[0],
            firstname or existing_entry[1],
            surname or existing_entry[2],
            contact[3] or existing_entry[3],
            contact[4] or existing_entry[4],
            phone or existing_entry[5],
            contact[6] or existing_entry[6],
        ]

    # Преобразуем словарь обратно в список
    cleaned_contacts_list = [list(contact) for contact in contacts_dict.values()]

    # Сохраняем очищенные данные
    with open(output_path, "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(cleaned_contacts_list)

# Указываем пути к файлам
input_file = "phonebook_raw.csv"
output_file = "phonebook.csv"

# Обрабатываем адресную книгу
process_phonebook(input_file, output_file)

print(f"Файл успешно обработан и сохранен в {output_file}")