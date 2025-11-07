import sys
import math

def find_divisors(number):
    """주어진 숫자의 약수를 찾아 리스트로 반환합니다."""
    divisors = []
    # 1부터 숫자까지 반복하며 약수를 찾습니다.
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    # 이 스크립트가 직접 실행되었을 때만 아래 코드를 실행합니다.
    
    try:
        # 1. [수정됨] 명령줄 인수(sys.argv)가 아닌,
        #    표준 입력(sys.stdin)에서 한 줄을 읽어옵니다.
        #    이것이 "<stdin>"의 의미입니다.
        input_line = sys.stdin.readline()
        
        # 2. 읽어온 줄(예: "100\n")의 공백을 제거하고 숫자로 변환합니다.
        input_number = int(input_line.strip())
        
        # 3. 약수를 계산합니다.
        result = find_divisors(input_number)
        
        # 4. 'result' 리스트의 모든 숫자를 문자열로 변환하고 쉼표(,)로 연결하여 출력합니다.
        print(",".join(map(str, result)))
        
    except (ValueError, TypeError, AttributeError):
        # 숫자가 아니거나 빈 입력일 경우, 오류를 내고 종료합니다.
        sys.exit(1)
