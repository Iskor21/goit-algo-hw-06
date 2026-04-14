from collections import UserDict

# для запису полів
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# валідація номера
class Phone(Field):
    def __init__(self, value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Телефон має містити рівно 10 цифр")
        super().__init__(value)

class Name(Field):
    def __init__(self, value: str):
        super().__init__(value)

#Додавання телефонів. Видалення телефонів. Редагування телефонів. Пошук телефону.
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
            else:
                raise f"Телефон {phone} не знайдено"

    def find_phone(self, number):
        for phone in self.phones:
            if  phone.value == number:
                return phone
        return None

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
            return new_phone
        else:
            raise ValueError(f"Телефон {old_phone} не знайдено")


    def __str__(self):
        phones = "; ".join(str(p) for p in self.phones) if self.phones else "-"
        return f"Contact name: {self.name.value}, phones: {phones}"


#Додавання записів. Пошук записів за іменем. Видалення записів за іменем.
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name: Record):
        if name in self.data:
            del self.data[name]
            print(f"Запис {name} видалено.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print("=== Вивід книги ===")
print(book)

# Знаходження та редагування телефону для John
print("\n=== Редагування ===")
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
print("\n=== Пошук ===")
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
print("\n=== Видалення ===")
book.delete("Jane")

# Виведення всіх записів у книзі
print("\n=== Вивід книги ===")
print(book)

