# ORM

ORM이란 `Object-Relation Mapping`의 약자로 객체와 관계형 데이터를 연결시켜주는 시스템을 말한다. 데이터베이스의 테이블과 프로그래밍 언어의 객체를 연결하여 SQL 쿼리를 사용하지 않고 테이블에 CRUD(Create Read Update Read)를 할 수 있게 해주는 시스템이다. 해당 시스템을 사용하여 장고 명령어를 사용하여 테이블을 조작하는 명령어들에 대해 알아보았다.

## QuerySet으로 반환되는 경우

장고 명령어를 사용하여 데이터베이스의 데이터를 가져올 때 여러개의 데이터를 가지고 올 수 있다. 이때 QuerySet이라는 리스트의 형태로 반환하게 된다.

### all()

특정 테이블의 모든 데이터를 가지고 온다.

```shell
In : Category.objects.all()
Out : <QuerySet [<Category: Category object (2)>, <Category: Category object (3)>, <Category: Category object (4)>, <Category: Category object (5)>, <Category: Category object (6)>, <Category: Category object (7)>]>
```

### filter() & exclude()

특정 테이블에서 조건에 부합하는 데이터를 가지고 오거나, 제외하고 가지고 온다.

```shell
In : Category.objects.filter(name='브루드커피')
Out : [<Category: Category object (3)>, <Category: Category object (4)>]

In : Category.objects.filter(name='브루드커피').filter(id=3)
Out : [<Category: Category object (3)>]

In : Category.objects.filter(name='브루드커피').exclude(id=3)
Out : [<Category: Category object (4)>]
```

### values()

모델 인스턴스가 아닌 dictionary을 포함하는 QuerySet을 반환한다.

```shell
In : Category.objects.filter(name='브루드커피')
Out : [<Category: Category object (3)>, <Category: Category object (4)>]

In : Category.objects.filter(name='브루드커피').values()
Out : <QuerySet [{'id': 3, 'name': '브루드커피'}, {'id': 4, 'name': '브루드커피'}]>
```

### values_list()

dictionary를 반환하는 대신 반복 될 때 튜플을 반환한다.

```shell
In : Category.objects.filter(name='브루드커피').values_list()
Out : <QuerySet [(3, '브루드커피'), (4, '브루드커피')]>
```

## QuerySet으로 반환되지 않는 경우

단일의 데이터를 가지고 올 때의 경우이다.

### create()

테이블에 데이터를 추가 해주는 메소드로, 생성된 인스턴스를 반환한다.

```shell
In : category = Category.objects.create(name='콜드브루')
In : category.name
Out : '콜드브루'
```

### get()

지정된 조회 매개 변수와 일치하는 인스턴스를 반환한다.

```shell
In : Category.objects.get(id=1)
Out : <Category: Category object (1)>
```

### update()

지정된 필드에 대해 업데이트 쿼리를 수행하고 일치하는 행 수를 반환한다.

```shell
In : Category.objects.filter(name='탄산').update(name='콜드브루')
Out : 2
```

### delete()

QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고 삭제 된 개체 수와 개체 유형별 삭제 횟수가 있는 dictionary를 반환한다.

```shell
In : Category.objects.filter(name='qp').delete()
Out : (1, {'products.Category': 1})
```

### save()

추가 또는 수정을 수행하는 메소드로, 단일 객체에 대해서 업데이트를 수행할 때 많이 사용한다.

```shell
In : category = Category.objects.get(id=2)
Out : <Category: Category object (2)>

In : category.name
Out : '브루드커피'

In : category.name = 'new name'
In : category.save()

In : category.name
Out : 'new name'
```

### exist()

filter()와 함께 서용해서 filter 조건에 맞는 데이터가 있는지 조회, 존재하면 True 존재하지 않으면 False를 반환한다.

```shell
In : Category.objects.filter(name='브루드커피').exists()
Out : True
```
