# -*- coding: utf-8 -*-
"""
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
n = 5, m=3, v = [1, 2, 3, 4, 5]

이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

[입력]
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

[출력]
#1 21
#2 11088
#3 1090
"""

import sys

T = int(input())

for test_case in range(1, T + 1):
    length, filter_length = map(int, input().split())
    vlist = list(map(int, input().split()))
    print("{0} {1} {2}".format(sys.getsizeof(length), sys.getsizeof(filter_length), sys.getsizeof(vlist)))
    
    length, filter_length = map(int, input().split(' '))
    vlist = list(map(int, input().split(' ')))
    print("{0} {1} {2}".format(sys.getsizeof(length), sys.getsizeof(filter_length), sys.getsizeof(vlist)))
    
    # idx = 0
    # max_val = 0
    # min_val = 1e10
    
    # while idx + filter_length <= length:
    #     if max_val <= sum(vlist[idx : idx + filter_length]):
    #         max_val = sum(vlist[idx : idx + filter_length])
    #     if min_val >= sum(vlist[idx : idx + filter_length]):
    #         min_val = sum(vlist[idx : idx + filter_length])
    #     idx += 1
    
    # print("#{0} {1}".format(test_case, max_val - min_val))