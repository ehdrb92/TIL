단순 삽입 정렬은 주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하며 정렬하는 알고리즘이다. 단순 선택 정렬과 비슷해 보이지만 값이 가장 작은 원소를 선택하지 않는다는 점이 다르다. 정렬 방식은 다음과 같다.

`[6, 4, 1, 7, 3, 9, 8]`

해당 배열에서 앞쪽에서 두 번째 원소부터 스캔을 하기 시작한다. 그러면 4는 맨 앞 인덱스인 6보다 작다 그러면 4를 맨 앞 인덱스에 삽입한다. 해당 방법을 반복하면 결국 첫 번째 스캔에서 1이 맨 앞에 오게된다. 그러면 이제 세 번째 원소부터 스캔을 시작하여 삽입을 시작하면 결국 원소 3이 두 번째 인덱스에 오게 된다. 이런 방식으로 정렬을 하는 것이다.

```python
from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
```

* 이진 삽입 정렬

```python
from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1  # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl + pr) // 2  # 검색 범위의 중앙 원소 인덱스
            if a[pc] == key:     # 검색 성공
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
    
        pd = pc + 1 if pl <= pr else pr + 1  # 삽입할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key
```

* 파이썬 bisect.insort 사용

```python
from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬(bisect.insort을 사용)"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
```
