# 내부 함수로 구현

print("s : ")
s = input()
print("t : ")
t = input()

def fcmp(s, t):
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

    if s[0] == '-':
        for i in s:
            if i.isnumeric() or i == '.' or i == '-':
                cond = "NUM"
            else:
                cond = "STR"
    else:
        cond ="STR"

    if t[0] == '-':
        for i in t:
            if i.isnumeric() or i == '.' or i == '-':
                cond = "NUM"
            else:
                cond = "STR"
    else:
        cond = "STR"

    if cond == "NUM":
        return numcmp(s, t)

    elif cond == "STR":
        return strcmp(s, t)

    else:
        print("Error")
        exit()

p = fcmp(s, t)
print(p)
