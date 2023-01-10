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
        s = s.replace(key,vel)
        print(s)
    return s

solution("2three45sixseven")