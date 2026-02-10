class Car:
    handle = 1
    speed = 0

    def __init__(self, name, speed):
        self.name = name        # 현재 객체의 name(지역변수)에게 인자값 치환
        self.speed = speed

    def showData(self):     # class의 method는 반드시 self값을 가지고 있어야함
        km = "킬로미터"
        msg = "속도: " + str(self.speed) + km
        return msg
    
    def printHandle(self):
        return self.handle      # class 내의 멤버를 찾을 땐 self.멤버
    
print(Car.handle)       # 원형(prototype) 클래스의 멤버 호출
car1 = Car('tom', 10)   # 생성자 호출 후 객체 생성(인스턴스화)
print('car1 객체 주소: ', car1)
print('car1: ', car1.name, ' ', 'car1.speed: ', car1.speed, car1.handle)        # 지역에서 없으면 원형클래스를 참조, 원형클래스에도 없으면 error
car1.color = '파랑'     # 객체에 추가
print('car1.color: ',car1.color)

car2 =Car('john', 20)       # 생성자 호출 후 객체 생성(인스턴스화) 
print('car2 객체 주소: ', car2) 
print('car2: ', car2.name, ' ', 'car2.speed: ', car2.speed, car2.handle) 
# print(Car.color, ' ', car2.color)
print(id(Car), id(car1), id(car2))  # 각 객체는 다른 메모리 주소를 가짐
print(car1.__dict__)
print(car2.__dict__)


print('--메소드----')
print('car1 speed: ', car1.showData())      # car1.showData(car1)과 같은 의미이지만 인터프리터가 대신 해주기 때문에 생략해야한다-> 직접 쓰면 error
print('car2 speed: ', car2.showData())
car1.speed = 80
car2.speed = 110
print('car1 speed: ', car1.showData())     
print('car2 speed: ', car2.showData())

print('carr1 handle: ', car1.printHandle())
print('carr2 handle: ', car2.printHandle())


