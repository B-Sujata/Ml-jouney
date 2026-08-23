class Solution:
    def sumGame(self, num: str) -> bool:
        original_num = int(num)
        
        mid = len(num)//2
        first_half = num[:mid]
        second_half = num[mid:]
        first_half_sum = 0
        second_half_sum = 0

        if '?' not in num:
            while(first_half!=0):
                first_half_sum+=int(first_half)%10
                second_half_sum+=int(second_half)%10
                first_half = int(first_half)//10
                second_half = int(second_half)//10
            if first_half_sum==second_half_sum:
                return False
            else:
                return True
        else:
            for i in range(len(original_num)):
                if original_num[i]=='?':
                    original_num[i]=randint(0, 9)
                else:
                    continue

        while(first_half!=0):
            first_half_sum+=int(first_half)%10
            second_half_sum+=int(second_half)%10
            first_half = int(first_half)//10
            second_half = int(second_half)//10
        if first_half_sum==second_half_sum:
            return False
        else:
            return True

