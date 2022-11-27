## Django save()와 create()

1. save는 INSERT/UPDATE, create는 INSERT 쿼리문을 수행한다. save는 pk값이 이미 존재하는 데이터를 삽입할 때 UPDATE를 그렇지 않은 경우 INSERT를 수행한다.
2. create의 경우 pk값이 존재하는 데이터를 중복해서 삽입할려고 하면 IntegrityError를 발생시킨다.
3. save에 force_insert=True 옵션을 줄 경우 create와 같은 기능이 된다.
4. save는 작업을 마친 후 None을 반환하지만 create는 만들어진 객체를 반환한다.

Django create의 소스코드는 다음과 같다.

```python
def create(self, **kwargs):
    """
    Create a new object with the given kwargs, saving it to the database
    and returning the created object.
    """
    obj = self.model(**kwargs)
    self._for_write = True
    obj.save(force_insert=True, using=self.db)
    return obj
```