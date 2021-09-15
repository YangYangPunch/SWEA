# -*- coding: utf-8 -*-
"""
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
 
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력]
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

[출력]
#1 1
#2 1
#3 1

"""

T = int(input())


def dfs(graph, start_node, end_node):
    visited = []
    need_visit = graph[start_node]
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node in graph.keys():
                need_visit.extend(graph[node])
    
    if end_node in visited:
        return 1
    else:
        return 0


for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = {}
    update_node = []
    
    for _ in range(e):
        key, value = map(int, input().split())
        
        if key not in graph.keys():
            graph.update({key: [value]})
        else:
            update_node = graph[key]
            update_node.append(value)
            graph.update({key: update_node})
        
    s, g = map(int, input().split())
    
    print("#{0} {1}".format(test_case, dfs(graph, s, g)))



















