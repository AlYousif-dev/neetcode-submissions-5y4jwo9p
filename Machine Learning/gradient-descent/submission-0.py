class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:   
        for i in range(iterations):
            init -= learning_rate * (init * 2)
            print(init)
        return round(init,5)