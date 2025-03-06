from datetime import date

#Clase que representa una habitación
class Room:
    #Constructor
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night

#Clase que representa un huésped
class Guest:
    #Constructor
    def __init__(self, guest_id, name, email):
        self.guest_id = guest_id
        self.name = name
        self.email = email

#Clase que representa una reserva       
class Reservation:
    #Constructor
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        
    #Calcular el costo 
    def calculate_reservation_cost(reservation):
        nights = (reservation.check_out_date - reservation.check_in_date).days
        return reservation.room.price_per_night * nights

#Clase que representa un hotel
class Hotel:
    #Constructor
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []
        
    #Buscar habitaciones disponibles
    def find_available_rooms(hotel, check_in_date, check_out_date):
        reserved_rooms = set()
        for reservation in hotel.reservations:
            if not (reservation.check_out_date <= check_in_date or reservation.check_in_date >= check_out_date):
                reserved_rooms.add(reservation.room)
        return [room for room in hotel.rooms if room not in reserved_rooms]
    

#Prueba
#Instanciamos algunas clases
#Hotel
hotel = Hotel("Hotel Plaza")

#Habitaciones
room1 = Room(1, "Sencilla", 100)
room2 = Room(2, "Doble", 200)
room3 = Room(3, "Suite", 300)

#Agregamos las habitaciones
hotel.rooms.extend([room1, room2, room3])

#Huesped
guest = Guest("G001", "Juan Pérez", "juan.perez@example.com")

#Registramos la reserva para el invitado en la habitación 101
check_in_date = date(2025, 3, 1)
check_out_date = date(2025, 3, 5)
reservation = Reservation("R001", guest, room1, check_in_date, check_out_date)
hotel.reservations.append(reservation)

#Calculamos el costo de la reserva
cost = reservation.calculate_reservation_cost()
print(f"Costo de la reserva (Reserva {reservation.reservation_id}): ${cost}")

# Buscar habitaciones disponibles para las mismas fechas
available_rooms = hotel.find_available_rooms(check_in_date, check_out_date)
print("\nHabitaciones disponibles para las fechas seleccionadas:")
for room in available_rooms:
    print(f"Habitación {Room(room).room_number} - Tipo: {Room(room).room_type} - Precio por noche: ${Room(room).price_per_night}")