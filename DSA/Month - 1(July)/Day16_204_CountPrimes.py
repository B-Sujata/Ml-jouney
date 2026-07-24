# After spending hours on this problem I finally come up with a solution whose sample test cases are accepted but it can't be submitted on leetcode and I learned here where comes the Sieve of Eratosthenes algorithm. And Leetcode problem number 204 is to teach this Sieve of Eratosthenes algorithm so Yess Now I'll again start from the scratch and solve this problem by this approach and I'm determined to get it submitted on the leetcode today itself.Let's go we've got this one...

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        
        if n==0 or n==1:
            return 0
        if 2<n:
            count+=1
        
        for num in range(3, n, 2):
            divisor_found = False
            for i in range(3, int(math.sqrt(num))+1, 2):
                if num%i==0:
                    divisor_found = True
                    break
            if divisor_found==False:
                count+=1
        return count
        
        
        
