import heapq

def algorithm(graph, start, goal, heuristic):
    open_set = []  # 검사받지 못한 노드
    came_from = {}  # 검사를 통해 찾은 최단거리 노드, 딕셔너리로 두 노드의 관계를 표현

    # 시작부터 목표까지의 실제 거리
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # 실제 거리 + 휴리스틱
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    # 시작 노드에 대한 정보 저장
    open_set.append((f_score[start], start))

    # 모든 노드를 검사할 때까지 반복
    while open_set:
        # 검사 받지 못한 노드 중 가장 f_score가 가장 낮은 노드를 추출
        # 추출하면 저장된 데이터는 삭제, 힙은 정렬시 f_score가 가장 낮은 순부터 이진 트리 방식으로 정렬
        _, current_node = heapq.heappop(open_set)

        # 현재 노드가 목표 노드이면 여태 지나온 최단거리 노드를 출력
        if current_node == goal:
            path = reconstruct_path(came_from, current_node)
            return path

        # 현재 노드에 이웃하는 노드를 가져와 비교
        for neighbor, cost in graph[current_node].items():
            # 잠정적인 최단 거리 = 현재 노드까지의 최단 거리 + 이웃하는 노드 사이의 실제 거리
            tentative_g_score = g_score[current_node] + cost

            # 잠정적인 최단 거리가 이웃하는 노드까지의 최단거리보다 작으면 해당 노드로 가는 길을 저장하고 힙에 추가
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node # 최단거리 노드로 저장
                g_score[neighbor] = tentative_g_score # 잠정적인 최단거리를 해당 노드까지의 최단거리로 저장
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor] # 우선순위 값도 갱신
                heapq.heappush(open_set, (f_score[neighbor], neighbor)) # 힙에 추가함으로써 해당 노드에 이웃하는 또다른 노드로부터 최단거리 검색

    return None  # 경로가 없을 경우

# 저장했던 최단거리 노드를 순서대로 정렬
def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    return path[::-1]

# 주어진 그래프와 휴리스틱 값
graph = {
    'A' : {'B' : 6, 'F' : 3},
    'B' : {'A' : 6, 'C' : 3, 'D': 2},
    'C' : {'B' : 3, 'D' : 1, 'E' : 5},
    'D' : {'B' : 2, 'C' : 1, 'E' : 8},
    'E' : {'C' : 5, 'D' : 8, 'I' : 5, 'J' : 5},
    'F' : {'A' : 3, 'G' : 1, 'H' : 7},
    'G' : {'F' : 1, 'I' : 3},
    'H' : {'F' : 7, 'I' : 2},
    'I' : {'E' : 5, 'G' : 3, 'H' : 2, 'J' : 3},
    'J' : {'E' : 5, 'I' : 3}
}

heuristic = {
    'A' : 10,
    'B' : 8,
    'C' : 5,
    'D' : 7,
    'E' : 3,
    'F' : 6,
    'G' : 5,
    'H' : 3,
    'I' : 2,
    'J' : 0
}

# 시작 노드와 목표 노드
start_node = 'A'
goal_node = 'J'

# 알고리즘 실행
path = algorithm(graph, start_node, goal_node, heuristic)
if path:
    print("최단 경로:", path)
else:
    print("경로가 없습니다.")
