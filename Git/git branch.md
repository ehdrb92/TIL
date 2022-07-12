# Git Branch

Git은 개발자가 어떤 업무를 하는가에 따라 branch를 나누어 작업을 한다고 한다.
개발자들 사이에 통용적으로 운용되는 브랜치에는 어떤 것이 있는지 알아보고자 한다.

![Getting Started](./image/total-branch.png)

## main branch

`main branch`는 일반적으로 **배포가 가능한 상태를 관리** 하기위한 코드가 있는 브랜치이다.
커밋을 할 때는 브랜치에 태그를 사용하여 배포 번호를 기록한다.

## developer branch

![Getting Started](./image/develop-branch.png)

`developer branch`는 main과 비슷한 역할을 하는데, 배포 목적이 아닌 **개발중인 기능들을 통합**하는 역할을 한다.

보통 GitHub에서 default 브랜치를 developer로 사용한다. 왜냐하면 평소에는 developer 브랜치를 기반으로 개발을 진행하기 때문에
`$ git push origin some-feature`(내 로컬 저장소의 some-feature branch를 중앙 원격 저장소로 올리는 명령)를 한 후, Github 페이지에서 해당 some-feature branch에 대해 병합을 할 때 중앙 원격 저장소의 ‘main’이 아닌 default로 설정되어 있는 ‘develop’에 병합하도록 설정하는 것이다.

## feature branch

![Getting Started](./image/feature-branch.png)

`feature branch`는 개발을 하는 단계에서 developer에서 분기하여 필요한 기능만을 위한 코드를 짜기 위한 것이다.
보통 브랜치의 이름을 `feature/[기능명]`과 같이 작성한다.
예를 들어 회원가입을 하기 위한 기능을 개발하는 브랜치라 하면 `feature/signup`과 같이 명명한다.

## release branch

`releases branch`는 기능의 개발이 모두 통합되어 완료된 developer에서 분기하여 **최종적으로 점검**을 한다.
특정 버전의 출시가 정해지면 해당 브랜치에서 기능이 정상적으로 작동하는지 점검한 후 main에 병합을 한다.
기능을 추가하는 작업은 하지 않는다. 출력되는 결과 값은 같은 상태에서 버그 및 로직의 수정만을 하게 된다.\

release의 이름은 보통 `release-[버전]`으로 명명한다.
그리고 main에 병합하게 되면 해당 브랜치에도 버전에 대한 태그를 달아준다.

## hotfix branch

![Getting Started](./image/hotfix-branch.png)

`hotfix branch`는 배포중인 프로그램에 발생한 버그를 **긴급하게 수정**해야 할 때 운용되는 브랜치이다.
main으로부터 분기하여 해당 버그를 수정한 후 다시 병합한다. 이때 developer에도 함께 병합해야한다.

hotfix를 main에 병합하게 되면 분기해온 main의 버전이 1.0 버전이였다면, hotfix를 병합해준 이후 1.0.1과 같이 버전의 태그를 달아준다.
