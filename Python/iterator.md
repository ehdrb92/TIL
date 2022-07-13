# Iterator

파이썬에는 이터레이터라는 메소드가 존재한다. 이터레이터는 반복 가능한 객체에서 값을 하나씩 뽑아내어 반환하는 메소드이다. 우리가 파이썬에서 for문을 사용하면 반복 가능한 객체에서 값을 뽑아내는 것을 볼 수있다.
그런데 이는 for문이 원래 그런 특징을 가진게 아니라, 자동으로 이터레이터를 생성하여 값을 뽑아내도록 해주는 것이다.

그렇다면 우리가 임의로 이터레이터를 만들어 보도록 하자.

```python
class 이터레이터이름:
    def __iter__(self):
        코드
 
    def __next__(self):
        코드
```

이터레이터를 만드는 기본적인 구조는 위와 같다. 그렇다면 이 예시를 참고하여 이터레이터 코드를 짜보면 아래와 같이 만들 수 있다.

```python
class Counter:
    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생
 
for i in Counter(3):
    print(i, end=' ')
```

위 코드의 결과는 `0, 1, 2`가 반환되게 된다.
