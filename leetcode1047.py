class Solution:
    def removeDuplicates(self, S: str) -> str:
        li = []
        for i in S:
            if len(li) == 0:
                li += i
            else:
                if li[len(li)-1] == i:
                    li.pop()
                else:
                    li += i
        return "".join(li)
