list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("1 : ", list[0])
print("2 : ", list[0:-1])
print("3 : ", list[0:-2])
print("------------------------------------------------")

string = '\n$10. 2109 W. Chicago Ave., 773-772-0406, theoldoaktap.com'
print(string.split())
price_tmp = string.split()[0][:-1]
print("1 : ", price_tmp)

address_tmp = string.split()[1:-2]
print("2 : ", address_tmp)
print("3 : ", ' '.join(address_tmp))

print("------------------------------------------------")
# 리스트(배열) 정의
food = [ "123", "자장면", "짬뽕", "탕수육", "물만두", "팔보채" ]
# 요소들 사이에 공백 넣기 (구분자는 공백)
print(" ".join(food))
# 모든 요소들을 하나로 연결하여 출력 (구분자 없음)
print("".join(food))
# 슬래쉬(/)기호를 구분자로 넣은 후 연결하여 출력
print("/".join(food))
# 줄바꿈 문자를 구분자로 하여 출력
print("\n".join(food))