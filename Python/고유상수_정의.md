# enum

**enum**이란 파이썬에서 고유한 의미를 가진 상수값의 집합이다.

프로젝트를 진행하며 특정 상황에 어떤 상태를 부여하기 위해 상수값을 부여해야 할 일이 있었다.

처음에는 각 클래스 별로 필요한 상수값을 별개로 지정하였는데, 이는 너무 불필요하게 반복되는 느낌이 있었다.

그래서 알아본 바 enum이라는 개념에 대해 알게 되었다.

## enum class 만들기

```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

위와 같이 별도의 Enum 클래스를 생성하고 각 색깔에 고유한 상수값을 지정하여 활용할 수 있다.

## enum 활용 예시

```python
>>> member = Color.RED
>>> member.name
'RED'
>>> member.value
1
```

enum은 이터레이션이 가능하다.

```python
>>> class Shake(Enum):
...     VANILLA = 7
...     CHOCOLATE = 4
...     COOKIES = 9
...     MINT = 3
...
>>> for shake in Shake:
...     print(shake)
...
Shake.VANILLA
Shake.CHOCOLATE
Shake.COOKIES
Shake.MINT
```

## enum 중복

enum은 중복되는 멤버명을 허용하지 않는다.

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     SQUARE = 3
...
Traceback (most recent call last):
...
TypeError: Attempted to reuse key: 'SQUARE'
```

하지만 중복값은 허용한다.

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     DIAMOND = 1
...     CIRCLE = 3
...     ALIAS_FOR_SQUARE = 2
...
>>> Shape.SQUARE
<Shape.SQUARE: 2>
>>> Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
>>> Shape(2)
<Shape.SQUARE: 2>
```