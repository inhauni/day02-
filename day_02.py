harry_porter={
    '헤르미온느' : '그리핀도르',
    '말포이' : '슬리데린',
    '말포이' : '그리핀도르'
}

print(harry_porter)
print(type(harry_porter))

#출력값 :
#{'헤르미온느': '그리핀도르', '말포이': '그리핀도르'} -> 말포이라는 key값의 최종 value는 가장 마지막에 입력된 값
#<class 'dict'>

# PI = 3.14
# print(f'원주율의 값은 {PI}이고 타입은 {type(PI)}입니다')
#
# PI = 2.76
# print(f'원주율의 값은 {PI}이고 타입은 {type(PI)}입니다')

math_values=(3.14,2.76)

print(f'원주율의 값은 {math_values[0]}이고 타입은 {type(math_values)}입니다')
# math_values[0]=9.99
# print(f'원주율의 값은 {math_values[0]}이고 타입은 {type(math_values)}입니다')

#오류 발생 : tuple 에 새로운 값을 삽입 할 수 없다 because : tuple은 read only(=immutable:값을 변경 불가)

# x='harry porter'
x=-90
y=x+12

print(2*2*2*2*2)
print(2**5)
print(pow(2,5))
# 세개 다 지수 관련 함수

print(type(divmod(9,5))) #class =튜플
print(type((1,2))) #class tuple
test=1,2 #packing
print(type(test)) #class tuple , 이때 (1,2)를 괄호 없이 쓰면 type에 정수 두개를 배당한 것 처럼 인식 ->오류 발생
print(test) #클래스 튜플

print(test[1]) #2출력
a,b =test #unpacking
print(a) # 1이 출력
print(b) # 2가 출력

# 튜플이 분해되어 각각 순서대로 변수에 배당됨 : unpacking

# a,b,c = test #unpacking : test에 할당 된 숫자의 개수는 2개이므로 오류 발생

# number =0b10011010
# number2=0x9A
# print(number)
# print(number2)

number =154
print(bin(number))
print(hex(number))
print(oct(number))

print(ord(" "))