# """
# 여러 개의 수열을 정해진 규칙에 따라 합치려고 한다. 다음은 3개의 수열이 주어진 경우의 예이다.
# 수열 1: [2, 3, 4, 5]
# 수열 2: [4, 8, 7, 6]
# 수열 3: [9, 10, 15, 16]
# 수열 4: [1, 2, 6, 5]
#
# 수열 2의 첫 숫자 보다 큰 수자를 수열 1에서 찾아 그 앞에 수열 2를 끼워 넣는다.
# [2, 3, 4, 4, 8, 7, 6, 5]
#
# 합쳐진 수열에 대해, 수열 3의 첫 숫자보다 큰 숫자를 찾아 그 앞에 수열 3을 끼워 넣는다.
# 큰 숫자가 없는 경우 맨 뒤에 붙인다.
# [2, 3, 4, 4, 8, 7, 6, 5, 9, 10, 15, 16]
#
# 마지막 수열까지 합치고 나면, 맨 뒤의 숫자부터 역순으로 10개를 출력한다.
# [1, 2, 6, 5, 2, 3, 4, 4, 8, 7, 6, 5, 9, 10, 15, 16]
#
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 수열의 개수 M,
# 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열이 주어진다. 4<=N<=1000, 1<=M<=1000
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,
# 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력한다.
#
# [입력]
# 3
# 4 4
# 2 3 4 5
# 4 8 7 6
# 9 10 15 16
# 1 2 6 5
# 5 5
# 273 415 58 798 251
# 675 193 494 506 365
# 479 390 224 334 387
# 107 402 569 422 183
# 88 709 994 206 916
# 10 10
# 178 778 659 231 274 123 788 16 483 404
# 36 14 602 74 287 689 730 703 611 339
# 445 468 126 821 946 212 218 143 999 923
# 288 792 249 142 996 999 570 757 141 921
# 98 87 800 892 401 244 661 179 403 985
# 474 315 694 816 838 525 288 94 609 6
# 789 433 474 883 927 841 242 233 286 749
# 7 667 875 986 107 957 887 520 430 649
# 721 206 65 776 328 807 845 908 382 836
# 707 811 790 652 805 190 407 257 668 307
#
# [출력]
# #1 16 15 10 9 5 6 7 8 4 4
# #2 251 798 365 506 494 193 675 387 334 224
# #3 404 483 16 788 123 274 231 659 778 178
#
# """
import sys
sys.stdin = open('input_수열 합치기.txt', 'r', encoding='UTF-8')


class Node:
    def __init__(self, data, prv=None, nxt=None):
        self.data = data
        self.prv = prv
        self.nxt = nxt


# Doubly Linked List Class
class DLL(Node):
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def add_to_tail(self, data):
        new_data = Node(data)
        cur_node = self.head

        while cur_node.nxt is not None:
            cur_node = cur_node.nxt

        cur_node.nxt = new_data
        new_data.prv = cur_node
        self.tail = new_data

    def print(self):
        cur_node = self.head

        while cur_node is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.nxt
        print()

    def print_reverse_10(self):
        cur_node = self.tail

        for _ in range(10):
            print(cur_node.data, end=" ")
            cur_node = cur_node.prv
        print()

    def merge(self, arr):
        cur_node = self.head

        # arr의 앞 부분에 위치하는 경우
        if self.head.data > arr.head.data:
            arr.head.prv = self.head
            arr.tail.nxt = cur_node
            self.head = arr.head
            cur_node.prv = arr.tail
        else:
            while cur_node.nxt is not None:
                if cur_node.data <= arr.head.data < cur_node.nxt.data:
                    arr.head.prv = cur_node
                    arr.tail.nxt = cur_node.nxt
                    cur_node.nxt = arr.head
                    cur_node.nxt.prv = arr.tail
                    break
                else:
                    cur_node = cur_node.nxt

            if cur_node.nxt is None:
                arr.tail.nxt = None
                arr.tail.prv = cur_node
                self.tail = arr.tail
                cur_node.nxt = arr.head


T = int(input())

for test_case in range(1, T + 1):
    length, num = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(num)]
    node_list = [0] * num

    for i in range(num):
        node_list[i] = DLL(num_list[i][0])
        for j in range(1, length):
            node_list[i].add_to_tail(num_list[i][j])

        if i != 0:
            node_list[0].merge(node_list[i])

        print()
    print("#{}".format(test_case), end=" ")
    print("{}".format(node_list[0].print_reverse_10()))


# a = DLL(2)
# a.add_to_tail(3)
# a.add_to_tail(4)
# a.add_to_tail(5)
# a.add_to_tail(8)
#
# b = DLL(1)
# b.add_to_tail(2)
# b.add_to_tail(6)
# b.add_to_tail(5)
# b.add_to_tail(7)
#
# a.print()
# b.print()
#
# a.merge(b)
# a.print()
# a.print_reverse_10()







