def main():
    dict_a = dict()
    dict_b = {}
    dict_c = { 0: 0}
    print(dict_a, dict_b, dict_c)
    print(type(dict_a),type(dict_b), type(dict_c))

    dict_a= {'name' : '어벤저스 엔드게임',
             'type' : '히어로무비'
            }
    print(dict_a['name'])
    # print(dict_a["등장인물"])
    print(dict_a.get("등장인물"))
    print(dict_a.get("name"))
    dict_a["등장인물"] = ["헐크","스티브","아이언맨","블랙호크"]
    # print(dict_a.get("등장인물"))

    del dict_a["type"]
    # print(dict_a)

    if "name" in dict_a:
        print(dict_a)
    else:
        print("name은 dict_a 의 키 값이 아니다")

    # for key in dict_a:
    #     print(key, ":" ,dict_a[key])

    for key, value in dict_a.items():
        print(key, value)


if __name__ == "__main__":
    main()
