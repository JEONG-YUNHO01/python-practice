## 인스턴스 변수

class Example:
    ## 초기자 인스턴스 변수 0을 초기화
    def __init__(self):
        self.num = 0

    ## 인스턴스 변수 num 을 출력
    def show_num(self):
        print(self.num)

    ## 인스턴스 변수 num 에 3을 더함
    def add_num(self):
        self.num = self.num + 3
    
    ## 인스턴스 변수 num 에 3을 뺌
    def subtract_num(self):
        self.num = self.num - 3 

e1 = Example() ## 인스턴스 생성

print("초기화된 인스턴스 변수 값")
e1.show_num()

print("인스턴스 변수 값을 변경(더하기)")
e1.add_num()
e1.show_num()

print("인스턴스 변수 값을 변경(빼기))")
e1.subtract_num()
e1.show_num()

"""
이렇게 코딩을 해도 문제는 없으나 하드 코딩이 될 가능성이 높아짐
ex) 특정값을 더하고 빼는 메서드가 존재하는 클래스에서 인스턴스마다 특정값을 변경할 경우 모든 인스턴스에 해당 특정값을 설정해야함

def add_num(self):
        self.num = self.num + 3

def subtract_num(self):
        self.num = self.num - 3

num에 더하거나 빼는 값 3을 변경하고 싶은 경우 양쪽 메서드를 같이 수정해야하는 번거로움 발생

그럴때 클래스 변수를 통해 해결하는 방향으로 가는 것이 좋음.
"""