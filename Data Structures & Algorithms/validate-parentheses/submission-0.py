class Solution:
    def isValid(self, s: str) -> bool:
        B=[]
        A={ ")" : "(", "]" : "[", "}" : "{" }
        for i in s :
            if i in A:
                if B and B[-1]==A[i]:
                    B.pop()
                else:
                    return False 
            else:
                B.append(i)
        return True if not B else False

        