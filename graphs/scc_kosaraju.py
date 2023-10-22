from __future__ import annotations


def dfs(u):
    """
    Doctest:
    >>> global graph, visit, stack
    >>> graph = [[1], [2], [0], []]
    >>> visit = [False, False, False, False]
    >>> stack = []
    >>> dfs(0)
    >>> stack
    []
    """
    global graph, reversed_graph, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True

    for v in graph[u]:
        dfs(v)

    stack.append(u)


def dfs2(u):
    """

    Doctest:
    >>> global reversed_graph, visit, component
    >>> reversed_graph = [[], [0], [1], [2]]
    >>> visit = [False, False, False, False]
    >>> component = []
    >>> dfs2(2)
    """
    global graph, reversed_graph, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True
    component.append(u)
    for v in reversed_graph[u]:
        dfs2(v)


def kosaraju():
    """
    Doctest:
    >>> global n, m, graph, reversed_graph, stack, visit, scc, component
    >>> n, m = 4, 4
    >>> graph = [[1], [2], [0], []]
    >>> reversed_graph = [[2], [0], [1], []]
    >>> stack, visit, scc, component = [], [False]*n, [], []
    >>> result = kosaraju()
    >>> sorted(result, key=lambda x: x[0])
    [[0, 2, 1], [3]]
    """
    global graph, reversed_graph, scc, component, visit, stack
    for i in range(n):
        dfs(i)
    visit = [False] * n
    for i in stack[::-1]:
        if visit[i]:
            continue
        component = []
        dfs2(i)
        scc.append(component)
    return scc


if __name__ == "__main__":
    # n - no of nodes, m - no of edges
    n, m = list(map(int, input().strip().split()))

    graph: list[list[int]] = [[] for _ in range(n)]  # graph
    reversed_graph: list[list[int]] = [[] for i in range(n)]  # reversed graph
    # input graph data (edges)
    for _ in range(m):
        u, v = list(map(int, input().strip().split()))
        graph[u].append(v)
        reversed_graph[v].append(u)

    stack: list[int] = []
    visit: list[bool] = [False] * n
    scc: list[int] = []
    component: list[int] = []
    import doctest

    doctest.testmod()
    print(kosaraju())
