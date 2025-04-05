# __init__ 특수한기능 지정된함수 생성자
# __init__  함수는 꼭 있어야한다

class Student:
    def __init__(self, name, korean, math, english, science, *a, **kwargs) :
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.sience =science

    def get_sum(self):
        return self.korean + self.math + self.english + self.sience

    def get_average(self):
        return self.get_sum()/4
    

def main():
    a = Student("choi", 10,20,30,40)
    b = Student("kim", 11,21,31,41)
    print(a,b)
    # print(a.sience, a.english, a.math, a.name)
 
if __name__ == "__main__":
    main()
