# 정규화

데이터베이스 정규화란 데이터 테이블상에 중복을 제거함으로서 무결성(integrity)를 유지하고, DB의 저정 용량을 줄이는 것이다.
테이블을 분해하는 정규화에는 단계가 구별되어 있다. 해당 단계별로 어떻게 데이터가 정리되는지 보도록 하자.

## 제1 정규화

!['정규화'](./image/%EC%A0%95%EA%B7%9C%ED%99%94(%EC%A0%84).png)
위 테이블은 정규화가 되지 않은 테이블이다. 한 눈에 봐도 정리가 잘 되지않은 느낌이다.

제 1정규형을 갖추려면 **도메인 원자값**이라는 조건이 만족해야 한다고 한다.
도메인 원자값은 아래의 조건을 만족해야 한다.

1. 반복 그룹이 존재하면 안된다.
2. 모든 행은 식별자로 완전하게 구분되어야 한다.

이제 조건을 알았으니 정규화를 시켜보도록 하자.

1. 반복되는 부분을 체크한다.
2. 반복되는 부분과 그렇지 않은 부분을 분리한다. (단, PK의 경우 모든 테이블에 존재)
3. 테이블을 나눈 후 반복되는 행을 삭제한다.

이 과정을 거치면 아래와 같은 테이블로 바뀐다.
!['정규화(1)'](./image/%EC%A0%9C1%EC%A0%95%EA%B7%9C%ED%99%94(1).png)
그런데, '학생' 테이블은 2번 조건인 "모든 행은 식별자로 완전하게 구분되어야 한다." 라는 조건이 만족하는 반면 수강내역은 prime key인 '학번'만으로는 모든 행이 구분되지 않는다.

그렇기 때문에 추가적으로 key를 설정 해 주어야 한다. 그래서 '수강 내역' 테이블의 '학번'+'수강학기'+'과목명'을 복합하여 식별자로 두면서 문제를 해결하면 제 1 정규화는 마무리 된다.
!['정규화(2)'](./image/%EC%A0%9C1%EC%A0%95%EA%B7%9C%ED%99%94(2).png)

## 제 2정규화

제 2정규화는 부분함수의 종속 제거이다. 간단하게 말하면 key가 아닌 값들은 모두 key값에 종속되어야 한다는 것이다.

바로 테이블을 통해 보도록 하자.
![제2정규형(1)](./image/%EC%A0%9C2%EC%A0%95%EA%B7%9C%ED%99%94(1).png)
제 1정규형을 마친 '수강내역' 테이블이 있다.

'수강내역'테이블은 '학번 + 수강학기 + 과목명'으로 이루어진 복합키가 존재한다. 여기서 제 2정규형을 만족하려면 성적과 제한인원이 복합키에 종속되어야한다.

성적의 경우 학번, 수강학기, 과목명을 알아야 하지만 '제한인원'의 경우 복합키의 학번과는 관계가 없다.

그래서 한번 더 분리가 가능하다.
![제2정규형(2)](./image/%EC%A0%9C2%EC%A0%95%EA%B7%9C%ED%99%94(2).png)
이렇게 분리하고 나면 테이블이 2개로 나뉜다.
![제2정규형(3)](./image/%EC%A0%9C2%EC%A0%95%EA%B7%9C%ED%99%94(3).png)

## 제3 정규형

제3 정규형은 테이블 내의 모든 속성이 다른 후보키에 의존하지 않아야 한다.

![제3정규형(1)](./image/%EC%A0%9C3%EC%A0%95%EA%B7%9C%ED%98%95(1).png)

학생테이블을 보면 키가 아닌데도 불구하고 전공이 대학 칼럼에 종속적인 관계로 묶여있음을 알 수 있다.

정규화가 잘된 테이블은 갑을관계가 성립되어야지 갑을병과 같이 위아래 관계가 늘어지면 안된다.

그래서 이를 분리시켜 주어야하는데 하나의 대학은 여러개의 전공과를 포함할 수 있어 이는 `one to many`관계가 성립한다.

그러므로 전공을 FK(Foreign Key)로 두고 테이블을 나눠준다.
![제3정규형(2)](./image/%EC%A0%9C3%EC%A0%95%EA%B7%9C%ED%98%95(2).png)
그리고 나누어진 테이블은 다음과 같이 된다.
![제3정규형(3)](./image/%EC%A0%9C3%EC%A0%95%EA%B7%9C%ED%98%95(3).png)

## 정리

순서대로 다시 정렬을 해보면 아래와 같은 순서로 진행된다.

1. 반복되는 행이 있다면 이를 나누어 제거한다.
2. 키가 아닌 값들은 모두 키에 종속되도록 한다.
3. 키가 아닌 값이 다른 키에 종속되는 경우를 제거한다.
