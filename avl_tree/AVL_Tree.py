# cria um node para arvore
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None
        self.h = 1


class AVLTree(object):

    # função para inserir um node
    def insert_node(self, root, val):

        # busca o local correto para se inserir o node
        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.l = self.insert_node(root.l, val)
        else:
            root.r = self.insert_node(root.r, val)

        root.h = 1 + max(self.getHeight(root.l),
                              self.getHeight(root.r))

        # atualiza o fator de balanceamento e balanceia a arvore
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

    # função pra deletar o node
    def delete_node(self, root, val):

        # procura o node a ser deletado e remove ele
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

        # atualiza o fator de  balanceamento do node
        root.h = 1 + max(self.getHeight(root.l),
                              self.getHeight(root.r))

        balanceFactor = self.getBalance(root)

        # função balanceia a arvore
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

    # função de rotação para esquerda
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

    # Obter altura do node
    def getHeight(self, root):
        if not root:
            return 0
        return root.h

    # Obter o fator de balanceamento do node
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
