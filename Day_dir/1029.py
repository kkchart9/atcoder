import io
import sys

_INPUT = """\
.#.......
#.#......
.#.......
.........
....#.#.#
.........
....#.#.#
........#
.........
"""
sys.stdin = io.StringIO(_INPUT)

from itertools import combinations
import numpy as np

S = []
for i in range(9):
    s = list(input())
    S.append(s)

combination = list(combinations(range(81), 4))

for li in combination:
    a, b, c, d = li
    a_w = a % 9
    a_h = a // 9
    b_w = b % 9
    b_h = b // 9
    c_w = c % 9
    c_h = c // 9
    d_w = d % 9
    d_h = d // 9

    if (S[a_h][a_w] == '#' and S[b_h][b_w] == "#" and S[c_h][c_w] == "#" and S[d_h][d_w] == "#"):
        i = [a_w, a_h]
        j = [b_w, b_h]
        k = [c_w, c_h]
        l = [d_w, d_w]

        lis = [i, j, k, l]
        A = np.array(lis[0])
        B = np.array(lis[1])
        C = np.array(lis[2])
        D = np.array(lis[3])
        lis.sort()
        dis_a = np.linalg.norm(A - B)
        dis_b = np.linalg.norm(A - C)
        dis_c = np.linalg.norm(D - B)
        dis_d = np.linalg.norm(D - C)

        # dis_a = np.linalg.norm(B - A)
        # dis_b = np.linalg.norm(B - D)
        # dis_c = np.linalg.norm(D - C)
        # dis_d = np.linalg.norm(C - A)

        # if (dis_a == dis_b and dis_b == dis_c and dis_c == dis_d):
        #     print(dis_a,dis_b,dis_c,dis_d)
        print(a,b,c,d)



    #
    # print(a_w, a_h, d_h)
# print(combination[0])