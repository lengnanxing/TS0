class Node(object):
    def __init__(self,data=-1,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Tree(object):
    def __init__(self):
        self.root=Node()
        self.Myqueue=[]
    def add_node(self,data):
        node_temp =Node(data)
        if self.root.data==-1:
            self.root=node_temp
            self.Myqueue.append(self.root)
        else:
            treeNode=self.Myqueue[0]
            if treeNode.left==None:
                treeNode.left=node_temp
                if node_temp.data!=999:
                    self.Myqueue.append(treeNode.left)
            else:
                treeNode.right=node_temp
                if node_temp.data!=999:
                    self.Myqueue.append(treeNode.right)
                self.Myqueue.pop(0)
    def front_digui(self,root):
        if root==None:
            return
        print(root.data)
        self.middle_digui(root.left)
        self.middle_digui(root.right)
    def middle_digui(self,root):
        if root==None:
            return
        self.middle_digui(root.left)
        print(root.data)
        self.middle_digui(root.right)
    def later_digui(self,root):
        if root==None:
            return
        self.middle_digui(root.left)
        self.middle_digui(root.right)
        print(root.data)
    def level_queue(self,root):
        if root==None:
            return
        MyQueue=[]
        node=root
        MyQueue.append(root)
        while MyQueue:
            node=MyQueue.pop(0)
            print(node.data)
            if node.left!=None:
                MyQueue.append(node.left)
            if node.right!=None:
                MyQueue.append(node.right)
tree=Tree()
tree_data_temp=[0,1,999,2,3,4]
for data in tree_data_temp:
    tree.add_node(data)
tree.level_queue(tree.root)
