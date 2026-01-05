class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        hold = 0
        output = ""
        left, right = 0, 0
        while left < len(num1) or right < len(num2):
            num_1 = int(num1[len(num1)-1-left]) if left < len(num1) else 0
            num_2 = int(num2[len(num2)-1-right]) if right < len(num2) else 0

            num = num_1 + num_2 + hold
            hold = 1 if num >= 10 else 0
            if hold > 0:
                num -= 10
            
            output += str(num)
            
            left += 1
            right += 1
        
        if hold > 0:
            output += str(hold)

        
        return output[::-1]