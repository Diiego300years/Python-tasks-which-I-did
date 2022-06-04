# should return len of words on the lef and right side from "="
def CommandLine(s):
    # code goes here
    s = s.split("=")
    ans = str(len(s[0])) + '='

    for i in range(1, len(s) - 1):
        x = s[i].rsplit(" ", 1)
        ans += str(len(x[0])) + " " + str(len(x[1])) + '='
    ans += str(len(s[len(s) - 1]))

    return ans


# keep this function call here
print(CommandLine("SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High"))