def insert(self, val):
        cur = self.root
        if not cur: 
            self.root = Node(val)
            return self.root
        
        while cur:
            if cur.info > val: 
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    break
            else: 
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    break
        
        return self.root


/////////////////////////////////////////

