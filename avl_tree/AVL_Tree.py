# Create a tree node
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None
        self.h = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, val):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.l = self.insert_node(root.l, val)
        else:
            root.r = self.insert_node(root.r, val)

        root.h = 1 + max(self.getHeight(root.l),
                              self.getHeight(root.r))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if val < root.l.val:
                return self.rightRotate(root)
            else:
                root.l = self.leftRotate(root.l)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if val > root.r.val:
                return self.leftRotate(root)
            else:
                root.r = self.rightRotate(root.r)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, val):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif val < root.val:
            root.l = self.delete_node(root.l, val)
        elif val > root.val:
            root.r = self.delete_node(root.r, val)
        else:
            if root.l is None:
                temp = root.r
                root = None
                return temp
            elif root.r is None:
                temp = root.l
                root = None
                return temp
            temp = self.getMinValueNode(root.r)
            root.val = temp.val
            root.r = self.delete_node(root.r,
                                          temp.val)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.h = 1 + max(self.getHeight(root.l),
                              self.getHeight(root.r))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.l) >= 0:
                return self.rightRotate(root)
            else:
                root.l = self.leftRotate(root.l)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.r) <= 0:
                return self.leftRotate(root)
            else:
                root.r = self.rightRotate(root.r)
                return self.leftRotate(root)
        return root

    # Function to perform l rotation
    def leftRotate(self, z):
        y = z.r
        T2 = y.l
        y.l = z
        z.r = T2
        z.h = 1 + max(self.getHeight(z.l),
                           self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                           self.getHeight(y.r))
        return y

    # Function to perform r rotation
    def rightRotate(self, z):
        y = z.l
        T3 = y.r
        y.r = z
        z.l = T3
        z.h = 1 + max(self.getHeight(z.l),
                           self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                           self.getHeight(y.r))
        return y

    # Get the h of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.h

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.l) - self.getHeight(root.r)

    def getMinValueNode(self, root):
        if root is None or root.l is None:
            return root
        return self.getMinValueNode(root.l)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end=" ")
        self.preOrder(root.l)
        self.preOrder(root.r)

