1 : N 관계에서 N측에 명시한다.

* ForeignKey(to, on_delete)

to : 대상모델
    클래스를 직접 지정하거나,
    클래스명을 문자열로 지정. 자기 참조는 "self" 지정

on_delete : Record 삭제 시 Rule
    CASCADE : FK로 참조하는 다른 모델의 Record도 삭제
    PROTECT : ProtectedError를 발생시키며, 삭제 방지
    SET_NULL : null로 대체. 필드에 null=True 옵션 필수
    SET_DEFAULT : 디폴트 값으로 대체. 필드에 디폴트 값 설정 필수
    SET : 대체할 값이나 함수 지정. 함수의 경우 호출하여 리턴값을 사용
    DO_NOTHING : 어떠한 행동도 하지 않는다. DB에 따라 오류가 발생할 수 있음