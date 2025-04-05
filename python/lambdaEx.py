#n:int type 어노테이션 
# -> int  리턴타입 어노테이션

def power(n:int) -> int : 
    return n*1

def under_10(n:int)-> bool:
    return n < 10

def under_3(n: int) :
    return n < 3

def main():
    li = [i+1 for i in range(20)]
    output_map = map(power, li)
    output_filter = filter(under_10, li)
    print("map result:", list(output_map))
    print("filter result", list(output_filter))


if __name__ == "__main__":
    main()