from hotel import Hotel
from room import Luxury, Standard, Economy
from guest import Guest

# Запускаем нашу программу
if __name__ == "__main__":

    # Создаем отель
    hotel = Hotel()

    # Добавляем номера
    hotel.add_room(Luxury(101, 2, 200, True, True))
    hotel.add_room(Standard(102, 3, 150, 2))
    hotel.add_room(Economy(103, 4, 100, 4))

    # Создаем гостей
    guest1 = Guest("Иван Троянов", "+79008889988")
    guest2 = Guest("Михаил Попов", "+79001112233")

    # Гость 1 бронирует номер
    guest1.book_room(hotel.find_room_by_number(101))

    # Гость 2 пытается забронировать уже занятый номер
    guest2.book_room(hotel.find_room_by_number(101))

    # Гость 2 бронирует другой номер
    guest2.book_room(hotel.find_room_by_number(102))

    # Показываем свободные номера
    print("\nСвободные номера:")
    for room in hotel.available_rooms():
        print(f"Номер {room.number}, Тип: {room.get_type()}")

    # Гость 1 отменяет бронирование
    guest1.cancel_reservation(hotel.find_room_by_number(101))

    # Гость 2 освобождает номер
    guest2.cancel_reservation(hotel.find_room_by_number(102))