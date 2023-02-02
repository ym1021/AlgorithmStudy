import sys
sys.stdin = open('../../files/input.txt', 'r')

from collections import deque

M, N, K = map(int, input().split())
data = [[1]*(N+2) for _ in range(M+2)]