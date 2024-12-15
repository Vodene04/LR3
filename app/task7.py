class Pyramid:
    def __init__(self, base_area: float, height: float):
        self.__base_area = base_area #площадь
        self.__height = height #высота

    # получение значения площади
    @property
    def base_area(self):
        return self.__base_area

    # получение значения высоты
    @property
    def height(self):
        return self.__height

    # задание значения площади
    @base_area.setter
    def base_area(self, input_base_area: float):
        self.__base_area = input_base_area

    # задание значения высоты
    @height.setter
    def height(self, input_height: float):
        self.__height = input_height

    @staticmethod
    def about():
        return "Команда из 3 разработчиков: реализуем программу для расчета объема правильной пирамиды."