# 1차 프로젝트 6일차

1차 프로젝트 1주차 주말동안 위와 같이 장바구니 기능을 하는 api를 작성해 보았다.

전체적으로 코드가 복잡하게 짜여 있지만, 서버측에서 자체적으로 기능 구현에 대한 테스트는 정상적으로 작동하는 것을 확인하였다.

## GET

```python
class CartView(View):
    @login_decorator
    def get(self, request):
        '''
        카트 상태의 상품 조회

        - 장바구니 모달창 또는 장바구니 페이지로 이동시 해당 유저의 장바구니 상품 조회
        - http://localhost:8000/orders/cart
        '''
        user = request.user
        CART_STATUS = 1

        user_cart = Order.objects.filter(user=user.id).get(order_status=CART_STATUS).orderitem_set.all()

        result = [{
            'title'   : order.product.title,
            'price'   : order.order_price,
            'quantity': order.order_quantity,
            'picture' : order.product.productimage.main_url
        } for order in user_cart]

        return JsonResponse({'result' : result}, status = 200)
```

해당 뷰의 get은 클라이언트 측에서 로그인한 유저가 장바구니 목록을 불러오려고 할 때 요청을 받는 로직이다.

로그인 데코레이터를 통하여 jwt 인증을 통해 접속한 유저의 id정보를 받아오고, 해당 정보를 토대로 `orders` 테이블에서 유저의 주문 데이터 중 장바구니 상태의 주문을 불러온다. 그리고 해당 주문에서 `order_items`테이블로 역참조해서 장바구니 물건을 가져오는 로직이다.

이 로직은 이전부터 많이 구현해 보던 부분이라 별다른 어려움을 느끼지는 못했던거 같다.

## POST

```python
    @login_decorator
    def post(self, request):
        '''
        제품 카트에 담기

        - 웹 사이트 상에서 `ADD TO CART` 버튼 클릭 시 카트에 해당 상품을 담기
        - http://localhost:8000/orders/cart
        '''
        try:
            data = json.loads(request.body)

            user        = request.user
            product     = data['product']
            CART_STATUS = 1

            selected_product = Product.objects.get(id=product)
            

            if Order.objects.filter(user=User.objects.get(id=user.id), order_status=CART_STATUS).exists():
                if OrderItem.objects.filter(product=product, order=Order.objects.filter(user=user.id).get(order_status=CART_STATUS).id).exists():
                    ordered_item = OrderItem.objects.filter(product=product, order=Order.objects.filter(user=user.id).get(order_status=CART_STATUS).id)
                    ordered_item.update(order_quantity=OrderItem.objects.filter(product=product).get(order=Order.objects.filter(user=user.id).get(order_status=CART_STATUS).id).order_quantity + 1)
                else:
                    OrderItem.objects.create(
                        product        = selected_product,
                        order          = Order.objects.get(user=user.id),
                        order_quantity = 1,
                        order_price    = selected_product.price
                    )
            else:
                Order.objects.create(
                    user         = User.objects.get(id=user.id),
                    order_status = OrderStatus.objects.get(id = CART_STATUS)
                )
                OrderItem.objects.create(
                    product        = selected_product,
                    order          = Order.objects.get(user=user.id),
                    order_quantity = 1,
                    order_price    = selected_product.price
                )

            items = OrderItem.objects.filter(order__user_id=user)

            result = [{
                'title'   : item.product.title,
                'price'   : item.order_price,
                'quantity': item.order_quantity,
                'picture' : item.product.productimage.main_url
            } for item in items]
   
            return JsonResponse({'result' : result}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
```

가장 골머리를 앓았던 부분이다. 웹 페이지 상에서 `ADD TO CART`라는 버튼을 클릭하면 클라이언트가 카트에 해당 물품을 저장하는 로직이다.

그런데 여기서 장바구니 상태의 주문 존재여부, 장바구니 상태의 해당 물품 존재여부에 따라서 여러갈래로 분기를 하는 양상을 띠다 보니 코드가 전체적으로 좀 복잡해진 경향이 있다.

거기다가 해당 로직을 구현함에 있어 서로 참조하는 관계가 많다보니 참조 관계를 이어주느라 좀 고생을 하였다. 잘 맞았다고 생각해서 로직을 테스트하면 실수 투성이라 에러가 많이 발생하였다.

당장의 기능 구현에는 성공하였지만, 구현이 중요한게 아니다. 위의 복잡한 코드를 어떻게 하면 간결하고 가독성이 좋게 짤 수 있을까??? 남은 프로젝트 기간동안 고민이 필요할 듯하다.

## PETCH

```python
    @login_decorator
    def patch(self, request):
        '''
        장바구니에 올라간 상품 수량 증감

        - 웹 사이트의 장바구니 모달창 또는 장바구니 페이지에서 '+', '-' 버튼으로 상품 개수 증감
        - http://localhost:8000/orders/cart
        '''
        try:
            data = json.loads(request.body)

            user        = request.user
            product     = data['product']     # 해당 제품 product_id 값
            calculation = data['calculation'] # 제품을 더할 것인지, 뺄 것인지 구분 (1 = 더하기, 0 = 빼기)
            CART_STATUS = 1

            pick_products = OrderItem.objects.filter(order=Order.objects.filter(user=user.id).get(order_status=CART_STATUS), product=product)
            pick_product  = OrderItem.objects.filter(order=Order.objects.filter(user=user.id).get(order_status=CART_STATUS)).get(product=product)

            if calculation == 1:
                pick_products.update(
                    order_quantity=(pick_product.order_quantity + 1) # 상품 개수 증가
                )
            elif calculation == 0:
                pick_products.update(
                    order_quantity=(pick_product.order_quantity - 1) # 상품 개수 감소
                )

            result = {'order_quantity' : OrderItem.objects.filter(order=Order.objects.filter(user=user.id).get(order_status=CART_STATUS)).get(product=product).order_quantity}

            return JsonResponse({'result' : result}, status = 200)
        
        except OrderItem.DoesNotExist:
            return JsonResponse({'message' : 'DATA_NOT_EXIST'}, status = 400)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
```

전체 페이지에서 모달창의 형태로 장바구니를 열거나, 별도의 장바구니 페이지에 접속하여 장바구니에 들어있는 상품들의 수량을 조절하는 로직이다.

해당 로직 또한 복잡한 참조관계 덕분에 위와 같이 지옥의 가독성을 보여주는 코드가 작성되었다.

이 또한 추후에 리팩토링에 중점을 두도록하자....

그리고 조건문을 통해 분기한 후 특정 데이터에 접근하여 숫자값을 연산해주는 과정이 있는데, 처음에는 당연히 안될 것이라 생각하여 헤메고 있었다.

그러다가 쉘을 통하여 테스트를 해보았는데, 가능하다는 사실을 알게되어 코드를 작성할 수 있었다....

역시 개발자는 생각할 시간에 쉘을 통해 한번이라도 더 테스트 해보는 중요성을 알게 된 순간이였다.

## DELETE

```python
    @login_decorator
    def delete(self, request, product):
        '''
        장바구니에 올라간 상품 삭제
        
        - http://localhost:8000/orders/cart
        '''
        try:
            user = request.user
            CART_STATUS = 1

            OrderItem.objects.filter(order=Order.objects.filter(user=user.id).get(order_status=CART_STATUS).id, product=product).delete()

            return JsonResponse({'message' : 'SUCCESS'}, status = 200)

        except OrderItem.DoesNotExist:
            return JsonResponse({'message' : 'DATA_NOT_EXIST'}, status = 400)
```

마지막으로 장바구니의 상품을 삭제하는 기능이다. 별 달리 설명할 사항은 없다. 그냥 타겟 상품을 참조관계를 통해 찾아내어 삭제하는 기능이다.