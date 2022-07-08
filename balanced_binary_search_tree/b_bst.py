#Convertendo um array ordenado para uma árvore binária balanceada
 

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None
 

def sorted_arr_balancedBST(sorted_arr):
     
    if not sorted_arr:
        return None
    
    arr_middle = int((len(sorted_arr)) / 2)
    root = TreeNode(sorted_arr[arr_middle])
    root.left = sorted_arr_balancedBST(sorted_arr[:arr_middle])
    root.right = sorted_arr_balancedBST(sorted_arr[arr_middle+1:])
    return root

def pre_order(TreeNode):
    if not TreeNode:
        return
     
    print (TreeNode.value, end=" ")
    pre_order(TreeNode.left)
    pre_order(TreeNode.right)
    
def in_order(TreeNode):
 
    if not TreeNode:
        return
 
    in_order(TreeNode.left)
    print (TreeNode.value, end=" ")
    in_order(TreeNode.right)
    
    
def pos_order(TreeNode):
    
    if not TreeNode:
        return
    
    pos_order(TreeNode.left)
    pos_order(TreeNode.right)
    print (TreeNode.value, end=" ")

