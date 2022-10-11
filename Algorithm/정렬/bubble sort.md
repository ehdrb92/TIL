버블 정렬(bubble sort)이란 이웃한 두 원소의 대소관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘으로, 단순 교환 정렬이라고도 한다.

* 일반적인 버블 정렬

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
```

일반적인 버블 정렬 코드의 예시이다. 정렬의 마지막 인덱스부터 비교하며 숫자가 낮은 원소가 점점 교환되어 내려온다.

* 알고리즘 개선 1

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬(교환 횟수에 따른 중단)"""
    n = len(a)
    for i in range(n - 1):
        exchng = 0  # 패스에서 교환 횟수
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break
```

만약 정렬은 하는 중 특정 루프에서 교환이 한번도 일어나지 않는다면 뒤는 더 볼 것없이 교환이 완료되었다는 의미가 된다. 그래서 exchange 변수를 두고 해당 변수가 하나의 루프가 끝날 때 까지 교환이 없었다면 정렬을 종료하는 방법이다.

* 알고리즘 개선 2

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬(스캔 범위를 제한)"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
```

정렬의 범위를 빠르게 좁혀 나가는 방법으로 빠르게 정렬하는 방법이다. 첫 스캔에서 처음부터 끝까지 모두 비교를 할 것이다. 여기서 마지막으로 교환이 일어난 지점을 저장하게 된다. 그러면 해당 지점 이후는 이미 모두 정렬이 이루어 졌다는 뜻이 된다. 해당 지점을 기준으로 스캔 범위를 좁히는 방법이다.

* 쉐이커 정렬

```python
from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
```

쉐이커 정렬은 마치 쉐이커를 흔들듯이 앞뒤로 번갈아가며 정렬하는 방법을 말한다. 만약 우리가 정렬하려는 배열이 다음과 같다고 생각해보자.

`[9, 1, 2, 3, 4, 5, 6, 7, 8]`

이렇게 된다면 이제까지 어떤 정렬 방식을 사용하든 결국 모두 스캔하며 루프 또한 많이 이루어지게 된다. 왜냐하면 마지막 인덱스 부터 스캔을 하며 정렬하기 때문이다. 그래서 쉐이커 정렬은 처음에는 뒤 인덱스부터 스캔, 정렬하지만 그 다음에는 앞 인덱스부터 차례대로 스캔한다. 그러면 원소 9는 두 번째 스캔에서 맨 뒤로 옮겨져 정렬이 완료되게 된다.
