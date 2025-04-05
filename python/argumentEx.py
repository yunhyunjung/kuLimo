# *values는 가변매개변수
# n:int 는 타입힌트
# 함수를 사용할때 타입을 알수있꼐힌트추
# _ 는 사용되지 않는 변수
# list와 튜플의 차이
# 튜플로 만들어진 원소는 변경불가능하다

def print_n_times(n : int, *values):
    print(type(values))
    for _ in range(n):
        for v in values:
            print(v)
        print()

#기본변수
def print_n_times(value, n=3):
    for i in range(n):
        print(value)

#키워드매개변수
def print_n_times_keyword(value, *values, a=3, b=4, c=5):
    for _ in range(a):
        print(a,b,c)
        print(value)
        for v in values:
            print(values)

# 가변키워드매개변수
# 앞에서 정의되지않은 매개변수가 들어올경우 가변매개변수
def print_n_times_keyword_variable(value, *values, a=3, b=4, c=5, **kwarged):
    print(type(kwarged)) #dictionary
    for _ in range(a):
        print(a,b,c)
        print(f"value:::::::::: { value}")
        for v in values:
            print(f"values  ::::::::::::: {values}")

    for k, v in kwarged.items():
        print(k,v)


def main():
    # print_n_times(3, "abc", "def", "ghi", "안녕", "하세요")
    # print_n_times_keyword("안녕하세요", 5, "abc", "def", a=6, b=7)
    print_n_times_keyword_variable("안녕하세요", 5, "abc", "def","ghi","jkl", a=6, b=7,d=999 ,new="new_value")

if __name__ == "__main__":
    main()