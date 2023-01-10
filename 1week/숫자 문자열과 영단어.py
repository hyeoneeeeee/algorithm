def solution(s):
    dic = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
        "zero":"0"
    }
    for key,vel in dic.items():
        print(key,vel)
        s.replace(key,vel)
        print(str(s))
    return str(s)

solution("2three45sixseven")