
#Общий класс Мебель
class Furniture:

    def __init__(self, fur_height, fur_width, fur_length, fur_color):
        self.fur_height = fur_height
        self.fur_width = fur_width
        self.fur_color = fur_color
        self.fur_length = fur_length

        self.fur_square = fur_square = fur_width * fur_length
        self.capacity = fur_square * fur_height


class Closet(Furniture):

    def __init__(self, fur_height, fur_width, fur_length, fur_color, wood_type):
        super().__init__(fur_height, fur_width, fur_length, fur_color)
        self.wood_type = wood_type

class Couch(Furniture):

    def __init__(self, fur_height, fur_width, fur_length, fur_color, ch_material):
        super().__init__(fur_height, fur_width, fur_length, fur_color)
        self.ch_material = ch_material

class Table(Furniture):

    def __init__(self, fur_height, fur_width, fur_length, fur_color, ty_appointment):
        super().__init__(fur_height, fur_width, fur_length, fur_color)
        self.ty_appointment = ty_appointment

