import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

def post_order(preorder, start, end):
    if start > end:
        return
    
    root = preorder[start]  # 전위 순회의 첫 값은 항상 루트 노드
    divide = start + 1
    
    # 왼쪽 서브트리와 오른쪽 서브트리를 나누는 지점 찾기
    while divide <= end and preorder[divide] < root:
        divide += 1

    # 왼쪽 서브트리 후위 순회
    post_order(preorder, start + 1, divide - 1)
    # 오른쪽 서브트리 후위 순회
    post_order(preorder, divide, end)
    # 루트 노드 출력
    print(root)

def main():
    preorder = list(map(int, input().strip().split()))
    post_order(preorder, 0, len(preorder) - 1)

if __name__ == "__main__":
    main()