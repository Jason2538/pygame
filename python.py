name = "\"윤아로\""
name = '"안지호"'
ment = "안녕하세요?"
age = 20
wonju = 3.14

units = 151
score = 421 
stamina = "89%"
life = "2개"

print("파괴한 유닉 수 : {}, 점수: {}" .format(151, 421))
print("체력: {}, 목숨: {}".format("89%", "2개"))

print (name)
print(ment[-4:-2])


list = [1, 2, 3, 4, 5, "윤아로", "안지호"]

print(list[:5])

food = ["삼겹살", "목살", "등심"]

print (food)

food.append("안심")

print(food)

food.append("갈매기살")

print(food)

food.insert(0, "곱창")

print(food)

food.remove("곱창")

print(food)

del(food[0])

print(food)

sports = ("야구", "축구", "배드민턴")

print(sports)

print(sports[1])

people = {'name':'윤아로', 'age':63}

print(people)

print(people["age"])





##################################################################################################################################################################################################################################################################################################################################################

# number = 1
# print(float(number))
# number2 = 3.174
# print(int(number2))

# num1 = int(input())
# num2 = int(input())
# print(num1+num2)

print(len([1, 2, 3, 4, 5]))

print(min(456, 786, 3546, 14846, -324646365846))

print(max(456, 786, 3546, 14846, -324646365846))

print(sum([41324864, 545712446545648643545, 65489435148674351486, 654835486465484416, 6548434654657984464156452]))

print(divmod(5, 9))

print("이서준 똥멍청이")

print(abs(448746514654734684646874146846514654651654351465145646546846548645648946464654654864658746574864798479/8798974897487967984984984984678786498489))

print(pow(2, 100))

print(round(3.745, 2))

#연산자: 산술연산자, 비교연산자, 논리연산자

print(5/3)

print(5//3)

print(5%3)

print(pow(2,3))

print(2**3)


################################

#==
#>
#<
#<=
#>=
#!=

a= 10
#a +=1 == a = a+1

a = 10
a += 5
a -= 5
a *= 3
a /= 3
print(a)

##########################
#and
#or
#not


a, b = 6, 4

print(5 < a and 5 < b)

print(5 < a or 5 < b)

print(5 < a and not 5 < b)

print(5 < a or not 5 < b)

##########################################################################################################################################################################################################################################################################

num = 10
if num==10:
    print("10입니다.")
elif num == 20:
    print("20입니다.")
else:
    print("10입니다.")
print("끝")

for i in range(10):
    print(i)


list = ['삼겹살', '항정살', '목살']
for i in list:
    print(i)


a = 1
while a<10:
    print(a)
    a+=1

#함수

def plus3(number, number2):
    return number+number2
print(plus3(13, 30))
