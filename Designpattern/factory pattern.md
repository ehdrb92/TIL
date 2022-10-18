## 팩토리 패턴(factory pattern)

* 특징

    + 객체 생성 부분에 대한 부분을 별도로 구분하여 추상화한 패턴
    + 상위 클래스와 하위 클래스가 존재하는데, 상위 클래스는 주요 뼈대를, 하위 클래스는 구체적인 내용을 결정
    + 클래스가 나누어져 있어 느슨한 결합을 가지며 유연성이 높음
    + 리팩토링 시 유지 보수성이 좋음

* 용도

    특정 공통된 객체를 여러 곳에서 만들어서 사용할 때

* 단점

    새로운 종류의 객체를 생성해야 할 때 마다 클래스를 함께 만들어야한다.