class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #constraint 1: any closed parenthese is preceded by a open parentheses
        #constraint 2: at any index, the #open >= #closed
        output = []
        def generate(cur_string, open_n, close_n):
            if open_n == 0 and close_n == 0:
                output.append(cur_string)
            elif open_n == close_n:
                generate(cur_string+'(', open_n-1, close_n)
            elif open_n < close_n:
                if open_n == 0:
                    output.append(cur_string+')'*close_n)
                else:
                    generate(cur_string+'(', open_n-1, close_n)
                    generate(cur_string+')', open_n, close_n-1)
        generate(cur_string = '', open_n = n, close_n = n)
        return output

