# m개 중에서 n개를 고르는 모든 조합을 찾는 알고리즘, 완전탐색

import sys

print('n과 m을 입력 : ', end='')
n, m = map(int, sys.stdin.readline().split())


def pick(cur, cur_list):
    if cur == n:
        print(*cur_list[1:])
        return

    for i in range(cur_list[-1] + 1, m + 1):
        cur_list.append(i)
        pick(cur + 1, cur_list)
        cur_list.pop(-1)


pick(0, [0])
