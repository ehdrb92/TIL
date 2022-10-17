KMP법은 접두사와 접미사의 일치를 이용한 방법으로 브루트 포스에 비해 빠른 검색 속도를 가지고 있다. 먼저 대략 적인 원리를 살펴보면 다음과 같다.

예를들어 'banabac'라는 문자열을 'banabanabac'라는 문자열에서 검색한다고 생각하자. 첫 번째 인덱스부터 탐색하기 시작하면, 'banaba'까지는 일치하지만 이후 한 개의 문자열에 대해 일치하지 않는 모습을 보인다. 이때 브루트 포스 방법의 경우 단순히 1번째 인덱스부터 다시 검색하기 시작하겠지만 KMP는 다르다.

KMP는 일치한 문자열의 접두사와 접미사를 고려한다. 위에서 처음에 검색할 때 'banaba'의 문자열이 일치하였다. 이때 이 문자열의 접두사와 접미사가 'ba'로 일치하는 모습을 보였다. 그러면 KMP법에 의해 다음 검색은 일치한 접미사의 인덱스부터 시작한다. 그러면 중간에 있는 'ana'의 문자열을 건너뛰고 4번째 인덱스의 'b'부터 검색을 시작하게 된다. 그러면 불필요하게 중간 탐색을 제외하는 것이다.

* KMP법 파이썬 구현 코드

```python
def kmp_match(txt: str, pat: str) -> int:
    """KMP법에 의한 문자열 검색"""
    pt = 1  # txt를 따라가는 커서
    pp = 0  # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1)  # 건너뛰기 표

    # 건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1
```