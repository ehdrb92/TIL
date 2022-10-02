**Linked list(연결 리스트)**란 각 노드가 데이터와 포인터를 가지고 연결된 구조이다.

여기서 노드란 특정 데이터를 담은 그릇과 같은 것이라고 생각하면 된다.

프로그래밍 언어에서 클래스가 노드라고 생각해도 무방하다.

포인터는 해당 노드와 연결된 다른 노드를 가르키는 주소를 담은 데이터이다.

방식에 따라 노드는 포인터를 하나 또는 두 개까지 가질 수 있다.

포인터를 하나만 가지는 방식은 다음에 올 노드의 주소만 가진다.

하지만 포인터를 두 개 가지는 노드는 자신의 앞, 뒤 두 개 노드에 대한 주소를 가지고 있다.

## 배열과 차이점

연결 리스트의 경우 배열과 유사하지만 차이점이 존재한다.

1. 배열은 메모리에서 데이터의 논리적, 물리적 주소가 순차적으로 저장된다. 하지만 연결 리스트의 경우 논리적 주소만 순차적으로 진행될 뿐 물리적 주소는 순차적이지 않을 수 있다.

2. 배열은 index를 가지고 있어 indexing을 통해 빠르게 특정 데이터에 접근이 가능하다. 하지만 연결 리스트의 경우 특정 데이터를 찾기 위해 노드의 포인터를 따라가며 찾아야 한다.

3. 배열은 데이터를 삽입/삭제할 때 해당 데이터 이외에 다른 데이터를 같이 이동하는 많은 작업이 동반될 수 있다. 하지만 연결 리스트의 경우 논리적 주소만 신경쓰면 되기 때문에 많은 작업이 필요치 않다.

4. 동일한 양의 데이터를 저장했을 때 연결 리스트의 경우 각 노드가 데이터 뿐만 아니라 토인터에 대한 물리적 공간도 같이 할당받아야 하기 때문에 많은 메모리를 차지하게 된다.

## 활용

- 데이터의 양이 많지 않고, 데이터의 삽입/삭제하는 경우가 많은 경우 연결 리스트를 사용하는 것이 유리하다.