## 파일 쓰기

f = open('example.txt', 'w')
for i in range(3):
    f.write(str(i + 1) + "번 예시입니다.\n")
f.close()

"""
파일을 열고 닫는 것을 편하게 처리하기 위해 with문을 사용할 수도 있다.
with open('example.txt', 'w') as f:
    for i in range(0, 3):
        f.write(i + "번 예시입니다.")
"""