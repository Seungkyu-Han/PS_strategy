N = int(input('단어의 수를 입력 : '))

words = []

for i in range(N):
    words.append(list(input().strip()))

print('보드를 입력')

board = []

for i in range(5):
    board.append(list(input().strip()))

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


def hasword(cur_x, cur_y, target_word, visited):  # 해당 위치에 찾는 단어가 있는지 확인하는 함수
    # 범위를 확인하지 않고 넘어오기 때문에 범위 확인을 가장 먼저 해준다.
    if not (0 <= cur_x < 5 and 0 <= cur_y < 5):
        return False

    if len(target_word) == 0:
        return True

    if target_word[0] != board[cur_x][cur_y]:
        return False

    for t in range(8):
        go_x = cur_x + dx[t]
        go_y = cur_y + dy[t]

        if not (0 <= go_x < 5 and 0 <= go_y < 5):
            continue

        if not visited[go_x][go_y]:
            continue

        visited[go_x][go_y] = False
        if hasword(go_x, go_y, target_word[1:], visited):
            return True
        visited[go_x][go_y] = True

    return False


def solve(target_word):
    for q in range(5):
        for w in range(5):
            visited_list = [[True] * 5 for i in range(5)]
            if hasword(q, w, target_word, visited_list):
                return True
    return False


for i in range(N):
    if solve(words[i]):
        print(*words[i])
