numbers_dict = {0: "ноль",
                1: "один", 2: "два", 3: "три", 4: "четыри", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
                10: "десять",
                11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
                16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать",
                20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестдесят", 70: "семдесят",
                80: "восемдесят", 90: "девяноста", 100: "сто", 200: "двести", 300: "триста", 400: "четыресто",
                500: "пятьсот", 600: "шестьсот", 700: "семьсот",
                800: "восемьсот", 900: "девятьсот", 1000: "тысяча"}

# get value from numbers_dict
def get_value(num):
    value = numbers_dict.get(num)
    return f' {value}'

def delimeter(num: int):
    result_list = []
    # единицы
    if num < 20:
        result_list.append(get_value(num))
    # десятки
    elif num < 100:
        result_list = delimeterOf10(num)
    # сотые
    elif num < 1000:
        result_list = delimeterOf100(num)
    # тысячные
    elif num < 1000000:
        result_list = delimeterOf1000(num)
    # миллион
    else:
        result_list = delimeterOfMillion(num)
    return result_list

def delimeterOf10(num: int):
    result_list = []
    first = int((num / 10)) * 10
    second = num - first
    temp_list = [first, second]
    for i in temp_list:
        result_list.append(get_value(i))
    return result_list

def delimeterOf100(num: int):
    result_list = []
    first = int((num / 100)) * 100
    second = int((num - first) / 10) * 10
    third = num - (first + second)
    if second < 20:
        new_second = second + third
        temp_list = [first, new_second]
    else:
        temp_list = [first, second, third]
    for i in temp_list:
        result_list.append(get_value(i))
    return result_list

def delimeterOf1000(num: int):
    result_list = []
    first = int((num / 1000)) * 1000
    second = int(((num - first)) / 100) * 100
    third = int((num - first - second) / 10) * 10
    fourth=num-(first+second+third)
    if first/1000!=1:
        new_first=get_value(first/1000)
        temp_list=[new_first,second,third,fourth]
    if second==0 and third<20:
        new_third=third+fourth
        temp_list=[first,new_third]
    elif second>0 and third<20:
        new_third=third+fourth
        temp_list=[first,second,new_third]
    elif second==0 and third>20:
        temp_list = [first,third, fourth]
    else:
        temp_list=[first,second,third,fourth]
    for i in temp_list:
        result_list.append(get_value(i))
    return result_list

def delimeterOfMillion(num: int):
    pass

def start(text: str):
    result = ''
    splitted_list = text.split()
    for word in splitted_list:
        if word.isdigit():
            number_len = len(word)
            if number_len <= 9:
                list = delimeter(int(word))
                for i in list:
                    result += f' {i}'
            else:
                # for Billion
                pass
        else:
            result += f' {word}'
    return result

print(start(text='salam 2112 asalam'))
