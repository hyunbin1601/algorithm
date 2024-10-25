import sys
input = sys.stdin.readline

n = int(input())

def star_draw(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        stars = star_draw(n//3)  # n//3은 3으로 나눈 몫을 의미함, 재귀
        result = []  # stars는 재귀 호출을 통해 반환된 값을 저장하는 변수, result는 출력할 별을 저장하는 배열
        for i in range(n): #n개의 줄을 생성하기 위함,
            if i // (n//3) == 1:  # 공백이 위치하는 곳 설정 -> 이것도 출력 보면서 조정했어야 했음....
                result.append(stars[i % (n//3)] + ' ' * (n//3) + stars[i % (n//3)])  # 공백 줄 출력, %는 나머지
            else:
                result.append(stars[i%(n//3)] * 3)  # 공백을 제외한 줄은 별을 그대로 출력한다
        return result  # result 배열을 반환
    
print('\n'.join(star_draw(n))) # \n은 줄바꿈을 의미함, join은 리스트를 문자열로 변환하는 함수
# 왜 join을 사용하는가? -> join을 사용하지 않으면 리스트 형태로 출력되기 때문에, join을 사용하여 문자열로 변환하여 출력함
# join 앞에 \n을 사용하는 이유는? -> 줄바꿈을 위해서 사용함
# 그럼 첫째줄은 어떻게 출력되는가? -> 첫째줄은 별을 그대로 출력함
# 그럼 \n이 첫째줄에 미치는 영향은? -> 첫째줄은 별을 그대로 출력하고, 그 다음부터는 \n을 사용하여 줄바꿈을 해줌
# for문을 대신 사용하여 출력할 수 있는 방법은? -> for문을 사용하여 출력할 수 있지만, join을 사용하여 출력하는 것이 더욱 간단하고 효율적임

        