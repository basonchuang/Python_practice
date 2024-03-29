class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.left:
            # the left node of root has value, then assign the key to the right node
            root.right = insert(root.right, key)
        else:
            # the left node of root doesn't have value, assign the key to the left node
            root.left = insert(root.left, key)
        return root
def pre_order_traversal(root):
    if root is not None:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        

root = None
input = input("Input: ")

input_root = input.split('root = [')
input_root = str(input_root[1]).split(']')[0]

p = eval(input.split('p = ')[-1][0])
q = eval(input.split('q = ')[-1][0])

for i in input_root.split(','):

    if i != 'null':
        # is value
        root = insert(root, eval(i))
    else:
        # need to be turnd into None
        i = None
        root = insert(root, None)

s = Solution()
s.lowestCommonAncestor(root, p, q)
#pre_order_traversal(root)