
#Общий класс Мебель
class Furniture:

    def __init__(self, fur_height, fur_width, fur_length, fur_color, fur_square, fur_capacity):
        self.fur_height = fur_height
        self.fur_width = fur_width
        self.fur_color = fur_color
        self.fur_square = fur_square
        self.fur_capacity = fur_capacity
        self.fur_length = fur_length

        fur_square = fur_width * fur_length
        fur_capacity = fur_square * fur_height


class Closet(Furniture):

    def __init__(self, fur_height, fur_width, fur_length, fur_color, fur_square, fur_capacity,wood_type):
        super().__init__(self, fur_height, fur_width, fur_length, fur_color, fur_square, fur_capacity)
        self.wood_type = wood_type

class Couch(Furniture):

    def __init__(self, fur_height, fur_width, fur_length, fur_color, fur_square, fur_capacity, ch_material):
        super().__init__(self, fur_height, fur_width, fur_length, fur_color, fur_square, fur_capacity)
        self.ch_material = ch_material

class Table(Furniture):

    def __init__(self, fur_height, fur_width, fur_length, fur_color, fur_square, fur_capacity, ty_appointment):
        super().__init__(self, fur_height, fur_width, fur_length, fur_color, fur_square, fur_capacity)
        self.ty_appoinment = ty_appointment
