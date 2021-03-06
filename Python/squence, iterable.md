# 시퀀스 객체와 반복 가능한 객체

리스트, 튜플, range, 문자열은 시퀀스 객체이면서 반복 가능한 객체라고 했다. 시퀀스 객체와 반복 가능한 객체의 차이점은 무엇일까?

다음 그림과 같이 반복 가능한 객체는 시퀀스 객체를 포함한다.

![squence](./image/sqenceobject.png)

리스트, 튜플, range, 문자열은 반복 가능한 객체이면서 시퀀스 객체이다. 하지만, 딕셔너리와 세트는 반복 가능한 객체이지만 시퀀스 객체는 아니다. 왜냐하면 시퀀스 객체는 요소의 순서가 정해져 있고 연속적(sequence)으로 이어져 있어야 하는데, 딕셔너리와 세트는 요소(키)의 순서가 정해져 있지 않기 때문이다. 따라서 시퀀스 객체가 반복 가능한 객체보다 좁은 개념이다.

즉, 요소의 순서가 정해져 있고 연속적으로 이어져 있으면 시퀀스 객체, 요소의 순서와는 상관없이 요소를 한 번에 하나씩 꺼낼 수 있으면 반복 가능한 객체이다.
