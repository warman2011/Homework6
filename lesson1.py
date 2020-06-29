from time import sleep

class TrafficLight():

    __color = ('Red', 'Yellow', 'Green')

    def running(self):
        """Run TrafficLite"""
        print(self.__color[0])
        sleep(7)
        print(self.__color[1])
        sleep(2)
        print(self.__color[2])
        sleep(5)
        print('Все лампочки перегорели!!!')


a = TrafficLight()
a.running()
# print(a.__color)




