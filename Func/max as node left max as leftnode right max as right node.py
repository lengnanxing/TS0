list0=[3,2,1,6,0,5]
#max_index=list0.index(max(list0))
#print(max_index)
def func1(list):#类似前序遍历
    if len(list)==0:
        return
    k=list.index(max(list))
    func1(list[0:k])
    print(list[k])
    func1(list[k+1:])
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def reConstructBinaryTree(self, pre, tin):
        # write code here
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        res = TreeNode(pre[0])
        res.left = self.reConstructBinaryTree(pre[1: tin.index(pre[0]) + 1], tin[: tin.index(pre[0])])
        res.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return res
#max_index=list0.index(max(list0))
def func2(list):
    max_index = list.index(max(list))
    res=TreeNode(max(list))

    if max_index!=0:
        res.left=func2(list[0:max_index])
    else:
        res.left=None
    print(res.val)
    if max_index!=len(list)-1:
        res.right=func2(list[max_index+1:])
    else:
        res.right=None
    return res

func2(list0)
