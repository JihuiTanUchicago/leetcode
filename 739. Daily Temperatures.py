class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = [[temperatures[0],0]]
        answers = [0] * len(temperatures)
        if len(temperatures) <= 1:
            return answers
        for i in range(1, len(temperatures)):
            if temperatures[i] <= monotonic_stack[-1][0]:
                monotonic_stack.append([temperatures[i], i])
            else:
                while monotonic_stack != [] and temperatures[i] > monotonic_stack[-1][0]:
                    day = monotonic_stack.pop()[1]
                    answers[day] = i - day
                monotonic_stack.append([temperatures[i],i])
        return answers



            