# 1차 프로젝트 5일차

```python
from django.views import View
from django.http import JsonResponse

from products.models import Product

class ProductView(View):
    def get(self, request):
        category = int(request.GET.get('category', 1))
        offset   = int(request.GET.get('offset', 0))
        limit    = int(request.GET.get('limit', 0))
        sort     = int(request.GET.get('sort', 0))

        products = Product.objects.filter(categoryproduct__category_id=category)

        if sort == 0:
            sorted_products = products.order_by('-issue_number')
        elif sort == 1:
            sorted_products = products.order_by('issue_number')
        elif sort == 2:
            sorted_products = products.order_by('-price')
        elif sort == 3:
            sorted_products = products.order_by('price')

        result = [
            {
                'title'         : product.title,
                'issue_number'  : product.issue_number,
                'main_category' : product.category.get(id=category).name,
                'price'         : product.price,
                'main_img_url_1': product.productimage.main_url,
                'main_img_url_2': product.productimage.sub_url,
            }
            for product in sorted_products[offset:limit]]

        result.append(
            {
                'category_total' : len(products)
            }
        )

        return JsonResponse({'result' : result}, status = 200)
```

제품 전체 리스트 페이지에 대한 코드를 대대적으로 수정하였다. 이전 코드에 대해 어떤 부분을 어떤 이유에서 수정하였는지 정리를 해보았다.

## limit, offset

이번 프로젝트에서 기획한 제품의 페이지 리스트에서는 클라이언트가 요구하는 상품의 개수로 나누어서 상품의 리스트 페이지가 구성되도록 하는 것이었다. 그래서 처음에는 클라이언트로 부터 `page_size`라는 변수에 원하는 페이지의 개수를 담아 서버측에서 연산을 하여 `limit`, `offset`을 정하고 이에 따라 슬라이싱을 하여 데이터의 수량을 맞게 전송해 주는 것이었다.

그런데 멘토님의 의견은 현재 현업에서 통용적으로 사용되는 방식은 `limit`, `offset`을 클라이언트 측에서 연산하여 보내주는 것이라고 하였다.

그래서 위와 같이 코드를 수정하여 클라이언트 측으로 부터 쿼리 파라미터의 매개변수로 받도록 하였고, 프론트 개발자 측에도 이를 전달하였다.

## 상품 필터 기능

위의 코드를 살펴보면 `sort`변수를 클라이언트 측으로 부터 받아온다. 이는 상품 리스트를 특정 원하는 방식으로 정렬하는 기능을 구현하기 위해서이다.

sort 변수에 특정 숫자 값을 받아와 발행번호의 오름, 내림차순 그리고 가격의 오름, 내림차순으로 정렬을 할 수 있도록 코드를 작성하였다. 기능 구현은 제대로 되는 것을 테스트해보았다. 하지만 보기엔 코드가 뭔가 하드코딩이 된거 같아 보여 마음에 들지 않았다.

그래서 더 깔끔하게 기능을 구현할 수 있는 코드를 찾아보았지만 아직은 찾지 못하였다. 좀 더 이에 대해 살펴보는 시간이 필요할 듯하다.

## 가독성과 효율성 향상을 위한 코드 로직

기존에 `result`배열에 원하는 데이터 정보를 넣을때는 for 반복문과 append 기능을 사용하여 코드를 작성하였다. 하지만 코드의 가독성과 속도면에서 파이썬의 리스트 표현식을 사용하는 방식이 효율적이라는 피드백을 받았다.

```python
for product in sorted_products[offset:limit]:
    result.append(
        {
            'title'         : product.title,
            'issue_number'  : product.issue_number,
            'main_category' : product.category.get(id=category).name,
            'price'         : product.price,
            'main_img_url_1': product.productimage.main_url,
            'main_img_url_2': product.productimage.sub_url,
        }
    )
```

그래서 위와 같은 기존의 코드를 수정하여 리스트 표현식으로 상품의 데이터 정보를 담도록 수정하였다. 내가 보기엔 위도 가독성이 크게 나쁘지는 않아 보이지만.... 아무래도 업계에 좀 더 오래 있었던 사람의 말을 듣는게 맞을거 같다. 그리고 코드의 속도에 대한 말씀을 하셨는데 이에 대한건 어떻게 테스트 해볼 수 있는지를 알아봐야겠다.
