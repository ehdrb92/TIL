# 1차 프로젝트 4일차

## 데이터모델링 기획의 중요성

오늘은 대부분의 시간을 데이터모델링을 생각하는데 다 소진했다... 기존에는 상품 카테고리의 관계 테이블 형태를 주가 되는 메인 테이블과 해당 테이블을 1:# 관계로 참조하는 서브 카테고리로 나누었다. 그리고 서브 카테고리와 상품 테이블을 #:# 관계로 연결 시켜주었다.

그런데 이후 특정 페이지의 로직을 구성하는데 해당 관계 모델이 너무 불편했다. 그래서 생각 끝에 메인과 서브 카테고리를 하나의 카테고리 테이블로 통합하는 방향으로 모델링 기획을 틀게 되었다. 이 과정에서 이미 만들어져 있던 migration과 해당 테이블들에 맞게 데이터를 만들어 두었던 csv파일들을 모두 수정하려니 생각보다 많은 시간이 소모되었다.

그리고 초기에 기획했던 모델링으로 이미 원격 저장소에 병합이 되었고, 팀원은 해당 모델링으로 작업을 하고 있었다. 이들을 모두 다시 새로 변경하려니 git을 사용하는 데에서도 많은 어려움들이 생겼다. 왜냐하면 이제까지는 각자가 자신의 기능을 개발하는 바에 맞게 모델링을 하고 있었기 때문이다. 그래서 충돌이 빈번히 발생하였다.

이 과정에서 특정 기획에 맞는 데이터베이스의 전체 모델링을 하는 작업은 보통 한 사람이 도맡아서 하는 편이 관리에 매우 용이하다는 사실을 알게되었다.