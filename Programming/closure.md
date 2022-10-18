# 클로저에 대한 이해

파이썬, 자바스크립트와 같은 언어에는 클로저라는 개념을 사용한다.

클로저의 기본적인 개념은 아래와 같다.

1. 해당 함수는 어떤 함수 내의 중첩된 함수여야 한다.
2. 해당 함수는 자신을 둘러싼(enclose) 함수 내의 상태값을 반드시 참조해야 한다.
3. 해당 함수를 둘러싼 함수는 이 함수를 반환해야 한다.

```python
def in_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper
```

위 함수는 캐시 히트 여부를 검사하는 함수이다. 정수 n을 받고 해당 정수의 키가 존재하면 해당 값을 반환하고, 없다면 cache 딕셔너리에 새로 담는다. 위에서 wrapper함수는 클로저로서 조건을 모두 만족한다.

1. in_cache 함수 내의 중첩된 함수이다.
2. Enclosing하는 in_cache 스코프의 cache 라는 상태값을 참조한다.
3. 자신을 둘러싼 함수는 자신(wrapper)을 반환하고 있다.

위의 함수를 사용해보기 위해 팩토리얼 값을 구하는 함수를 가져와 보자.

```python
def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret
```

함수를 다음과 같이 작동시킨다.

```python
factorial = in_cache(factorial)

factorial(3)
factorial(5)
factorial(10)
```

위와 같이 작동시키면 in_cache함수의 cache 자료구조에는 아래와 같은 값이 쌓일 것이다.

```python
cache = {
    3: 6,
    5: 120,
    10: 3628800,
}
```

in_cache 함수안에 정의된 cache라는 자료구조는 매번 실행되는 wrapper함수의 바깥에 정의되어 있다. 그래서 매번 factorial 함수가 실행되더라도 전역변수처럼 작동할 수 있다.

## 클로저의 장점

클로저는 위의 예시와 같이 자신의 스코프를 만들고 해당 스코프안에서만 전역변수처럼 활동하는 변수를 만들 수 있다. 그냥 전역변수를 쓰면 되지 않는가? 라고 생각할 수도 있지만 각 기능별로 작동하는 변수를 관리하기 위해서는 위와 같은 방식을 사용하면 훨씬 편하다.
