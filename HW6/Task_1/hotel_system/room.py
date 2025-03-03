class Room:
    """Номер"""

    def __init__(self, number: int, room_type: str, max_guests: int, price_per_night: float):
        self.number = number                   # Номер комнаты
        self._type = room_type                 # Тип номера
        self.max_guests = max_guests           # Максимальное количество людей, которое может разместиться в номере
        self.price_per_night = price_per_night # Стоимость за сутки
        self._availability = True              # Доступность номера

    # Метод бронирует номер, если он доступен
    def book(self):
        if self._availability:
            self._availability = False
            print(f"Номер {self.number} был забронирован.")
        else:
            print(f"Номер {self.number} Номер уже забронирован другим человеком.")

    # Метод освобождает номер
    def release(self):
        self._availability = True
        print(f"Номер {self.number} был освобождён.")

    # Метод проверяет, доступен ли номер
    def is_available(self) -> bool:
        return self._availability

    # Метод получает тип номера
    def get_type(self) -> str:
        return self._type

class Luxury(Room):
    """Номер Люкс"""

    def __init__(self, number: int, max_guests: int, price_per_night: float, has_balcony: bool, has_mini_bar: bool):
        super().__init__(number, "Luxury", max_guests, price_per_night)
        self.has_balcony = has_balcony    # Наличие балкона
        self.has_mini_bar = has_mini_bar  # Наличие мини-бара

    # Метод добавляет возможность указать дополнительные пожелания при бронировании
    def book(self, special_requests: str = ""):
        super().book()
        if special_requests:
            print(f"Особые пожелания при бронировании номера {self.number}: {special_requests}")


class Standard(Room):
    """Номер Стандарт"""

    def __init__(self, number: int, max_guests: int, price_per_night: float, bed_count: int):
        super().__init__(number, "Standard", max_guests, price_per_night)
        self.bed_count = bed_count  # Количество кроватей

    # Метод добавляет логику для уборки после освобождения номера
    def release(self):
        super().release()
        print(f"Уборка помещения {self.number} после освобождения.")


class Economy(Standard):
    """Номер Эконом"""

    def __init__(self, number: int, max_guests: int, price_per_night: float, bed_count: int):
        super().__init__(number, max_guests, price_per_night, bed_count)

    # Метод учитывает количество выезжающих постояльцев
    def release(self, guest_count: int):
        if guest_count < self.max_guests:
            print(f"{guest_count} гостей покинули номер {self.number}. Осталось гостей: {self.max_guests - guest_count}")
        else:
            super().release()