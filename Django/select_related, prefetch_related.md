메인 주제인 select_related와 prefetch_related에 대해 알기 전 선수적으로 알아야 할 개념들을 먼저 알고 가도록하자.

#### 지연 로딩(Lazy-Loading)

지연 로딩은 Django ORM이 실제 데이터 처리가 필요한 순간에만 쿼리 문을 실행하는 것이다. 단순히 ORM이 선언했다고 해서 그 순간 쿼리문이 실행되지 않는다.

쿼리문이 실행되는 예시는 아래와 같다.

1. Slicing
2. Picking, Caching
3. __repr__()
4. len()
5. list()
6. bool()

#### 즉시 로딩(Eager-Loading)

즉시 로딩은 지연 로딩과 반대되는 개념이다. 지연 로딩의 경우 ORM이 실행되는 순간마다 필요한 쿼리문을 실행하여 데이터를 가지고 오는 구조라면, 즉시 로딩의 경우 당장 필요없는 쿼리문도 한꺼번에 같이 가져오는 개념이다.

#### 캐싱(Caching)

Django는 Queryset Caching을 지원한다. ORM을 통해 메인 쿼리로 한번 실행되어 가져온 데이터의 경우에는 해당 데이터들이 저장되기 때문에 해당 데이터에 대한 ORM을 실행하면 쿼리를 실행하지 않고 데이터를 가져올 수 있다.

여기서 한 가지 더 짚고 넘어가야할 중요한 점이 있다. **"Django에서 Queryset은 하나의 쿼리와 추가적으로 N개의 쿼리를 가진다"** 이는 추후의 개념을 설명할 때도 중요한 개념이니 꼭 알아두도록 하자.

#### N+1 Problem

Django ORM은 기본적으로 지연 로딩방식을 채택하고 있다. 이 때문에 외래키를 참조하여 데이터를 가지고 올 때 문제가 발생한다.

```python
class City(models.Model):
    # ...
    pass

class Person(models.Model):
    # ...
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

people = Person.objects.all()

for person in people:
    person.city.name
```

위와 같은 참조 관계를 가진 두 테이블에서 Person 테이블에서 참조한 City 테이블의 정보를 가져오려 할 경우 먼저 쿼리셋으로 이미 선언된 Person 테이블의 정보를 가져오는 쿼리를 한번 수행하게 되고 이는 캐싱되어 루프를 통해 반복하더라도 쿼리를 계속해서 호출하지 않는다. 하지만 City 테이블의 경우 쿼리셋으로 선언되지 않았기 때문에 매번 쿼리문을 호출하며 불필요한 쿼리를 만들게 된다.

이러한 문제를 해결하기 위해 Django에서는 즉시 로딩을 지원하는 select_related와 prefetch_related를 제공한다.

#### select_related

특정 테이블을 참조하고있는 테이블에서 사용하여 참조하는 테이블의 데이터를 조인하여 가져올 수 있는 코드이다. 데이터베이스상에서 쿼리문을 통해 테이블을 직접 조인하게 된다.

```python
from django.db import models

class City(models.Model):
    # ...
    pass

class Person(models.Model):
    # ...
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

class Book(models.Model):
    # ...
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
```

위와 같은 테이블 관계가 있을 때, `Book.objects.select_related('author__hometown').get(id=4)`를 사용하면, Book 테이블에서 id값이 4인 Person, City 테이블의 정보를 조인시킨다. 그러면 해당 객체를 사용하여 데이터를 가져올 때는 데이터베이스의 참조관계를 들어가 조회하는 쿼리문을 사용하지 않게 되어 이를 최적화시키게 된다.

select_related는 정참조의 ForeignKey를 가진 테이블에서 다른 테이블을 조인하거나 OneToOneField로 연결된 테이블을 조인 시킬 때 사용된다. 역참조는 허용되지 않는다. OneToOneField로 연결된 테이블 끼리의 조인은 역참조 또한 사용가능하다.

#### prefetch_related

이 방식은 select_related와 다르게 쿼리문을 통해 테이블을 직접 조인하는 방식이 아니다. Django의 캐싱을 활용하여 불필요한 쿼리문을 줄이는 방식이다.

```python
cities = City.objects.all().prefetch_related("person_set")

for city in cities:
    city.person_set.name
```

위와 같은 테이블 예제에서 cities 변수에 prefetch_related를 사용하여 관계지어 해당 쿼리를 호출하면 City 테이블 뿐만아니라 Person 테이블도 함께 캐싱되게 된다. 그래서 해당 캐싱된 데이터를 불러올 때마다 쿼리문을 호출하지 않아도 되도록 최적화하는 방식이다.

prefetch_related의 경우 정참조와 역참조를 가지지 않고 모든 경우에서 사용할 수 있다.