#함수정의
def print_3_time():

    print("hello")
    print("hello")
    print("hello")
    a = 100
    return "ok", 1, "completed", a

#인자의 타입은 중요하지않고, 갯수만 일치하면 실행이 가능하다

def print_n_time(n):
    for i in range(n):
        print("안녕하세요!!!")

def main():
    re = print_3_time()
    print_n_time(3)
    print(re)

if __name__ == "__main__":
    main()
