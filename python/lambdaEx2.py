#n:int type 어노테이션 
# -> int  리턴타입 어노테이션
# lambda keyword -기능을 매개변수로 전달하는 코드를 더 효율적으로 작성 

def main():
    li = [i+1 for i in range(20)]
    output_map = map(lambda x : x*x, li)
    output_filter = filter(lambda x : x < 10, li)
    print("map result:", list(output_map))
    print("filter result", list(output_filter))
    a = lambda x, y : x+y
    print(a)

if __name__ == "__main__":
    main()