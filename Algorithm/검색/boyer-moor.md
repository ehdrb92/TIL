보이어 무어법은 KMP와 유사한 방법이다. 기본적으로 일치, 불일치를 가릴 떼 불일치하는 문자가 뒤에 있을 확률이 높다는 것을 가정하고 찾는 방식이다. 비교를 할 skip 테이블을 만들고 해당 테이블을 기준으로 비교를 하기 시작한다.

* skip 테이블 만드는 방법

pattern = 'abcab'

각 문자의 value는 `length - index - 1`으로 나온 값 중 가장 최소값으로 한다. 만약 계산한 value가 0일 경우 value = length, 그리고 패턴에 없는 모든 문자 또한 value = length이다.

a의 value는 4, 1이므로 최소값인 1
b의 value는 3, 0이므로 최소값인 0이 되어야 하지만 0은 해당 사항에 없으므로 3
c의 value는 2

결론적으로 a = 1, b = 3, c = 2, 이외 문자 = 5

string = 'abaabbcababdabcab'
pattern = 'abcab'

비교

[a, b, a, a, b, b, c, a, b, a, b, d, a, b, c, a, b]
[a, b, c, a, b]

불일치 하며 해당 문자열의 마지막 문자는 b, b의 value는 3이므로 3칸 이동 후 비교

[a, b, a, a, b, b, c, a, b, a, b, d, a, b, c, a, b]
         [a, b, c, a, b]

불일치 하며 해당 문자열의 마지막은 a, a의 value는 1이므로 1칸 이동 후 비교 이를 반복한다.

[a, b, a, a, b, b, c, a, b, a, b, d, a, b, c, a, b]
            [a, b, c, a, b]

[a, b, a, a, b, b, c, a, b, a, b, d, a, b, c, a, b]
                     [a, b, c, a, b]

[a, b, a, a, b, b, c, a, b, a, b, d, a, b, c, a, b]
                                    [a, b, c, a, b]

맞는 문자열 발견 후 종료

* 보이어 무어 법 파이썬 코드

```python
def bm_match(txt: str, pat: str) -> int:
    """보이어 무어법에 의한 문자열 검색"""
    skip = [None] * 256  # 건너뛰기 표

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # 검색하기
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
              else len(pat) - pp

    return -1
```