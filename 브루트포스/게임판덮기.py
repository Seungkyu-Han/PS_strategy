result = 0


def solve(board_list, h, w):
    global result
    result = 0

    # 놓을 수 있는 블록의 종류
    block = [[[0, 0], [1, 0], [0, 1]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 1]], [[0, 0], [1, 0], [1, -1]]]

    def cover():
        global result

        x, y = find(h, w)
        if x == -1 and y == -1:
            result += 1
            return

        for q in range(4):
            if is_blank(x, y, q):
                cover_block(x, y, q, '#')
                cover()
                cover_block(x, y, q, '.')

    def find(h_len, w_len):
        for q in range(h_len):
            for r in range(w_len):
                if board_list[q][r] == '.':
                    return [q, r]
        return [-1, -1]  # 모든 칸이 덮여있으면

    def is_blank(x, y, block_type):
        for q in range(3):
            if 0 <= x + block[block_type][q][0] < h and 0 <= y + block[block_type][q][1] < w:
                if board_list[x + block[block_type][q][0]][y + block[block_type][q][1]] == '#':
                    return False
        return True

    def cover_block(x, y, block_type, blank_or_block):
        for q in range(3):
            board_list[x + block[block_type][q][0]][y + block[block_type][q][1]] = blank_or_block

    cover()
    print(result)


for _ in range(int(input())):
    H, W = map(int, input().split())

    board = []
    blank_cnt = 0

    for i in range(H):
        board.append(list(input().strip()))
        blank_cnt += board[-1].count('.')

    # 빈칸의 수가 3의 배수가 아니면 어차피 덮지 못하니 continue
    if blank_cnt % 3 != 0:
        print(0)
        continue

    solve(board, H, W)
