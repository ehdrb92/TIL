# 파이썬 코드 실행 속도 측정하기

개발에 입문하면서 항상 듣는 말이 코드의 가독성과 효율성에 관한 것이다.

가독성은 짜여진 코드에 대한 별도의 설명이 없어도 뭘 하려는 건지 알 수 있는 것이다.

그러면 효율성이란 무엇일까?? 효율성이란 말에는 많은 의미가 내포되어 있겠지만 실행속도 또한 포함될 것이다.

그래서 코드의 실행시간은 어떻게 하면 알 수 있을까 궁금했다.

방법은 아래와 같다.

```python
import timeit
 
start_time = timeit.default_timer() # 시작 시간 체크
 
sum = 0
 
for i in range(100000000):
    sum += i
    
terminate_time = timeit.default_timer() # 종료 시간 체크
 
print("%f초 걸렸습니다." % (terminate_time - start_time))
```

timeit 내장 모듈을 가져와서 위의 예제와 같이 실행시켜주면 코드의 실행시간을 알려줄 것이다.