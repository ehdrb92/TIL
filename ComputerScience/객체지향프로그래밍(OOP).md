# 객체 지향 프로그래밍

객체 지향 프로그래밍의 특징은 "프로그래밍에서 필요한 데이터를 추상화시켜 상태와 행위를 가진 객체를 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직을 구성하는 프로그래밍 방법." 이라고 한다.

쉽게 말하자면, 비슷한 기능을 하는 함수들을 하나의 객체로 묶고, 묶인 객체들이 상호작용을 하는 방법이라고 할 수도 있을것 같다.

이러한 객체 지향 프로그래밍은 4가지의 대표적인 특징을 가지고 있다.

## 캡슐화(encapsulation)

캡슐화는 객체의 속성(data field)과 행위(methods)를 하나로 묶고, 실제 구현 내용 일부를 내부에 감추어 은닉한다는 특징이다.

```python
class Person():
    def __init__(self, arms, legs):
        self.arms = 2
        self.legs = 2

    def say_hello(self):
        print("Hello.")
```

위는 사람(Person)이라는 클래스로 `__init__`을 통하여 사람 객체가 생성될 때마다 모두 팔 두 개와 다리 두 개를 가지고 태어나도록 하였다. 그리고 `say_hello`함수로 사람 클래스에 해당 메소드를 호출 시키면 동일하게 인사를 하도록 하였다.

이는 위에서 언급한 특징인 객체의 속성과 행위를 하나의 클래스(객체)로 묶은 것을 볼 수 있다. 그렇다면 구현 내용의 일부를 은닉하는 것은 무엇을 말하는 것일까?

## 상속(inheritance)

상속은 객체가 다른 객체로 부터 동일한 기능을 상속받는 것을 의미한다.

```python
class Person():
    def __init__(self, arms, legs):
        self.arms = 2
        self.legs = 2

    def say_hello(self):
        print("Hello.")

class Korean(Person):
    def __init__(self, hair):
        self.hair = 'black'
```

위 코드는 Person을 기반 클래스로 하여 Korean이 파생 클래스가 되어 상속을 받는 모습이다. Korean에는 머리카락이 검은색이라는 속성이 있다 그런데 Person 클래스를 상속 받아 팔과 다리가 2개라는 속성값 또한 같이 가지게 된다. 그리고 say_hello 메소드 또한 사용할 수 있다.

## 추상화(Abstraciton)

추상화란 공통된 속성 또는 기능을 추출하여 하나로 묶어 부르는 것이다. 다른 특별한 점은 없고, 위의 예와 같이 공통된 기능들을 Person이라는 하나의 클래스로 설계하는 것 자체를 추상화라고 한다.

## 다형성(polymorphis)

다형성이란 하나의 변수명, 함수명이 상황에 따라 다른 의미로 해석될 수 있다는 것이다. 즉, 오버라이딩(Overriding)이 가능하다는 의미이다.

```python
class Person():
    def __init__(self, arms, legs):
        self.arms = 2
        self.legs = 2

    def say_hello(self):
        print("Hello.")

class Korean(Person):
    def __init__(self, hair):
        self.hair = 'black'
    
    def say_hello(self):
        print("안녕하세요.")
```

위를 보면 Korean은 Person으로 부터 파생된 클래스라는 것을 알 수 있다. 그런데 Person 클래스에 이미 say_hello 함수가 정의되어 있음에도 불구하고 Korean에서 "안녕하세요."를 프린트하도록 다시 정의하였다. 그리면 기반 클래스에 이미 정의된 함수라고 할 지라도 Korean에서 만큼은 "안녕하세요."가 프린트 된다.
