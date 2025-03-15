import datetime

class Temp:
    month = int()

def main(): 
    now = datetime.datetime.now()

    if now.hour < 12:
        print(f"현재시각은 {now.hour}시로 오전입니다")

    if now.hour >=12:
        print(f"현재시각은 {now.hour}시로 오후입니다")
    
    now = Temp()
    now.month = 12

    if 2 < now.month < 6:
        print(f"이번달은 {now.month}월 이므로 봄입니다.")
    elif 5 < now.month < 9:
        print(f"이번달은 {now.month}월 이므로 여름입니다.")
    elif 8 < now.month < 12:
        print(f"이번달은 {now.month}월 이므로 가을입니다.")
    else:
        print(f"이번달은 {now.month}월 이므로 겨울입니다.")

if __name__ == "__main__":
    main()
