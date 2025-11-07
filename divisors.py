import sys
import math

# 과제는 보통 명령줄 인수를 받도록 요구합니다.
# sys.argv[1]에 약수를 구할 숫자가 들어옵니다.

def find_divisors(number):
    """주어진 숫자의 약수를 찾아 리스트로 반환합니다."""
    divisors = []
    # 1부터 숫자까지 반복하며 약수를 찾습니다.
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    try:
        # 명령줄 인수가 있는지 확인 (예: python divisors.py 100)
        if len(sys.argv) < 2:
            # 인수가 없으면 오류 메시지를 출력하거나 종료
            sys.exit(1)
        
        # 첫 번째 인수를 숫자로 변환
        input_number = int(sys.argv[1])
        
        # 숫자가 음수일 경우 (필요하다면) 처리
        if input_number <= 0:
            sys.exit(1)
            
        # 약수 계산 및 출력
        result = find_divisors(input_number)
        
        # 과제에서 요구하는 출력 형식에 맞게 결과를 출력합니다.
        # (테스트가 이 출력을 읽습니다. 여기서는 쉼표로 구분된 문자열로 가정합니다.)
        print(",".join(map(str, result)))
        
    except ValueError:
        # 숫자가 아닌 다른 값이 입력되었을 경우 처리
        sys.exit(1)
