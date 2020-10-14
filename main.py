# 외부함수로 구현

print("s : ")
s = input()
print("t : ")
t = input()


def numcmp(s, t):
    num1 = float(s)
    num2 = float(t)

    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


def strcmp(s, t):
    str1 = s
    str2 = t

    if str1 > str2:
        return 1
    elif str1 < str2:
        return -1
    else:
        return 0


def fcmp(s, t):
    s = s
    t = t

    for i in s:
        if 'a' <= i <= 'z':
            return strcmp
        elif 'A' <= i <= 'Z':
            return strcmp
        else:
            cond = "NUM"

    for j in t:
        if 'a' <= j <= 'z':
            return strcmp
        elif 'A' <= j <= 'Z':
            return strcmp
        else:
            cond = "NUM"

    if cond == "NUM":
        return numcmp

    elif cond == "STR":
        return strcmp

    else:
        print("Error")
        exit()


p = fcmp(s, t)

print(p(s, t))
