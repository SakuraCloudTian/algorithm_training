class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num_stack = []
        cur_str = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=='[':
                num_stack.append(num)
                stack.append(cur_str)
                cur_str=""
                num=0
            elif ch==']':
                repeat = num_stack.pop()
                prev_str = stack.pop()
                cur_str =prev_str+repeat*cur_str
            else:
                cur_str += ch
        return cur_str