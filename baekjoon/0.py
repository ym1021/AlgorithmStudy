def insert(root, key):
    if root is None:
        return {"val": key, "left": None, "right": None}
    else:
        if root["val"] < key:
            root["right"] = insert(root["right"], key)
        else:
            root["left"] = insert(root["left"], key)
    return root

def search(root, key):
    if root is None or root["val"] == key:
        return root is not None
    if root["val"] < key:
        return search(root["right"], key)
    return search(root["left"], key)

def minValueNode(node):
    current = node
    while current["left"] is not None:
        current = current["left"]
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root["val"]:
        root["left"] = deleteNode(root["left"], key)
    elif key > root["val"]:
        root["right"] = deleteNode(root["right"], key)
    else:
        if root["left"] is None:
            return root["right"]
        elif root["right"] is None:
            return root["left"]
        temp = minValueNode(root["right"])
        root["val"] = temp["val"]
        root["right"] = deleteNode(root["right"], temp["val"])
    return root

def preorder(root):
    if root:
        print(root["val"], end=" ")
        preorder(root["left"])
        preorder(root["right"])

def inorder(root):
    if root:
        inorder(root["left"])
        print(root["val"], end=" ")
        inorder(root["right"])

def postorder(root):
    if root:
        postorder(root["left"])
        postorder(root["right"])
        print(root["val"], end=" ")

def binary_tree_operations(input_list, N, M, L):
    root = None
    for num in input_list:
        root = insert(root, num)

    print(search(root, N))
    preorder(root)
    print()
    root = insert(root, M)
    inorder(root)
    print()
    print(search(root, L))
    root = deleteNode(root, L)
    postorder(root)

# 입력 받기
arr = input().split(', ')
arr = [int(s.strip("[]")) for s in arr]
N = int(input())
M = int(input())
L = int(input())

# 함수 호출
binary_tree_operations(arr, N, M, L)
