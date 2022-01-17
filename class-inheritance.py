class Parent:
    def __init__(self):
        self.example = "부모 클래스"

class Child01(Parent):
    ## 자식에서 인스턴스 변수 초기화
    def __init__(self):
        ## 부모의 인스턴스 변수를 상속하는 슈퍼클래스
        super().__init__() # 부모의 초기자 실행 후 자식의 인스턴스 변수 설정
        self.content = "자식 클래스 01"

class Child02(Parent):
    ## 자식에서 인스턴스 변수 초기화
    def __init__(self):
        ## 부모의 인스턴스 변수를 상속하는 슈퍼클래스
        super().__init__() # 부모의 초기자 실행 후 자식의 인스턴스 변수 설정
        self.content = "자식 클래스 02"

## 부모 객체 p1 생성
p1 = Parent()

## 자식 객체 c1 생성
c1 = Child01()
c2 = Child02()

## 부모 클래스의 인스턴스 변수 example와 자식의 content 에 접근 및 출력
print(p1.example)
print(c1.example, c1.content)
print(c2.example, c2.content)

## 부모 클래스에서 생성한 객체에서 자식의 변수를 사용할 수 있을까?

# print(p1.content) <- AttributeError: 'Parent' object has no attribute 'content'
# 부모의 클래스에는 content라는 attribute를 갖고 있지 않는다고 나옴
