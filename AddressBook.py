from collections import UserDict

# Базове поле
class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


# Ім'я контакту
class Name(Field):
    def __init__(self, value: str):
        if not value.strip():
            raise ValueError("Ім'я не може бути порожнім")
        if not value.isalpha():
            raise ValueError("Ім'я має містити лише літери")
        super().__init__(value)


# Телефон з валідацією
class Phone(Field):
    def __init__(self, value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Телефон має містити рівно 10 цифр")
        super().__init__(value)


# Запис контакту
class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str):
        for p in self.phones:
            if p.value == phone_number:
                self.phones.remove(p)
                return
        raise ValueError(f"Телефон {phone_number} не знайдено")

    def edit_phone(self, old_number: str, new_number: str):
        if not new_number.isdigit() or len(new_number) != 10:
            raise ValueError("Новий телефон має містити рівно 10 цифр")
        for p in self.phones:
            if p.value == old_number:
                p.value = new_number
                return
        raise ValueError(f"Телефон {old_number} не знайдено")

    def find_phone(self, phone_number: str):
        for p in self.phones:
            if p.value == phone_number:
                return p
        return None

    def __str__(self):
        phones = "; ".join(str(p) for p in self.phones) if self.phones else "-"
        return f"{self.name.value} | Телефон(и): {phones}"


# Адресна книга
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


# --- Тест ---
book = AddressBook()

john = Record(Name("John"), Phone("1234567890"))
john.add_phone("0987654321")
book.add_record(john)

ira = Record(Name("Ira"))
ira.add_phone("1111111111")
book.add_record(ira)

print("=== Вивід книги ===")
print(book)

print("\n=== Пошук ===")
found = book.find("John")
print(found)

print("\n=== Редагування ===")
ira.edit_phone("1111111111", "2222222222")
print(ira)

print("\n=== Видалення ===")
book.delete("John")
print(book)