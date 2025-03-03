# hotel.py
from typing import List
from room import Room

class Hotel:
    """Отель"""

    def __init__(self):
        self.rooms: List[Room] = [] # Список всех номеров

    # Метод добавляет новый номер в отель
    def add_room(self, room: Room):
        self.rooms.append(room)
        print(f"Номер {room.number} добавлен к отелю")

    # Метод находит номер по его номеру
    def find_room_by_number(self, number: int) -> Room:
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    # Метод возвращает список свободных номеров
    def available_rooms(self) -> List[Room]:
        return [room for room in self.rooms if room.is_available()]

    # Метод находит номера с заданной вместимостью
    def find_rooms_by_capacity(self, capacity: int) -> List[Room]:
        return [room for room in self.rooms if room.max_guests >= capacity]