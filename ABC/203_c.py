import io
import sys

_INPUT = """\
3 2
5 5
2 1
2 2
"""
sys.stdin = io.StringIO(_INPUT)

n,k = map(int,input().split())

friends=[]
for i in range(n):
    a,b = map(int,input().split())
    friends.append([a,b])

friends.sort()

now_village=0

now_village+=k

for i in range(n):
    friend_village=friends[i][0]
    friend_money=friends[i][1]
    # print(friend_village,friend_money,now_village)

    if friend_village<=now_village:
        now_village+=friend_money
    else:
        break

print(now_village)