# Unit Test란?

**유닛 테스트**란, 소스 코드의 특정 모듈이 개발자가 의도한 대로 정확히 작동하는지 검증하는 절차를 말한다.
유닛 테스트를 통해 각 개별의 기능별로 테스트 케이스를 작성하여 검사하기 때문에 추후 코드의 변경사항에 대해 오류가 발생하더라도 단시간에 찾아낼 수 있다.
테스트는 처음부터 끝까지 일련의 과정이 아닌 개별로 작성되기 때문에 각 테스트에 필요한 가짜 객체(mock)를 만들어 테스트하는 경우가 많다.

## Testing Pyramid

* Google Test Automation Conference에서 제안된 테스트 피라미드
* 시스템을 테스트 할때 크게 3가지 방법으로 나눌 수 있다
* 전체 테스트 비중을 아래와 같은 수치로 구현하는 것이 권장된다

* E2E Testing - 10%
* Integrating Testing - 20%
* Unit Testing - 70%

## End-To-End Testing / UI Testing

E2E Test는 종단(Endpoint) 간 테스트로 사용자의 입장에서 테스트 하는 것이다. 보통 Web, App 등에서 GUI를 통해서 시나리오, 기능 테스트 등을 수행합니다. 사용자에게 직접 노출되는 부분을 점검한다고 생각하면 된다.

E2E Test Framework : Cypress

## Integration Testing

최소 두 개이상의 클래스 또는 서브 시스템을 결합하여 테스트하는 방식이다.
예를 들면 Postman 또는 httpie를 통해 서버에 요청하여 JsonResponse가 의도대로 출력되는지 확인하는 방법이 있다.

## Unit Test

Unit Test의 특징에 대해서는 상단에 이미 언급하였고, 이외의 몇 가지 일반적인 원칙은 아래와 같다.

* 테스트 유닛은 각 기능의 가장 작은 단위에 집중하여, 해당 기능이 정확히 동작하는지를 증명해야 합니다.
* 각 테스트 유닛은 반드시 독립적이어야 합니다. 각 테스트는 혼자서도 실행 가능해야하고, 테스트 슈트로도 실행 가능해야 합니다. 이 때, 호출되는 순서와 무관하게 잘 동작해야 합니다. 이 규칙이 뜻하는 바, 새로운 데이터셋으로 각각의 테스트를 로딩해야 하고, 그 실행 결과는 꼭 삭제해야합니다. 보통 setUp() 과 tearDown() 메소드로 이런 작업을 합니다.
* 테스트가 빠르게 돌 수 있도록 만들기 위해 노력해야 합니다. 테스트 하나가 실행하는데 몇 밀리세컨드 이상의 시간이 걸린다면, 개발 속도가 느려지거나 테스트가 충분히 자주 수행되지 못할 것입니다. 테스트에 필요한 데이터 구조가 너무 복잡하고, 테스트를 하려면 매번 이 복잡한 데이터를 불러와야 해서 테스트를 빠르게 만들 수 없는 경우도 있습니다. 이럴 때는 무거운 테스트는 따로 분리하여 별도의 테스트 슈트를 만들어 두고 스케쥴 작업을 걸어두면 됩니다. 그리고 그 외의 다른 모든 테스트는 필요한 만큼 자주 수행하면 됩니다.
* 지금 사용하고 있는 툴이 개별 테스트나 테스트 케이스를 어떻게 수행하는지 배우셔야 합니다. 모듈 안에 들어있는 함수를 개발하고 있다면, 그 함수의 테스트를 자주, 가능하다면 코드를 저장할 때마다 자동으로 돌려야 합니다.
* 그날의 코딩을 시작하기 전에 항상 풀 테스트 슈트를 돌려야 합니다. 끝난 후에도 마찬가지입니다. 이 작업은 당신이 다른 코드를 망가뜨리지 않았다는 더 큰 자신감을 심어줄 것입니다.
* 모두가 공유하는 저장소에다가 코드를 집어넣기 전에 자동으로 모든 테스트를 수행하도록 하는 훅을 구현하는 하는 것이 좋습니다.
* 지금 한창 개발 중인데 그만두고 잠시 다른 일을 해야한다면, 다음에 개발할 부분에다가 일부러 고장난 유닛 테스트를 작성하는 것도 좋은 생각입니다.
* 코드를 디버깅할 때 가장 먼저 시작할 일은 버그를 찝어내는 새로운 테스트를 작성하는 것입니다. 이런 일이 언제나 가능한 것은 아니지만, 이런 버그 잡이 테스트들이야말로 당신의 프로젝트에서 가장 가치있는 코드 조각이 될 것입니다.
* 테스트 함수에는 길고 서술적인 이름을 사용하셔야 합니다. 테스트에서의 스타일 안내서는 짧은 이름을 보다 선호하는 다른 일반적인 코드와는 조금 다릅니다. 테스트 함수는 절대 직접 호출되지 않기 때문입니다. 실제로 돌아가는 코드에서는 square() 라든가 심지어 sqr() 조차도 괜찮습니다. 하지만 테스트 코드에서는 test_square_of_number_2(), test_square_negative_number() 같은 이름을 붙여야 합니다. 이런 함수명들은 테스트가 실패할 때나 보입니다. 그러니 반드시 가능한 한 서술적인 이름을 붙여야 합니다.
* 무언가 잘못되었거나 뜯어고쳐야만 할 경우, 괜찮은 코드에 테스트 셋이 있다면 당신이나 다른 유지보수 담당자들은 오류를 수정하거나 프로그램의 동작을 수정할 때 필시 그 테스트 슈트에 전적으로 의지할 것입니다.
* 테스트 코드의 또다른 사용 방법은 새로운 개발자들을 위한 안내서로 쓰는 방법입니다. 이미 만들어져 있는 코드에서 작업해야할 경우, 관련 테스트 코드를 돌려보고 읽어보는 것이야말로 가장 좋은 시작점일 경우가 많습니다. 이렇게 테스트 코드를 돌려보면 어느 지점이 문제인지, 수정하기 어려운 곳은 어디일지, 막다른 골목은 어디일지를 발견하게 됩니다. 몇 가지 기능을 추가해야 한다면 가장 먼저 해야할 일은, 그 새로운 기능이 아직 돌아가지 않음을 확인할 수 있는 테스트를 붙여넣는 것입니다.
