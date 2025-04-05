def return_100():
    return 100, 200, "_되돌아 가는 문자", True, False

def call_10_times(func):
    for i in range(10):
        func()


#간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

#return_100 ValuesError : too may values to unpack
def main():
    # a, b, c = return_100()
    # print(a,b,c)
    call_10_times(print_hello)
#lambda

if __name__ == "__main__":
    main()