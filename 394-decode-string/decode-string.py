class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        current_num=""
        for i in s:
            if '0'<=i<='9':
                current_num+=i
            elif i=='[':
                stack.append(int(current_num))
                current_num=""
                stack.append(i)
            elif i==']':
                temp=[]
                while(stack and stack[-1]!='['):
                    temp.append(stack.pop())
                temp.reverse()
                temp2="".join(temp)
                stack.pop()
                repeat_num=stack.pop()
                stack.append(repeat_num*temp2)
            else:
                stack.append(i)
        return "".join(stack)