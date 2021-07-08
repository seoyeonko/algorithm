# ch13-lab4: 히스토그램에서 가장 넓은 직사각형 넓이 구하기

def middle(v, a, c, b):
    h = min(v[c], v[c+1])
    w, i, j = 2, c-1, c+2
    s = w*h
    while i >= a and j <= b:
        if v[i] > v[j]:
            h = min(h, v[i])
            i -= 1
        else:
            h = min(h, v[j])
            j += 1
        w += 1
        s = max(s, w*h) # 더 큰 값을 새로운 s값으로 
    while i >= a:
        h = min(h, v[i])
        i -= 1
        w += 1
        s = max(s, w*h)
    while j <= b:
        h = min(h, v[j])
        j += 1
        w += 1
        s = max(s, w*h)
    return s


def histo(v, a, b):
    if a == b: return v[a] # 탈출조건
    c = (a+b)//2
    r1 = histo(v, a, c) # 앞 결과
    r2 = histo(v, c+1, b) # 뒤 결과
    r = max(r1, r2)
    r = max(r, middle(v, a, c, b))
    return r



v = list(map(int, input().split()))
print(histo(v, 0, len(v)-1))