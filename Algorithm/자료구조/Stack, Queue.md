# Stack & Queue

Stack과 Queue는 비슷하지만 조금은 다른 구조를 가진 데이터 구조이다.

## Stack

**Stack**자료구조는 데이터들이 들어오는 순서대로 쌓이고 마지막에 들어온 데이터부터 나오는 LIFO(Last In First Out)방식의 데이터 구조이다.

### 활용

어떤 경로 혹은 순서의 기록을 역순으로 저장하고 처리해야 할 때 많이 쓰인다.

- 웹 브라우저 방문기록
- 실행취소 기능 (Ctrl + z)

## Queue

**Queue**자료구조는 데이터들이 들어오는 순서대로 쌓이고 들어온 데이터부터 나오는 FIFO(First In First Out)방식의 데이터 구조이다.

### Double Ended Queue(Deque)

**Deque**는 Queue의 양 끝단에서 데이터의 삽입/삭제가 가능한 자료구조 이다.

Stack과 Queue의 혼합형 자료구조라고 생각할 수 있다.

### 활용

waiting 시스템 또는 scheduling 등 순서대로 처리가 필요한 경우 많이 쓰인다.

- 식당 예약
- OS 프로세스 스케쥴링
- 최근 방문 사이트 주소(Deque)
- 문서 작성 프로그램의 undo 기록 (Deque)
