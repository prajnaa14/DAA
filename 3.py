from itertools import permutations
graph=[
    [0,10,15,20],
    [5,0,9,10],
    [6,13,0,12],
    [8,8,9,0]
]
no_nodes=len(graph)
start_node=0
best_route=None
min_cost=float('inf')
for perm in permutations(range(1,no_nodes)):
    route=[start_node]+list(perm)+[start_node]
    cost=sum(graph[start][dest]for start,dest in zip(route,route[1:]))
    if cost<min_cost:
        best_route=route
        min_cost=cost
print("Optimal route: ",best_route)
print("total cost: ",min_cost)