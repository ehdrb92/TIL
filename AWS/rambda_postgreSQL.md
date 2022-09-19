# AWS Lambda와 postgreSQL 연결해보기

## Lambda 생성

연결하기위한 Lambda를 생성해준다.

AWS 람다의 대시보드의 화면 오른쪽 상단에 `함수생성` 버튼을 눌러준다.

`새로작성`을 선택한 후 적당한 함수이름을 설정하고, 본인이 구동할 언어에 대해 런타임을 설정해준다.

이번 테스트는 파이썬으로 진행되기 때문에 `python3.9`를 선택해주었다.

## 데이터베이스 및 테이블 생성

이후 해당 Lambda와 연결할 데이터베이스(RDS)를 만들어 준다.

데이터베이스는 RDS페이지로 이동하여 본인의 취향에 따라 MySQL, PostgreSQL 등으로 적당한 프리티어 데이터베이스를 만들어 준다.

해당 테스트에서는 PostgreSQL을 사용하도록 하겠다.

그리고 이번 테스트에서 사용할 테이블을 PostgreSQL shell로 이동하여 명령을 통해 만들어 준다.

```postgresql
CREATE TABLE users (
   id serial PRIMARY KEY,
   username VARCHAR ( 50 ) NOT NULL,
);
```

유저의 이름을 저장하기위한 간단한 테이블 생성

```postgresql
CREATE SEQUENCE users_sequence
  start 1
  increment 1;
```

id값을 순차적으로 저장하기위한 명령어

## Lambda와 데이터베이스 연결

적당한 데이터베이스를 만들었다면, Lambda와 데이터베이스를 연결시켜준다.

둘을 연결시키기 위해서 `psycopg2` 라이브러리를 설치해주어야 한다.

`pip install psycopg2`

여기서 위의 명령어로 psycopg2를 설치하게되면 오류를 맞이할 수 있다.

`ImportError: No module named 'psycopg2._psycopg'`

위와 같은 에러를 맞이하게 되는데 해당 오류가 왜 발생하는 이유는 AWS를 사용할 때 의존성의 문제라고한다.

그렇기에 이를 AWS에서 사용하려면 아래의 명령어로 설치를 해준다.

`pip install aws-psycopg2 -t [설치 디렉토리]`

pip설치가 완료되면 폴더가 생성되는데 `python`이라는 이름의 폴더를 생성하여 해당 폴더안에 옮겨준다.

이유는 이렇게 하지않으면 인식을 하지못한다고 한다.

그리고 python폴더를 압축하여 zip파일로 만들어준다.

람다페이지로 이동하여 Layer(계층)를 생성해준다.

zip파일을 업로드하고, 호환 런타임을 파이썬 버전들로 선택해준 뒤 계층을 생성한다.

생성한 계층을 람다에 연결시켜준다.

그리고 마지막으로 람다의 코드를 입력해주어야 한다.

```python
import psycopg2
from psycopg2.extras import RealDictCursor
import json

host = "lambda.catviomlsl6n.ap-northeast-2.rds.amazonaws.com"
username = "root"
password = "rds120806"
database = "lambda"

conn = psycopg2.connect(
    host = host,
    database = database,
    user = username,
    password = password
)

def lambda_handler(event, context):
    cur = conn.cursor(cursor_factory = RealDictCursor)

    name = event["name"]
    
    cur.execute(f"INSERT INTO users (id, user_name) VALUES (nextval('users_sequence'), '{name}');")
    cur.execute("select * from users")
    
    results = cur.fetchall()
    json_result = json.dumps(results)
    conn.commit()
    return json_result
```

위의 코드는 람다와 데이터베이스를 psycopg2로 연결시켜주고, 유저의 이름을 클라이언트로부터 얻어 데이터베이스에 저장해준다.

예시에서는 데이터베이스의 환경변수를 그대로 하드코딩하였지만, 실제로 배포할 경우에는 환경변수는 따로 저장해준다.

람다의 테스트 케이스를 작성하여 테스트를 진행하면, 데이터가 들어가는 모습을 볼 수 있다.