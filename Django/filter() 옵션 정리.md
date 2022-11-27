* exact(iexact): (대소문자를 가지지 않고)정확히 일치하는 데이터 조회

    Entry.objects.get(id__exact=14) # id값이 정확히 14
    Entry.objects.get(id__exact=None) # id값이 None == Null
    Blog.objects.get(name__iexact='beatles blog')

* contains(icontains): (대소문자를 가리지 않고)문자를 포함하는 데이터 조회

    Entry.objects.get(headline__contains='Lennon')

* in: list, tuple, string 또는 queryset과 같이 iterable한 객체를 대상으로 각 원소를 조회

    Entry.objects.filter(id__in=[1, 3, 4])
    : SELECT ... WHERE id IN (1, 3, 4);

    Entry.objects.filter(headline__in='abc')
    : SELECT ... WHERE headline IN ('a', 'b', 'c');

    inner_qs = Blog.objects.filter(name__contains='Cheddar')
    entries = Entry.objects.filter(blog__in=inner_qs)
    :SELECT ... WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%')

* gt, gte, lt, lte: 부등호를 사용한 비교

    Entry.objects.filter(id__gt=4)
    : SELECT ... WHERE id > 4;

    Entry.objects.filter(id__gte=4)
    : SELECT ... WHERE id >= 4;

    Entry.objects.filter(id__lt=4)
    : SELECT ... WHERE id < 4;

    Entry.objects.filter(id__gt=4)
    : SELECT ... WHERE id <= 4;

* startswith, istartswith, endswith, iendswith: 각각 접미사, 접두사를 조회

    Entry.objects.filter(headline__startswith='Lennon') # Lennon으로 시작하는 데이터
    Entry.objects.filter(headline__endswith='Lennon') # Lennon으로 끝나는 데이터

* range: 범위에 해당하는 데이터 조회

    import datetime
    start_date = datetime.date(2005, 1, 1)
    end_date = datetime.date(2005, 3, 31)
    Entry.objects.filter(pub_date__range=(start_date, end_date))