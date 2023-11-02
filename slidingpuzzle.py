from queue import PriorityQueue

# 3x3 슬라이딩 퍼즐 초기 상태
puzzle = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

# 3x3 슬라이딩 퍼즐 목표 상태
result = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# 초기 상태 퍼즐과 목표 상태 퍼즐을 비교하여 비교값 구하기
def right_position(puzzle, result):
    point = 0

    # 모든 위치를 확인하며 두 퍼즐의 숫자가 다르면 + 1
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != result[i][j]:
                point += 1

    # 목표 위치에 없는 값의 수를 다 구하여 반환
    return point

# 이동할 수 있는 타일을 이동시켜 모든 경우의 수의 퍼즐 구하기
def get_neighbors(puzzle):
    # 경우의 수 퍼즐을 담을 변수
    neighbors = []

    # 모든 타일을 확인하여 이동할 수 있는 빈 공간(0)을 찾아 좌표값 저장
    empty_row, empty_col = -1, -1
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                empty_row, empty_col = i, j

    # 타일이 이동할 수 있는 네(동서남북) 방향 저장
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 이동이 가능한 타일 구하기
    for dr, dc in moves:
        # 빈 공간의 좌표값에 이동할 좌표 값을 더하여 새로운 좌표 값으로 저장
        new_row, new_col = empty_row + dr, empty_col + dc

        # 새로운 좌표값이 3x3 규격에 맞게 범위 내에서 움직일 수 있을 경우에 위치를 바꿔 바뀐 위치의 퍼즐을 neighbor에 저장
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[empty_row][empty_col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[empty_row][empty_col]
            neighbors.append(new_puzzle)

    # 바꿀 수 있는 모든 경우의 수 퍼즐을 담아 반환
    return neighbors

# 퍼즐을 풀기 위한 최소 이동 횟수를 구하는 알고리즘
def solve_puzzle(puzzle, result):
    # 초기 상태의 퍼즐의 (우선순위(이동 횟수 + 목표 퍼즐 비교값), 이동 횟수, 퍼즐)을 저장
    start_node = (right_position(puzzle, result), 0, puzzle)
    # 우선 순위를 통해 값들을 정렬하기 위해 우선순위 큐 사용
    pq = PriorityQueue()
    # 초기 상태 퍼즐에 대한 값 저장
    pq.put(start_node)
    # 방문했던 퍼즐을 거를기 위해 사용
    visited = set()

    # 우선 순위 큐에 저장된 값이 없을 때까지 반복
    while not pq.empty():
        # 우선 순위가 가장 높은(우선 순위 값이 가장 작은)값을 가져와 이동 횟수와 퍼즐 저장, 꺼내진 큐는 삭제
        _, cost, current_puzzle = pq.get()

        # 만약 꺼낸 퍼즐이 목표 상태 퍼즐과 같다면 해당 이동 횟수를 반환
        if current_puzzle == result:
            return cost
        
        # 방문했던 퍼즐이 아니면 해당 퍼즐을 visited에 저장
        if tuple(map(tuple, current_puzzle)) not in visited:
            visited.add(tuple(map(tuple, current_puzzle)))

            # 현재 퍼즐을 가지고 이동 가능한 모든 경우의 수의 퍼즐을 구해 각각 우선순위 큐에 저장
            # 저장할 때 우선순위를 새로 구하고 이동 횟수 + 1
            for neighbor in get_neighbors(current_puzzle):
                pq.put((cost + right_position(neighbor, result), cost + 1, neighbor))

# 알고리즘 함수를 호출하여 최소 이동 횟수 값을 저장 및 출력
moves = solve_puzzle(puzzle, result)
print(f"퍼즐을 해결하기 위한 최소 이동 횟수: {moves}")