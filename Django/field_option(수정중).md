# Field option

장고 modeling을 통해 테이블 생성 시 데이터에 적용시킬 수 있는 옵션

`Null` : 만약 True로 설정된다면 해당 데이터는 Null값이 적용 가능하다. 기본값은 False

`Blank` : 만약 True로 설정된다면 해당 데이터는 공백으로 적용 가능하다. 기본값은 False

* Null과 Blank 속성 둘 다 값이 없다는 걸 의미하는 것 같은데 헷갈려서 찾아보니 `DateTimeField`, `ForignKey`와 같은 값은 없으면 Null로 지정되고 `CharField`, `TextField`와 같은 값들은 Blank로 저장된다고 한다.

`db_column` : column의 값을 지정한 변수의 이름이 아닌 다른 닉네임으로 사용하고 싶을 때 사용한다. (사용할 일이 있을지 의문이다...)

`db_index` : True로 설정할 경우 해당 column을 index로 설정한다고 한다. 이게 정확하게 무엇을 의미하는지는 모르겠다. 찾아본 바에 의하면 특정 데이터를 찾는 요청이 들어올 때 index column을 중심으로 탐색을 한다는 말이 있는데 좀 더 알아봐야 할 듯하다.

`db_tablespace` : 