# Transaction

transaction은 장고에서 제공하는 예외상황에 대한 롤백기능이다.

tracsaction을 적용한 코드가 예외상황 발생 없이 정상적으로 작동한다면, 코드의 모든 명령이 데이터베이스에 커밋된다.

하지만 중간과정 중 예외가 발생할 경우 진행이 중지되고, 이제까지 데이터베이스에 커밋되었던 모든 내용이 롤백된다.

## Transaction 적용

```python
from django.db import transaction

def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()

    with transaction.atomic():
        # This code executes inside a transaction.
        do_more_stuff()
```

또한 decorator로 적용이 가능하다.

```python
from django.db import transaction

@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()
```
