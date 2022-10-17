# 이진검색(binary search)

이진검색은 오름차순 또는 내림차순으로 정렬되어있는 배열에 대해 효율적으로 검색하는 알고리즘이다. 오름차순으로 정렬된 배열이 있다고 가정할 때 해당 배열의 중앙값부터 검색한다. 목표값이 중앙값보다 작거나 크면 해당 범위에서 다시 중앙값을 검색하고 같은 방식으로 계속해서 검색한다.

```python
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0           # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc    # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:
            break
    return -1            # 검색 실패
```

이진검색의 시간복잡도는 O(logn)이다.