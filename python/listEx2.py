def main():

    list_a = [1,2,3]
    list_b = [4,5,6]

    print(list_a+list_b)
    #리스트를 반복
    print(list_a*3) 

    #리스트에 항목추가
    list_a.append("add item")   
    print(list_a)

    #리스트에 해당위치에 항목추가
    list_a.insert(1, "insertItems") 
    print(list_a)

    #리스트에 요소제거
    del list_a[2]
    print(list_a)

    #리스트에 요소제거
    list_a.pop(1)
    print(list_a)

    #리스트에 요소의 값으로 삭제
    list_a.remove(3)
    print(list_a)   

    # print(1111 in list_a)     

    # j = 0
    # for i in list_b:
    #     j += 1
    #     print(f"{j}번째 요소는 {i}입니다 ")
    
    for j,i in enumerate(list_b):
        print(f"{j+i} 번째 요소는 {i}입니다.")

if __name__ == "__main__":
    main()
