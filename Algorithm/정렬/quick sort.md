퀵 정렬은 가장 빠른 정렬 알고리즘으로 알려져 있다.

`[5, 7, 1, 4, 6, 2, 3, 9, 8]`

위와 같은 배열이 있다고 할 때 퀵 정렬을 통해 오름차순으로 정렬해보도록 하자. 퀵 정렬에서는 기준이 되는 피벗이 있다. 피벗은 임의로 어떤 원소를 정하든 상관없지만 여기서는 정 가운데 원소로 정하도록 한다. 그러면 원소 6이 피벗이 된다. 그리고 left, right라는 두 개의 포인터를 둔다. 이 배열에서 left는 5, right는 8로 시작하여 피벗으로 올 때까지 범위를 좁혀올 것이다. left는 피벗인 6보다 큰 수가 나오면 멈추고, right는 피벗보다 작은 수 가 나오면 멈춘다. 그러면 피벗까지 정렬되는 과정은 다음과 같다.

`[5, 7, 1, 4, 6, 2, 3, 9, 8]`

-> `[5, 3, 1, 4, 6, 2, 7, 9, 8]`

-> `[5, 3, 1, 4, 2, 6, 7, 9, 8]` (여기서는 left가 피벗에 도달하고 right는 2에서 멈춘다. 그러면 두 수를 교환하며 정렬을 마친다)

정렬이 마치면 피벗을 기준으로 배열을 나누게 된다. 피벗은 자신의 자리를 찾아갔기 때문에 이제 정렬에서 제외된다.

`[5, 3, 1, 4, 2] [6] [7, 9, 8]`

이전의 피벗이 있던 배열을 제외하고 동일하게 피벗을 정하고 이를 기준으로 정렬을 수행한다. 그러면 다음과 같이 정렬이 된다.

`[1, 3, 5, 4, 2] [6] [7, 8, 9]`

피벗을 제외하고 또 배열을 나눈다. 그리고 계속해서 진행한다. 종료조건은 모든 배열이 하나의 원소로 쪼개어 질 때까지이다.

`[1] [3, 5, 4, 2] [6] [7, 8] [9]` 피벗 = 4, 8

-> `[1] [3, 2] [4] [5] [6] [7] [8] [9]` 피벗 = 5 (이 구간에서는 left와 right가 피벗에서 만나게 되는데 그러면 해당 정렬 종료)

-> `[1] [2] [3] [4] [5] [6] [7] [8] [9]` 정렬 종료

이후 모든 원소를 다시 하나로 합치면 퀵 정렬이 종료된다.
