class IdolGroup:
    def __init__(self, name, cnt, sex):
        self.group_name = name
        self.people_cnt = cnt
        self.sex = sex

    def show_info(self):
        if self.sex == "male":
            sex = "남성"
        elif self.sex == "female":
            sex = "여성"
        else:
            sex = "혼성"
        
        print("그룹명은 " + self.group_name + "이고, 인원수는 " + str(self.people_cnt) + "명의 " + sex + "그룹 입니다.")

class GirlGroup(IdolGroup):
    def __init__(self, name, cnt, member):
        super().__init__(name, cnt, "female")
        self.member = member

    ## 메서드 오버라이딩
    def show_info(self):
        super().show_info()
        print("멤버는 " + ', '.join(s for s in self.member))

class BoyGroup(IdolGroup):
    def __init__(self, name, cnt, member):
        super().__init__(name, cnt, "male")
        self.member = member

bts = BoyGroup("bts", 7, ["지민", "뷔", "RM", "정국", "제이홉", "슈가", "진"])
소녀시대 = GirlGroup("소녀시대", 8, ["효연", "윤아", "태연", "티파니", "수영", "유리", "써니", "서현"])

## IdolGroup 클래스의 상속클래스 BoyGroup에서 show_info()를 호출
## IdolGroup 클래스의 메서드 show_info()를 호출
print("부모클래스 메서드 호출")
bts.show_info()

## IdolGroup 클래스의 상속클래스 GirlGroup에서 show_info()를 호출
## 상속된 클래스 GirlGroup에서 재정의한 show_info()가 호출됨
print("자식클래스에서 오버라이딩된 메서드 호출")
소녀시대.show_info()