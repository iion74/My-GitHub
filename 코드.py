class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_Balanced(root,isBalanced=True):

    if root is None or not isBalanced:
        return 0, isBalanced

    left_height, isBalanced = is_Balanced(root.left, isBalanced)

    right_height, isBalanced = is_Balanced(root.right, isBalanced)

    if abs(left_height - right_height) >1 :
        isBalanced = False

    return max(left_height, right_height) + 1, isBalanced


if __name__ == '__main__':

    ''' Construct the following tree
                  A
                /   \
              B       C
             / \       \
            D   E       F
    '''

    d = TNode('D',None,None)
    f = TNode('F',None,None)
    e = TNode('E', None, f)
    c = TNode('C',None,None)
    b = TNode('B', c, d)
    root = TNode('A',b,e)


    if is_Balanced(root):
        print('Binary tree is balanced')
    else:
        print('Binary tree is not balanced')
