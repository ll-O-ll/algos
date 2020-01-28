def topologicalSort(jobs, deps):
        # using DFS algo... already defined
    permanent = [0]*len(jobs)
    visited = [0]*len(jobs)
    answer = []
    boo = True
    for n in range(len(permanent)):
        if permanent[n] == 0:
            boo = visit(permanent, visited, n, jobs, deps, answer, boo)
    if boo == False:
        return []
    return answer
def visit(permanent, visited, node, jobs, deps, answer, boo):
    if permanent[node] == 1:
        return
    if visited[node] == 1:
        #stop
        return False
    visited[node] = 1 
    for edge in deps:
        if edge[0] == jobs[node]:
            m = jobs.index(edge[1])
            boo = visit(permanent, visited, m, jobs, deps, answer, boo)
            if boo == False:
                return boo
    visited[node] = 0
    permanent[node] = 1
    #prepend
    answer.insert(0,jobs[node])
    
if __name__ == '__main__':
    jobs = [1, 2, 3, 4, 5, 6, 7, 8]
    deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [1, 6], [1, 2], [7, 6]]
    print(topologicalSort(jobs,deps))