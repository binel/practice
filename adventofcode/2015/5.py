import sys 

def containsBad(s):
    return ("ab" in s or
        "cd" in s or
        "pq" in s or
        "xy" in s)

def containsDouble(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True

    return False

def vowelCount(s):
    count = 0
    for i in range(0, len(s)):
        c = s[i]
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    return count

def isNice(s):
    return not containsBad(s) and containsDouble(s) and vowelCount(s) > 2

def main():
    input = sys.argv[1]
    niceCount = 0
    for line in input.splitlines():
        if (isNice(line)):
            niceCount += 1
    print(niceCount)

main()

