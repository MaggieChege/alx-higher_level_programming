#!/usr/bin/python3
if __name__=="__main__":
    import sys
    ans = 0
    i = 0
    for a in sys.argv:
        if i > 0:
            ans += int(a)
        i += 1
    print(ans)
