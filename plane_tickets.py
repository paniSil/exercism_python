"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    letters = ['A', 'B', 'C', 'D']
    for num in range(number):
        yield letters[num % 4]


def generate_seats(number):
    seats = generate_seat_letters(number)
    row = 0
    for seat in seats:
        if seat == 'A':
            row += 1
        if row == 13:
            row += 1
        yield str(row) + seat


def assign_seats(passengers):

    seated_passengers = {}

    seats = generate_seats(len(passengers))
    for passenger in passengers:
        seated_passengers[passenger] = next(seats)
    return seated_passengers


def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        code = seat + flight_id
        while len(code) < 12:
            code += '0'
        yield code
