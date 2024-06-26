import heapq
from collections import Counter
class node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=''
    def __lt__(self,other):
        return self.freq< other.freq
def printnode(node,val=''):
    if not node:
        return
    newval=val+str(node.huff)
    if not node.left and not node.right:
        print(f"{node.symbol}-->{newval}")
    printnode(node.left,newval)
    printnode(node.right,newval)
string=input("Enter the string: ").lower()
res=Counter(string)
nodes=[node(freq,char)for char,freq in res.items()]
heapq.heapify(nodes)
while len(nodes)>1:
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)
    left.huff='0'
    right.huff='1'
    new_node=node(left.freq+right.freq,left.symbol+right.symbol,left,right)
    heapq.heappush(nodes,new_node)
printnode(nodes[0])

