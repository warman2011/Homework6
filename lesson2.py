class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def Asphalt(self, height):
        print(self._lenght*self._width*0.025*height, 'т')


a = Road(1000, 20)
a.Asphalt(5)
