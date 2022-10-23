zip 함수는 여러 개의 순회 가능한 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 접근할 수 있는 반복자를 반환한다.

```python
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
```

* 병렬 처리

    zip 함수를 활용하면 여러 그룹의 테이터를 루프 한 번만 돌면서 처리할 수 있다. 가변인자를 받기에 2개 이상의 인자를 넘겨서 병렬 처리를 할 수 있다.

    ```python
    >>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    ...     print(number, upper, lower)
    ...
    1 A a
    2 B b
    3 C c
    4 D d
    5 E e
    ```

* unzip

    엮여 있는 데이터를 unzip을 통해 헤체할 수 있다.

    ```python
    >>> numbers = (1, 2, 3)
    >>> letters = ("A", "B", "C")
    >>> pairs = list(zip(numbers, letters))
    >>> print(pairs)
    [(1, 'A'), (2, 'B'), (3, 'C')]
    ```

* zip을 이용한 dictionaly 자료형 만들기

    ```python
    >>> keys = [1, 2, 3]
    >>> values = ["A", "B", "C"]
    >>> dict(zip(keys, values))
    {1: 'A', 2: 'B', 3: 'C'}
    ```