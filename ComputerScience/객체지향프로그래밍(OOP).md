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

상속은 상위 클래스의 특성을 하위 클래스가 이어받아서 재사용하거나 추가, 확장하는 것을 말한다.

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

## 설계 원칙(SOLID)

* 단일 책임 원칙(SRP, Single Responsibility Principle)

단일 책임 원칙은 모든 클래스는 각각 하나의 책임만 가져야 하는 원칙이다. 예를 들어 A라는 로직이 존재한다면 어떠한 클래스는 A에 관한 클래스여야 하고 이를 수정한다고 했을 때도 A와 관련된 수정이어야 한다.

* 개방-폐쇄 원칙(OCP, Open Closed Principle)

개방-폐쇄 원칙은 유지 보수 사항이 생긴다면 코드를 쉽게 확장할 수 있도록 하고 수정할 때는 닫혀 있어야 하는 원칙이다. 즉, 기존의 코드는 잘 변경하지 않으면서도 확장은 쉽게 할 수 있어야한다.

* 리스코프 치환 원칙(LSP, Liskov Substitution Principle)

리스코프 치환 원칙은 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 하는 것을 의미한다. 클래스는 상속이 되기 마련이고 부모, 자식이라는 계층 관계가 만들어진다. 이때 부모 객체에 자식 객체를 넣어도 시스템이 문제없이 돌아가게 만드는 것을 말한다. 즉, A 객체가 B 객체의 자식 꼐층일 때 A 객체를 B 객체와 바꿔도 문제가 없어야 한다.

* 인터페이스 분리 원칙(ISP, Interface Segregation Principle)

인터페이스 분리 원칙은 하나의 일반적인 인터페이스보다 구체적인 여러 개의 인터페이스를 만들어야 하는 원칙이다.

* 의존 역전 원칙(DIP, Dependency Inversion Principle)

의존 역전 원칙은 자신보다 변하기 쉬운 것에 의존하던 것을 추상화된 인터페이스나 상위 클래스를 두어 변하기 쉬운 것의 변화에 영향받지 않게 하는 원칙을 말한다. 예를 들어 타이어를 갈아끼울 수 있는 틀을 만들어 놓은 후 다양한 타이어를 교체할 수 있어야 한다. 즉, 상위 계층은 하위 계층의 변화에 대해 독립적이어야 한다.
