## 파일 읽기

f = open('example.txt', 'r')
lines = f.readlines()
for i in lines:
    # 파일을 읽을 때 각 줄의 요소를 리스트로 반환하기에 i는 \n을 포함하고 있다.
    # 줄바꿈 문자를 제거하기 위해 strip 함수를 사용한다.
    line = i.strip()
    print(line)
f.close()


"""
파일을 열고 닫는 것을 편하게 처리하기 위해 with문을 사용할 수도 있다.
with open('example.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        line = i.strip()
        print(line)
"""