class Solution:
    def isValid(self, s: str) -> bool:
        openset = {'(', '{', '['}
        dictset = {'(': ')', '{':'}', '[':']'}

        listy = []

        for i in s:
            if i in openset:
                listy.append(i)
                continue
            if not listy:
                return False
            if i != dictset[listy.pop()]:
                return False


            
        if listy:
            return False
        
        return True

