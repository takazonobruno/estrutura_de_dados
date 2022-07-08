from AVL_Tree import *

AVL_Tree = AVLTree()
root = None

nums = []

for n in range(0, 10):
    num = int(input("Type the number to add to the Tree: "))
    nums.append(num)

for i in nums:
    root = AVL_Tree.insert_node(root, i)

print("AVL:", end=" ")
AVL_Tree.preOrder(root)
print("\n")
val = int(input("Type the number that you wanted to remove of  the Tree: "))
root = AVL_Tree.delete_node(root, val)
print(" AVL After Deletion: ", end=" ")
AVL_Tree.preOrder(root)