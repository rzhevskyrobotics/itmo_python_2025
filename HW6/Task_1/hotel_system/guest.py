from room import Room

class Guest:
    """Гость"""

    def __init__(self, name: str, phone: str):
        self.name = name                # Имя гостя
        self.phone = phone              # Номер телефона
        self._reservation_id = None     # Идентификатор бронирования

    # Метод бронирует номер для гостя
    def book_room(self, room: Room):
        if room.is_available():
            room.book()
            self._reservation_id = room.number
            print(f"{self.name} забронировал номер {self._reservation_id}.")
        else:
            print(f"Номер {room.number} недоступен для бронирования.")

    # Метод отменяет бронирование
    def cancel_reservation(self, room: Room):
        if self._reservation_id == room.number:
            room.release()
            self._reservation_id = None
            print(f"{self.name}'s бронирование номера {room.number} было отменено.")
        else:
            print("Ваше бронирование не найдено.")