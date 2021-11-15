def topologicalSort(jobs, deps):
    # to simplify things I assume deps defines the graph's eses and jobs defines the graph's node
    S = [] # set of nodes with no incoming edges
    L = [] # list of topologically sorted nodes

    for job in jobs:
        if HasNoIncomingEdge(job,deps):
            S.insert(0,job)
    while len(S) != 0:
        node = S.pop(0)
        L.append(node)
        i = 0
        while i != len(deps):
            from_node = deps[i][0]
            to_node = deps[i][1]
            if from_node == node:
                deps.remove([from_node, to_node])
                if HasNoIncomingEdge(to_node, deps):
                    S.insert(0, to_node)
                continue
            i += 1
    if len(deps) != 0:
        print([])
    else:
        print(L)

def HasNoIncomingEdge(job, deps):
    for dep in deps:
        if dep[1] == job:
            return False
    else:
        return True

if __name__ == '__main__':
    jobs = [1, 2, 3, 4, 5, 6, 7, 8]
    deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [1, 6], [1, 2], [7, 6]]
    topologicalSort(jobs,deps)
