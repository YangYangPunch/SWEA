import sys

sys.stdin = open("input_수열 편집.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    length, cnt, index = map(int, input().split())
    num_list = list(map(int, input().split()))
    order_list = []
    for i in range(cnt):
        order_list.append(input().split())
    print(length, cnt, index)
    print(num_list)
    print(order_list)
