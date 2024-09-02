"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """
    Creation and behavior of alien
    """
    total_aliens_created = 0

    def __init__(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, other_object):
        pass


def new_aliens_collection(coordinate_list):
    """
    To create several aliens
    """
    alien_list = []
    for coordinate in coordinate_list:
        alien_list.append(Alien(coordinate[0], coordinate[1]))
    return alien_list
