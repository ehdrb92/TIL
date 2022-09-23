# class에서 self의 의미

```python
class 클래스이름:
    def __init__(self):
        self.속성 = 값
```

파이썬에서 클래스는 위와 같이 정의될 수 있다. 클래스에 대해 공부하면서 이해가 잘 가지않았던 개념이 "`self`가 무엇을 의미하는가?" 이다.

여기저기 살펴본 결과 클래스에서 self는 클래스 자신을 의미한다고 한다.... 말로만 해서는 이해가 잘 되지 않으니 직접 코드로 살펴보자.

```python
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()    # 안녕하세요.
```

위의 코드는 Person 클래스를 정의하고 해당 클래스를 james 변수로 지정하여 인스턴스로 만들고 greeting() 메소드는 호출한 모습이다.

그러면 어떤 식으로 코드가 작동할까?

클래스 안에 정의된 __init__()가 클래스가 동작함과 동시에 작동된다. 여기서 self 매개변수는 클래스 자신이라고 하였다.
그런데 Person()이 james이므로 self에는 james가 들어가게 되고, 아래와 같이 정의된다.

`james.hello = '안녕하세요.'`

여기서 우리는 greeting 메소드를 호출했기 때문에 해당 함수가 작동하게 되고, 결국 '안녕하세요.'를 출력하게 된다.
