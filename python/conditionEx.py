def main(): 
    number = int(input("숫자를 넣어주세요:"))
    if (number % 2 == 0):
        print("짝수입니다.")
    else:
        print("홀수입니다.")

    # 반복문 for
    for i in range(10):  #n번 반복 0부터 시작
        print(f"{i} 번째 반복되는 문장입니다.")
    print(list(range(10)))

if __name__ == "__main__":
    main()

