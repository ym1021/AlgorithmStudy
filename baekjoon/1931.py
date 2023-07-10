import sys
input_ = sys.stdin.readline

n = int(input_())
time = [[0]*2 for _ in range(n)]
for i in range(n):
    s, e = map(int, input_().split())
    time[i][0] = s
    time[i][1] = e
time.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end_t = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_t:
        cnt += 1
        end_t = time[i][1]
print(cnt)