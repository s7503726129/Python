class time:

    def __init__(self):
        print("시(0~23): ")
        h = input()
        print("분(0~59): ")
        m = input()
        print("초(0~59): ")
        s = input()

        self.hour = int(h)
        self.minute = int(m)
        self.second = int(s)

        if self.hour < 0 or self.hour > 23:
            raise Exception("시의 범위(0~23)를 넘었습니다. {0}시".format(self.hour))
        elif self.minute < 0 or self.minute > 59:
            raise Exception("분의 범위(0~59)를 넘었습니다. {0}분".format(self.minute))
        elif self.second < 0 or self.second > 59:
            raise Exception("초의 범위(0~59)를 넘었습니다. {0}초".format(self.second))

    def __add__(self, other):
        a = (60 * (60 * self.hour)) + (60 * self.minute) + self.second
        b = (60 * (60 * other.hour)) + (60 * other.minute) + other.second
        c = a + b
        resultH = c // 3600
        resultM = (c % 3600) // 60
        resultS = (c % 3600) % 60

        # resultH = self.hour + other.hour
        # resultM = self.minute + other.minute
        # resultS = self.second + other.second

        if resultH >= 24:
            raise Exception("24시를 초과했습니다. {0}시".format(resultH))
        else:
            print("두 시간의 합은 :{0}시 {1}분 {2}초 입니다.".format(resultH, resultM, resultS))

    def __repr__(self):
        return "시간 : " + str(self.hour) + "시 "+ str(self.minute) + "분 " + str(self.second) + "초 "

    def __lt__(self, other):
        a = (60 * (60 * self.hour)) + (60 * self.minute) + self.second
        b = (60 * (60 * other.hour)) + (60 * other.minute) + other.second
        return a < b

    def __eq__(self, other):
        a = (60 * (60 * self.hour)) + (60 * self.minute) + self.second
        b = (60 * (60 * other.hour)) + (60 * other.minute) + other.second
        return a == b

    def __gt__(self, other):
        a = (60 * (60 * self.hour)) + (60 * self.minute) + self.second
        b = (60 * (60 * other.hour)) + (60 * other.minute) + other.second
        return a > b

    def __del__(self):
        print("{0}시 {1}분 {2}초가 삭제되었습니다.".format(self.hour, self.minute, self.second))


A = time()
B = time()

C = A + B

print(A)
print(B)


if A < B:
    print("뒤 시간이 길다.")
elif A == B:
    print("두 시간이 같다.")
elif A > B:
    print("앞 시간이 길다.")
else:
    print("ERROR")
