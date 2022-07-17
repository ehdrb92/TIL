# Class의 상속

파이썬에서 클래스는 자신이 가지고 있는 함수 또는 인스턴스를 다른 클래스에 상속하여 사용할 수 있다.

어떤 식으로 상속이 되는지 과정을 보도록 하자.

```python
class 기반클래스이름:
    코드
 
class 파생클래스이름(기반클래스이름):
    코드
```

파이썬 클래스 상속은 기본적으로 위와 같이 만들 수 있다.

```python
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def study(self):
        print('공부하기')
 
james = Student()
james.greeting()    # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드
```

james라는 변수로 할당한 Student클래스는 Person클래스로 부터 상속받는 파생 클래스이므로 greeting과 study함수 모두 사용이 가능하다.

```python
class 기반클래스이름1:
    코드
 
class 기반클래스이름2:
    코드
 
class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
    코드
```

클래스 상속은 위와 같이 다중 상속 또한 가능하니 알아두도록 하자.
