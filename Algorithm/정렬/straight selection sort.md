단순 선택 정렬은 가장 작은 원소부터 선택해 알맞은 위치로 옮기는 작업을 반복하며 정렬하는 알고리즘이다.

예를 들어 다음과 같은 코드가 있다고 가정하자.

`[6, 4, 8, 3, 1, 9, 7]`

해당 배열을 오름차순으로 정렬하고자 한다. 이때 마지막 인덱스 부터 차례대로 모든 원소를 스캔한다. 그리고 그 중 최소값을 찾아내고 해당 원소를 스캔한 범위에서 제일 첫번째 인덱스와 교환해준다. 그러면 다음과 같이 정렬될 것이다.

`[1, 4, 8, 3, 6, 9, 7]`

이와 같은 과정을 반복하여 정렬을 수행하게 된다.

```python
from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """단순 선택 정렬"""
    n = len(a)
    for i in range(n - 1):
        min = i  # 정렬 할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]  # 정렬 할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환 
```
