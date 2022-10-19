# ManyToManyField

장고 프레임워크를 사용하여 데이터베이스를 작성할 때 다대다 관계를 정의할 때 편리한 메소드인 `ManyToManyField`에 대해 알아보자.

해당 메소드는 다대다 관계의 테이블을 작성할 때 무조건적으로 사용하면 좋은 기능이다. 왜냐하면 원래 다대다 관계에는 중간에 서로를 이어줄 테이블이 별도로 필요한데, 이를 수동으로 직접 작성할 필요가 없어진다. 간단한 명령어만 사용하면 장고가 자동으로 테이블을 생성시킨다. 사실상 ManyToManyField를 사용한 동시에 테이블이 생성되는 것이고, 명령어로 테이블의 데이터를 생성한다.

```python
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = ['movie']

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie) # ManyToManyField

    class Meta:
        db_table = ['']

    def __str__(self):
        return self.name
```

코드를 살펴보면 `publications` 변수에 메소드가 붙은 모습을 볼 수 있다. 어차피 위에 정의된 두 개의 테이블은 다대다 관계이기 때문에 메소드가 어디 달려있든 크게 상관은 없는 것으로 보인다. 그저 참조, 역참조관게만 좀 바뀔뿐이다.

```python
m1 = '다만 악에서 구하소서'
m2 = '신세계'
m3 = '곡성'

a1 = '이정재'
a2 = '황정민'
a3 = '최민식'
```

위와 같이 변수로 지정하고, 각 movie와 table에 데이터를 저장했다고 하자. 그리고 이들을 명령어를 통해 간단히 연결시킬 수 있다.

```python
a1.movies.add(m2)
a2.movies.add(m1, m2, m3)
a3.movies.add(m2)
```

이러면 다대다 관계를 이을 수 있는 데이블이 자동으로 생성된다. 그리고 이들의 관계 또한 명령어를 통해 확인할 수 있다.

```python
a1.movies.all() # <QuerySet [<Movie: 신세계>]>
a2.movies.all() # <QuerySet [<Movie: 신세계>], [<Movie: 다만 악에서 구하소서>, [<Movie: 곡성>]]>
a3.movies.all() # <QuerySet [<Movie: 신세계>]>
```

각 데이터의 참조 관계에 대해 쿼리셋으로 반환한다. 그리고 역참조 또한 가능하다.

```python
m1.actor_set.all() # <QuerySet [<Actor: 황정민>]>
m2.actor_set.all() # <QuerySet [<Actor: 이정재>], [<Actor: 황정민>], [<Actor: 최민식>]>
m3.actor_set.all() # <QuerySet [<Actor: 황정민>]>
```

이외에도 다양한 기능들이 있지만 일단은 가장 자주 쓰이는 명령어만 알아보았다. 그런데 ManyToManyField를 사용할 때 주의할 점이 있는데, 해당 메소드로 장고가 자동으로 생성한 테이블은 임의로 속성을 바꾸는 등 관리하기가 까다롭다고 한다. 그래서 이를 관리하기 쉬운 방법이 있는데 테이블을 따로 생성해 주고, ManyToManyField가 이를 바라보도록 하는 방법이다.

```python
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = ['movie']

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, through='MovieActor', related_name='actor') # ManyToManyField

    class Meta:
        db_table = ['']

    def __str__(self):
        return self.name

class MovieActor(model.Model):
    movie = models.ForeignKey('Actor', on_delete=models.CASCADE)
    actor = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_actor'
```

별도로 다리 테이블을 만들어 준 다음 ManyToManyField에 through 속성을 사용하여 MovieActor 테이블을 바라보도록 하였다. 이렇게 해주면 장고가 테이블을 별도로 생성하지 않고, 사용자가 직접 만들어준 테이블에 데이터를 생성하게 된다. 그러면 ManyToManyField의 간편한 명령어 기능은 사용할 수 있고, 테이블을 관리하기도 쉬워진다.

그리고 한 가지 편리한 기능이 한가지 더 있는데 우리가 위에서 역참조를 사용할 때 `참조하는 테이블명_set`을 사용하였는데 related_name 속성을 사용하면, `인자.related_name.메소드`를 사용하여 자신이 지정한 이름으로 좀 더 커스터마이징할 수 있다.
