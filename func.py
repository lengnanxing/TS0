def binary_search(list,n):#s.t:list升序；function:二分查找
    result=-1
    index_left=0
    index_right=len(list)-1
    while result==-1 and index_left+1!=index_right:
        if list[(index_left+index_right)//2]==n:
            result=(index_left+index_right)//2
        else:
            if list[(index_left+index_right)//2]<n:
                index_left=(index_left+index_right)//2
            else:
                index_right=(index_left+index_right)//2
    if result==-1:
        if list[index_left]==n:
            result=index_left
        if list[index_right]==n:
            result=index_right
    return result
def bubble_sort(list):#function:冒泡排序
    for i in range(len(list)-1,-1,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
def func1(list):#s.t:list为有升序的；function：去除重复元素
    k=-1
    for i in range(len(list)):
        if list[i]!=k:
            k=list[i]
        else:
            list[i]=-999
    while -999 in list:
        list.remove(-999)
    return list
