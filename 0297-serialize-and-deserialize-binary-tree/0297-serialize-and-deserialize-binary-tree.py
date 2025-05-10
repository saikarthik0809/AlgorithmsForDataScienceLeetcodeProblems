# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string_res=""
        def dfs(root):
            nonlocal string_res
            if not root:
                return
            string_res+=str(root.val)
            if root.left:
                string_res+="L"
                dfs(root.left)
            if root.right:
                string_res+="R"
                dfs(root.right)
            string_res+="U"
            return
        dfs(root)
        # print(string_res)
        return string_res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def get_val_from_data(x):
            i=0
            res=""
            # print(x, "||")
            while i<len(x):
                if x[i] in ["L", "R", "U"]:
                    break
                res+=x[i]
                i+=1
            x=x[i:]
            # print(res, "  ", x)
            if res:
                return int(res), x
            return res,x

        if not data:
            return None
        head=TreeNode(None)
        curr=head
        
        def dfs(curr):
            nonlocal data
            val, data=get_val_from_data(data)
            # print(val," || ", data)
            curr.val=val
            if data[0]=="L":
                data=data[1:]
                curr.left=TreeNode(None)
                dfs(curr.left)
            if data[0]=="R":
                data=data[1:]
                curr.right=TreeNode(None)
                dfs(curr.right)
            if data[0]=="U":
                data=data[1:]
                return
            return
        dfs(curr)
        return head
            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))