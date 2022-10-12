브루트 포스방식은 가장 기초적으고 단순하게 검색하는 방법이다. 사실상 선형검색하고 거의 같다고 봐도 무방하다.

```python
def bf_match(txt: str, pat: str) -> int:
    pt = 0 # txt 커서 (인덱스)
    pp = 0 # pat 커서 (인덱스)

    while pt != len(txt) and pp != len(pat): # pt, pp 커서가 모든 검색을 완료함 
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1
```

파이썬으로 브루트 포스를 구현한 코드이다.

* 파이썬 멤버십 연산자와 표준 라이브러리를 이용한 문자열 탐색 방법

    + 멤버십 연산자로 구하기

        `ptr in txt` -> ptn 문자열이 txt 문자열안에 포함되어 있는지 확인한다.

        `ptr not in txt` -> ptn 문자열이 txt 문자열안에 포함되어 있지 않은지 확인한다.

    + 표준 라이브러리 사용하기

        `string.find(value, start, end)` -> string 문자열 안의 [start:end]에 value가 포함되어 있는지 확인한다. 포함되어 있으면 가장 작은 인덱스 값을 반환하고, 없으면 -1을 반환한다.

        `string.rfind(value, start, end)` -> string 문자열 안의 [start:end]에 value가 포함되어 있는지 확인한다. 포함되어 있으면 가장 큰 인덱스 값을 반환하고, 없으면 -1을 반환한다.

        `string.index(value, start, end)` -> find 함수와 같은 기능을 수행한다. 다만, value가 발견되지 않으면 예외 처리로 ValueError를 반환한다.

        `string.rindex(value, start, end)` -> rfind 함수와 같은 기능을 수행한다. 다만, value가 발견되지 않으면 예외 처리로 ValueError를 반환한다.

        `string.startswith(value, start, end)` -> string 문자열 안의 [start:end]가 value로 시작하면 True 아니면 False를 반환한다.

        `string.endswith(value, start, end)` -> string 문자열 안의 [start:end]가 value로 끝나면 True 아니면 False를 반환한다.
