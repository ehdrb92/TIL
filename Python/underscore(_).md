파이썬에서 언더스코어(_)의 쓰임 정리

1. 실행된 마지막 결과값을 저장(인터프리터에서 적용)

    파이썬 인터프리터에선 마지막으로 실행된 결과값이 _라는 변수에 저장된다. 이는 표준 CPython 인터프리터에서 먼저 사용되었으며 다른 파이썬 인터프리터 구현체에서도 똑같이 사용할 수 있다.

    ```
    >>> 10
    10
    >>> _
    10
    >>> _ * 3
    30
    >>> _ * 20
    600
    ```

2. 값을 무시하고 싶을 경우

    _는 또한 어떤 특정값을 무시하기 위한 용도로 사용되기도한다. 값이 필요하지 않거나 사용되지 않는 값을 _에 할당하기만 하면된다.

    ```
    # 언패킹시 특정값을 무시
    x, _, y = (1, 2, 3) # x = 1, y = 3

    # 여러개의 값 무시
    x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5

    # 인덱스 무시
    for _ in range(10):
        do_something()

    # 특정 위치의 값 무시
    for _, val in list_of_tuple:
        do_something()
    ```

3. 특별한 의미의 네이밍을 하는 경우

    파이썬 컨벤션 가이드라인인 PEP8에는 다음과 같은 4가지의 언더스코어를 활용한 네이밍 컨벤션을 소개하고 있다.

    * `_single_leading_underscore`
        
        주로 한 모듈 내부에서만 사용하는 private 클래스/함수/변수/메서드를 선언할 때 사용하는 컨벤션이다. 이 컨벤션으로 선언하게 되면 from module import *시 _로 시작하는 것들은 모두 임포트에서 무시된다. 그러나, 파이썬은 진정한 의미의 private을 지원하고 있지는 않기 때문에 private을 완전히 강제할 수는 없다. 즉, 위와 같은 임포트문에서는 무시되지만 직접 가져다 쓰거나 호출을 할 경우엔 사용이 가능하다. 그래서 “weak internal use indicator"라고 부르기도 한다.

        ```
        _internal_name = 'one_module' # private 변수
        _internal_version = '1.0' # private 변수

        def __init__(self, price):
            self._price = price

        def _double_price(self): # private 메서드
            return self._price * self._hidden_factor

        def get_double_price(self):
            return self._double_price()
        ```

    * `single_trailing_underscore_`

        파이썬 키워드와의 충돌을 피하기 위해 사용하는 컨벤션이다. 그리 많이 사용하지는 않을 것이다.

        ```
        Tkinter.Toplevel(master, class_='ClassName') # class와의 충돌을 피함

        list_ = List.objects.get(1) # list와의 충돌을 피함
        ```

    * `__double_leading_underscores`

        이는 컨벤션이라기보단 하나의 문법적인 요소이다. 더블 언더스코어는 클래스 속성명을 맹글링하여 클래스간 속성명의 충돌을 방지하기 위한 용도로 사용된다. (맹글링이란, 컴파일러나 인터프리터가 변수/함수명을 그대로 사용하지 않고 일정한 규칙에 의해 변형시키는 것을 말한다.) 파이썬의 맹글링 규칙은 더블 언더스코어로 지정된 속성명 앞에 _ClassName을 결합하는 방식이다. 즉, ClassName이라는 클래스에서 __method라는 메서드를 선언했다면 이는 _ClassName__method로 맹글링 된다.

        ```
        class A:
            def _single_method(self):
                pass

            def __double_method(self): # 맹글링을 위한 메서드
                pass

        class B(A):
            def __double_method(self): # 맹글링을 위한 메서드
                pass

        print(dir(A())) # ['_A__double_method', ..., '_single_method']
        print(dir(B())) # ['_A__double_method', '_B__double_method', ..., '_single_method']

        # 서로 같은 이름의 메서드를 가지지만 오버라이드가 되지 않는다.
        ```

        더블 언더스코어로 지정된 속성명은 위와 같이 맹글링이 되기 때문에 일반적인 속성 접근인 ClassName.__method으로 접근이 불가능하다. 간혹, 이러한 특징으로 더블 언더스코어를 사용해 진짜 private처럼 보이게 하는 경우가 있는데 이는 private을 위한 것이 아니며 private으로의 사용도 권장되지 않는다.

    * `__double_leading_and_trailing_underscores__`

        스페셜 변수나 메서드(매직 메서드라고도 부른다.)에 사용되는 컨벤션이며, __init__, __len__과 같은 메서드들이 있다. 이런 형태의 메서드들은 어떤 특정한 문법적 기능을 제공하거나 특정한 일을 수행한다. 가령, __file__은 현재 파이썬 파일의 위치를 나타내는 스페셜 변수이며, __eq__은 a == b라는 식이 수행될 때 실행되는 스페셜 메서드이다. 물론 사용자가 직접 만들 수도 있지만 그런 경우는 정말 거의 없으며, 일부 스페셜 메서드의 경우 직접 수정하거나 하는 일은 빈번히 있을 수 있다. __init__의 경우 클래스의 인스턴스가 생성될 때 처음으로 실행되는 메서드인데 인스턴스의 초기화 작업을 이 메서드의 내용으로 작성할 수 있다.

        ```
        class A:
            def __init__(self, a): # 스페셜 메서드 __init__에서 초기화 작업을 한다.
                self.a = a

            def __custom__(self): # 커스텀 스페셜 메서드. 이런건 거의 쓸 일이 없다.
                pass
        ```

4. 숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때

    Python 3.6에 추가된 문법으로 언더스코어로 숫자값을 좀 더 읽기 쉽도록 자릿수를 구분할 수 있게 되었다.

    ```
    dec_base = 1_000_000
    bin_base = 0b_1111_0000
    hex_base = 0x_1234_abcd

    print(dec_base) # 1000000
    print(bin_base) # 240
    print(hex_base) # 305441741
    ```