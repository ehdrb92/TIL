# Django에서 View 클래스

![djagoview](./image/django_as_view(1).png)

이제까지 장고 앱의 view.py에서 특정 함수 로직을 작성할 때 시키는데로만 하다보니 View클래스를 아무생각없이 사용해왔다. 그래서 이번에는 이것을 사용하는 이유에 대해 알아보고자 한다.

```python
# Django source code

class View:
    """
    Intentionally simple parent class for all views. Only implements
    dispatch-by-method and simple sanity checking.
    """

    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def __init__(self, **kwargs):
        """
        Constructor. Called in the URLconf; can contain helpful extra
        keyword arguments, and other things.
        """
        # Go through keyword arguments, and either save their values to our
        # instance, or raise an error.
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classonlymethod
    def as_view(cls, **initkwargs):
        """Main entry point for a request-response process."""
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError(
                    'The method name %s is not accepted as a keyword argument '
                    'to %s().' % (key, cls.__name__)
                )
            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r. as_view "
                                "only accepts arguments that are already "
                                "attributes of the class." % (cls.__name__, key))

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            self.setup(request, *args, **kwargs)
            if not hasattr(self, 'request'):
                raise AttributeError(
                    "%s instance has no 'request' attribute. Did you override "
                    "setup() and forget to call super()?" % cls.__name__
                )
            return self.dispatch(request, *args, **kwargs)
        view.view_class = cls
        view.view_initkwargs = initkwargs

        # take name and docstring from class
        update_wrapper(view, cls, updated=())

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        update_wrapper(view, cls.dispatch, assigned=())
        return view
    ..
    ..
    
GET ,POST ,PATCH -> get, post, patch
    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    ..
    ..
```

장고의 소스 코드를 뒤져보면 클래스 View가 어떤 식으로 구성되어 있는지 한눈에 볼 수 있다.

우선 우리가 클라이언트로 부터 요청을 받으면 URLconf를 통해 url구조를 파악해 어떤 로직으로 동작이 진행을 할지 정하게 된다.

![django_as_view](./image/django_as_view(2).png)

그 중 as_View라는 메소드가 호출되게 되면 복잡한 내부 로직을 통해 마지막에 dispatch 메소드를 반환한다.

그러면 dispatch 메소드는 클라이언트로 받은 GET, POST, PATCH 등의 요청을 소문자로 변환하여 http_method_names 리스트를 탐색하여 적절한 요청인지를 판별한 이후 handler로 반환한다.

그러면 우리가 작성한 view.py로 가서 짜여진 함수 중 하나가 실행되는 것이다.
