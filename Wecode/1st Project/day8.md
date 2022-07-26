# 1차 프로젝트 8일차

오늘은 제품 장바구니 기능에 대해 리뷰를 받은 내용을 수정하는 데 많은 시간을 쏟았다. 그리고 받은 리뷰에는 그 동안 알지 못했던 개념들이 많았는데 간략히 정리해보았다.

## valueError : The QuerySet value for an exact lookup must be limited to one result using slicing

오늘 Q객체를 사용하여 특정 조건에 맞는 데이터를 찾아오려는 데 제목과 같은 오류를 마주쳤다.

직역하면, "정확한 조회에 대한 QuerySet 값은 슬라이싱을 사용하여 하나의 결과로 제한되어야 합니다."이다.

문제가 발생한 코드는 아래와 같다.

```python
user_cart         = Q(user=user.id) & Q(order_status=STATUS.CART.value)
user_cart_product = Q(product=Product.objects.get(id=product)) & Q(order=Order.objects.filter(user_cart))
```

이 오류는 왜 생긴 것일까??

내가 이해한 바로는 `Q(order=Order.objects.filter(user_cart)`부분에서 filter로 데이터를 받아오면 QuerySet 형태로 반환되어 특정 조회를 조회하려는게 불가능 하다는 것으로 보인다.

이에 대한 해답을 stackoverflow에서 찾아보았는데,

`Q(order__in=Order.objects.filter(user_cart))`와 같이 변수 뒤에 `__in`을 붙이는 것이었다. 이것이 무엇을 뜻하는 바인지는 모르겠지만 문제는 해결되었다.

## Q객체는 filter 외에 get에도 사용이 가능하다

처음 Q객체에 대해 배웟을 때, 조건 값을 대입하고 이를 filter()를 사용하여 데이터를 불러왔는데, 알고 보니 get에도 사용이 가능하다는 사실을 알아내었다.

## Enum

프로젝트 기획에서 특정 상태를 나타내는 상수를 변수로 지정하고 사용할 일이 많았다.

나는 이를 일일이 상수변수를 지정하여 특정 요청의 로직마다 작성해 주었는데 이를 좀 더 깔끔하게 관리하는 기능을 배웠다.

바로 python Enum 이었다.

```python
from enum import Enum

class STATUS(Enum):
    CART                   = 1
    BEFORE_DEPOSIT         = 2
    PREPARING_FOR_DELIVERY = 3
    SHIPPING               = 4
    DELIVERY_COMPLETED     = 5
    EXCHANGE               = 6
    RETURN                 = 7
```

위의 코드와 같이 Enum 모듈을 가져와 특정 클래스를 만들고 이를 내가 가지고 오고 싶은 형태로 불러올 수 있다.

이에 대한 좀 더 자세한 부분은 프로젝트가 끝난 후 자료를 남기려 한다.

## 마무리

벌써 프로젝트의 종료가 길어야 2일 밖에 남지 않았다. 이제는 남은 기간동안 더 이상은 기능구현은 진짜 힘들고, 기존에 기능을 구현했던 부분에 대해 리팩토링을 진행할 계획이다.

그리고 최종발표에 대한 자료와 발표를 준비할 시간이 필요하기에 마지막까지 바쁜 일정을 소화해야 할 것 같다.

이번 1차 프로젝트를 수행하며 아쉬운 점이 많았다. 하지만 너무 자책하지 말고 마지막까지 힘내서 좀 더 좋은 결과를 낼 수 있도록 힘내도록 해야겠다.