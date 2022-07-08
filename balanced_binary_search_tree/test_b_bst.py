from b_bst import *



s_arr = [1, 4, 9, 16, 25, 36]
root = sorted_arr_balancedBST(s_arr)
print ('Preorder Balanced BST ')
pre_order(root)
print('\n')
print('-' * 50)
print ('Inorder Balanced BST ')
in_order(root)
print('\n')
print('-' * 50)
print ('Posorder Balanced BST ')
pos_order(root)


