class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer= []
        for i in range(1,n+1):
            divby3 = (i%3 == 0)
            divby5 = (i%5 == 0)
            if divby3 and divby5:
                answer.append("FizzBuzz")
            elif divby3:
                answer.append("Fizz")
            elif  divby5:
                answer.append("Buzz")
            else:
                
                answer.append(str(i))


        return answer
