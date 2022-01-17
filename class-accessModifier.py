## 클래스 접근 제한자

"""
Python 클래스는 기본적으로 모든 멤버가 퍼블릭이다.
내부적 사용 변수 혹은 메서드는 이름앞에 _를 붙이지만 퍼블릭은 아니다.
프라이빗 멤버를 구성하려면 __를 이름앞에 붙인다.
"""

class Example:
    def __init__(self):
        self.__no = 0
        ## private 메서드 를 인스턴스 초기화시 호출한다.
        self.__startPrint()
    def printExam(self):
        print(self.__no)

    def set_no(self, num):
        self.__no = num

    ## 프라이빗 메서드를 생성, 클래스 내부에서만 접근할 수 있다.
    def __startPrint(self):
        print(self.__no, "을 출력합니다. 이것은 프라이빗 메서드이므로 외부에서 접근할 수 없습니다.")

print("e1객체 생성")
e1 = Example()
# print(e1.__no) <- AttributeError: 'Example' object has no attribute '__no'
# 클래스 외부에서 접근할 수 없다.

## 클래스 내부에서 printExam 메서드를 통해 내부 __no 변수에 접근해서 값을 출력하는 방식으로 해결한다.
e1.printExam()

## 인스턴스 변수에 무분별한 접근 및 변경을 막기위한 set메서드 set_no을 통해서만 변경할 수 있는 방식으로 설정
e1.set_no(3)
e1.printExam()

# e1.__startPrint() <- AttributeError: 'Example' object has no attribute '__startPrint'
# 외부에서 접근할 수 없다.
print("e2객체 생성")
e2 = Example()

