'''
슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

제한사항

스테이지의 개수 N은 1 이상 500 이하의 자연수이다.

stages의 길이는 1 이상 200,000 이하이다.

stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
    각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
    단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.

만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.

스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
'''

# 내가 생각한 풀이

def solution(N, stages):
    bundle = []
    answer = [] # 답안 제출 결과
    
    for i in range(1, N + 1): # 1 스테이지 부터 차례대로 실패율을 계산할 루프
        challenger = 0 # 스테이지에 도전한 사람
        
        for j in range(N): # 해당 스테이지의 도전자 수를 계산할 루프
            if i <= stages[j]: # <= 기호는 스테이지에 있거나 이미 통과한 사람일 경우 도전자 수를 추가하는 방식
                challenger += 1
        
        fail = stages.count(i) / challenger # 실패율 계산
        
        bundle.append((fail, i)) # (실패율, 스테이지)로 bundle 리스트에 저장
    bundle.sort(reverse=True) # 내림차순으로 정렬
    
    for i in bundle: # 제출할 배열에 스테이지만 추가
        answer.append(i[1])
    
    return answer

'''
위의 코드에서는 실패율이 같은 스테이지의 오름차순 정렬을 구현하지 못했다.
그리고 전체적으로 루프문이 너무 많아 리소스 낭비가 심한 코드이다.
'''

# 다른 풀이 1

def solution(N, stages):
    result = {} # 결과 딕셔너리
    denominator = len(stages) # 게임 유저의 수??
    for stage in range(1, N+1): # 1스테이지부터 차례대로 꺼내는 루프
        if denominator != 0: # 스테이지에 도달한 사람이 있는지 확인
            count = stages.count(stage) # 카운트 함수로 클리어하지 못한 사람의 수를 구해주었다.
            result[stage] = count / denominator # 실패율을 계산하여 딕셔너리에 "키:값"으로 저장한다.
            denominator -= count # 다음 실패율 계산에서 사용될 스테이지 도달자를 구해준다.
        else: # 없으면 그냥 0
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True) # 딕셔너리의 값을 기반으로 내림차순 정렬한다.

'''
전체 게임 참가자 수에서 스테이지별 도전자를 차감하며 다음 스테이지 도전자 수를 계산하는 방식은 획기적이였다.
그런데 마지막 람다를 이용하여 내림차순 정렬하였는데, 여기서 같은 실패율을 가진 스테이지가 어떻게 오름차순 정렬되었는지는 모르겠다.
'''

# 다른 풀이 2

def solution(N, stages):
    answer = [] # 정답 제출
    fail = [] # (스테이지, 실패율)로 저장하기 위한 리스트
    info = [0] * (N + 2) # 각 스테이지 도달자를 기록하기위한 배열로 보인다.
    for stage in stages: # 스테이지 도전자를 하나씩 꺼낸다.
        info[stage] += 1 # 몇 스테이지에 몇명인지 카운트한다.
    for i in range(N):
        be = sum(info[(i + 1):]) # 스테이지 총 도전자 수
        yet = info[i + 1] # 스테이지에 도전 중인 유저의 수
        if be == 0: # 도전자가 없었다면
            fail.append((str(i + 1), 0)) # 실패율을 0으로 저장
        else: # 아니면
            fail.append((str(i + 1), yet / be)) # 실패율을 계산해서 저장
    for item in sorted(fail, key=lambda x: x[1], reverse=True): # 실패율을 기준으로 내림차순 정리
        answer.append(int(item[0])) # 스테이지를 결과 리스트에 순서대로 저장
    return answer

'''
'다른 풀이1'과 사실상 유사하다.
'''

# 다른 풀이 3

def solution(N, stages):
    fail = {}
    for i in range(1,N+1): # 1스테이지 부터 차례대로~
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer

'''
짧고 간결한 코드이다. 하지만 이해를 못함... 그리고 속도가 느렸다.
'''