# Tree
from graphviz import Graph
from collections import deque


class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1  # chieu cao cua cay hien tai


class Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
            # self.root.balance+=1

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
        # 2. update heigth of node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # 3. kiem tra can bang cua node
        balance = self.get_balance(node)

        # neu bi mat can bang:

        # TH 1 - Left Left (xoay right)
        if balance > 1 and key < node.left.value:
            return self.rotate_right(node)

        # TH 2 - Right Right (xoay left)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # TH3 - Left Right (xoay left right)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # TH 4 - Right Left (xoay right left)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        # Return the new root
        return x

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

    # ham search
    def search(self, key):
        return self._search(self.root, key) is not None

    def _search(self, node, key):
        if node is None or node.value == key:
            return node

        if key < node.value:
            return self._search(node.left, key)

        return self._search(node.right, key)

    def delete(self, root, key):
        # 1. xoa node trong cay AVL
        if not root:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        # 2. cap nhat chieu cao cua node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # 3. Kiem tra tinh can bang cua cay
        balance = self.get_balance(root)

        # Neu bi mat can bang:

        # TH1 - Left Left (xoay phai)
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # TH 2 - Left Right (xoay trái phải)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # TH 3 - Right Right (xoay trai)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # TH 4 - Right Left (xoay phai trai)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

# ham duyet cay Bfs


def traversal_bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Inorder tree traversal (Left - Root - Right)


def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.value, end=" ")
    inorderTraversal(root.right)


# main
bst = Tree()
elements = [50, 30, 20, 40, 70, 60, 80, 25, 45, 90, 75]
for x in elements:
    bst.insert_node(x)
print('inoreder traversal BST tree:')
inorderTraversal(bst.root)
print('\nTraversal tree by BFS:')
result = traversal_bfs(bst.root)
print(result)
# search
x = 40
if bst.search(x) == True:
    print(f'Found {x} in BST tree ')
    bst.delete(bst.root, x)
    print(f'BST tree after delete {x} is:')
    print(traversal_bfs(bst.root))
else:
    print(f'Not found {x} in BST tree ')
