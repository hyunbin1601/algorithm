import sys
input = sys.stdin.readline

# 이진트리를 입력받아 전위순회, 중위 순회, 후위 순회한 결과 출력 프로그램 작성

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)


n = int(input()) # 이진 트리의 노드의 개수

tree = {} # 이진 트리 생성

for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right] # 이진 트리 생성
    

def preorder(node):
    if node == '.':
        return
    
    print(node, end='') # 루트 출력
    preorder(tree[node][0]) # 왼쪽 자식들 재귀로 방문하며 출력
    preorder(tree[node][1]) # 오른쪽 자식들 재귀로 방문하며 출력
    
def inorder(node):
    if node == '.':
        return
    
    inorder(tree[node][0]) # 왼쪽 자식 출력
    print(node, end='') # 루트 출력
    inorder(tree[node][1]) # 오른쪽 자식 출력
    
def postorder(node):
    if node == '.':
        return
    
    postorder(tree[node][0]) # 왼쪽 자식 출력
    postorder(tree[node][1]) # 오른쪽 자식 출력
    print(node, end='') # 루트 출력
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
