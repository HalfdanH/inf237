import sys


def lps(pattern):
    n, k = 0, len(pattern)

    lps = [0]*k

    idx = 1

    while idx < k:
        if pattern[idx] == pattern[n]:
            n+=1
            lps[idx] = n
            idx+=1
        else:
            if n!= 0:
                n = lps[n-1]
            else:
                lps[idx] = 0
                idx+=1
    return lps



def kmp(text, pattern):
    prefix = lps(pattern)
    n, k = len(text), len(pattern)
    txt_idx, pat_idx = 0, 0
    while txt_idx < n:
        if pattern[pat_idx] == text[txt_idx]:
            txt_idx +=1
            pat_idx += 1
        if pat_idx == k:
            return True
            #pat_idx = prefix[pat_idx-1]
        
        elif txt_idx<n and pattern[pat_idx] != text[txt_idx]:
            if pat_idx != 0:
                pat_idx = prefix[pat_idx-1]
            else:
                txt_idx += 1
    return False



n = int(sys.stdin.readline())

clock1 = sorted(list(map(int, sys.stdin.readline().split())))
clock2 = sorted(list(map(int, sys.stdin.readline().split())))

d1  =[]
d2 = []

for i in range(n):
    diff = abs(clock1[i]-clock1[(i+1)%n])
    diff = min(diff, 360000-diff)
    d1.append(diff)

    diff = abs(clock2[i]-clock2[(i+1)%n])
    diff = min(diff, 360000-diff)
    d2.append(diff)

d2 += d2

a = kmp(d2, d1)

if a:
    print("possible")
else:
    print("impossible")

