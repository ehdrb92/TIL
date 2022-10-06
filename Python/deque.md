파이썬에는 큐와 스택 자료구조를 손쉽게 만들어 주는 deque 자료형이 있다.

```python
from collections import deque

str = "abc de fg"

dq = deque(str)

deque(['a', 'b', 'c', ' ', 'd', 'e', ' ', 'f', 'g'])
```

위와 같이 모듈을 가져와서 문자열을 뒤집어 씌워주면 각 문자가 하나씩 쪼개어져 나오게 된다.