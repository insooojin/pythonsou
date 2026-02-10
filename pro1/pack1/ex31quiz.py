
# 다중 상속 연습문제2
# 클래스의 상속관계 연습문제 - 다형성
# ElecProduct의 sub class 두 개를 만들고 volumeControl()을 overriding 하여 다형성을 구현하시오.
class ElecProduct:
    volume = 0      

    def volumeControl(self, volume):
        # print(f'볼륨조절: {volume}')
        pass

class ElecTv(ElecProduct):
    def tv1(self):
        print('ElecTv 고유 메소드')
   
    def volumeControl(self, volume):
         # 계산
         print('금요일 와우')
         self.volume = volume
         print(f'ElecTv 볼륨을 조절한다: {volume}')
       
class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
         sori = volume
         print(f'ElecRadio 소리를 조절: {sori}')

product = ElecProduct()
tv = ElecTv()
# 다형성 처리하기
product = tv
product.volumeControl(5)
print()
radio = ElecRadio()
product = radio
product.volumeControl(3)

print('---------')
q1 = [ElecTv(), ElecRadio()]
for a in q1:
    a.volumeControl(2)
    print()

# 다중 상속 연습문제3

class Animal:

    def move(self):
        print('대부분의 동물들은 4발로 걸어요')

class Dog(Animal):
    # Field
    name = '개'

    # Method
    def move(self):
        print('댕댕이')


class Cat(Animal):
    
    # Field
    name = '고양이'

    # Method
    def move(self):
        print('냥냥이')


class Wolf(Dog, Cat):
    pass        


class Fox(Cat, Dog):
    
    #Method
    def move(self):
        print('여우')
    
    def foxMethod(self):
        print('Fox 고유 메소드')
        # pass를 쓰면 자식이 있다고 생각

animal = [Dog(), Cat(), Wolf(), Fox()]
for a in animal:
    print('-------'*10)
    print(a)      
    a.move()