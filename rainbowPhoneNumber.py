import hashlib
import time

# 전화번호의 범위를 설정합니다.
def generate_phone_numbers():
    for i in range(1000, 10000):  # 1000 ~ 9999 (앞자리에 0이 올 수 없음)
        for j in range(10000):  # 0000 ~ 9999
            yield f"010-{i:04d}-{j:04d}"

# 전화번호에 대한 SHA-256 해시값을 계산합니다.
def sha256_hash(phone_number):
    return hashlib.sha256(phone_number.encode()).hexdigest()

# 레인보우 테이블을 생성합니다.
def create_rainbow_table():
    rainbow_table = {}
    for phone_number in generate_phone_numbers():
        hashed_value = sha256_hash(phone_number)
        rainbow_table[hashed_value] = phone_number
    return rainbow_table

# 주어진 해시값에 대해 원래 전화번호를 찾습니다.
def reverse_lookup(hash_value, rainbow_table):
    return rainbow_table.get(hash_value, None)

# 메인 함수
def main():
    # 전화번호 입력
    example_phone = input("찾을 전화번호를 입력하세요 (형식: 010-XXXX-XXXX): ")
    
    # 시작 시간 측정
    start_time = time.time()
    
    # SHA-256 해시값 계산
    example_hash = sha256_hash(example_phone)
    print(f"입력한 전화번호: {example_phone}, Hash: {example_hash}")
    
    # 레인보우 테이블 생성
    print("레인보우 테이블 생성 중...")
    rainbow_table = create_rainbow_table()
    
    # 레인보우 테이블에서 찾기
    found_phone = reverse_lookup(example_hash, rainbow_table)
    
    # 종료 시간 측정
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # 결과 출력
    if found_phone:
        print(f"원래 전화번호를 찾았습니다: {found_phone}")
    else:
        print("원래 전화번호를 찾지 못했습니다.")
    
    print(f"소요된 시간: {elapsed_time:.2f}초")

# 실행
if __name__ == "__main__":
    main()
