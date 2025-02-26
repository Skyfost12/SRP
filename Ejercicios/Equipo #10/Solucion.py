class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night

class Guest:
    def __init__(self, guest_id, name, email):
        self.guest_id = guest_id
        self.name = name
        self.email = email
        
class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        
        def calculate_reservation_cost(reservation):
            nights = (reservation.check_out_date - reservation.check_in_date).days
            return reservation.room.price_per_night * nights


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []
        
    def find_available_rooms(hotel, check_in_date, check_out_date):
        reserved_rooms = set()
        for reservation in hotel.reservations:
            if not (reservation.check_out_date <= check_in_date or reservation.check_in_date >= check_out_date):
                reserved_rooms.add(reservation.room)
        return [room for room in hotel.rooms if room not in reserved_rooms]

