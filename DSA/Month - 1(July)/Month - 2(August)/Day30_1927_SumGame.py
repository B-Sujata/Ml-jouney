# The below solution is not right or working one, but it is my first attempt so keeping it here for tracking how I started and I reach the solution

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


# Second atttempt
class Solution:
    def sumGame(self, num: str) -> bool:
        
        
        mid = len(num)//2
        first_half = num[:mid]
        second_half = num[mid:]
        first_half_sum = 0
        second_half_sum = 0
        first_counter = 0
        second_counter = 0

        for i in range(len(first_half)):
            if first_half[i]!='?':
                first_half_sum+=int(first_half[i])
            if second_half[i]!='?':
                second_half_sum+=int(second_half[i])
        
        for i in first_half:
            if i=='?':
                first_counter+=1
        
        for i in second_half:
            if i=='?':
                second_counter+=1
        
        difference = first_half_sum - second_half_sum
        extra_questions = abs(first_counter - second_counter)
        effect = extra_questions*9
        
        if first_counter==second_counter:
            if difference==0:
                return False
            return True
        return 2 * difference + (first_counter - second_counter) * 9 != 0
        
        
'''
Approach

The idea is to split the string into two equal halves and compare their digit sums while accounting for the ? characters.

Split the string into two halves.
first_half
second_half
Calculate the sum of fixed digits in each half.
Ignore ? because its value is not known yet.
Count the number of ? in each half:
first_counter
second_counter

Calculate the fixed sum difference:

difference = first_half_sum - second_half_sum
If both halves contain the same number of ?:
Alice and Bob can effectively cancel each other's choices.
Therefore, only the existing sum difference matters.
If the difference is 0, Bob can make the sums equal → return False.
Otherwise, Alice wins → return True.

If the number of ? is different:

The unequal number of question marks creates an unavoidable advantage for one side.
Each unmatched ? can contribute up to 9.
The game can be represented by:
2 * difference + (first_counter - second_counter) * 9
If this value is 0, Bob can force equal sums.
Otherwise, Alice can force unequal sums.

Hence:

return 2 * difference + (first_counter - second_counter) * 9 != 0
Algorithm
1. Find the midpoint of num.
2. Split num into first_half and second_half.
3. Initialize both digit sums to 0.
4. Traverse both halves:
      - If character is not '?', add it to the corresponding sum.
5. Count '?' in each half.
6. Calculate:
      difference = first_half_sum - second_half_sum

7. If number of '?' in both halves is equal:
      - If difference == 0 → return False
      - Otherwise → return True

8. Otherwise:
      - Calculate:
        2 × difference + 9 × (first_counter - second_counter)
      - If it is non-zero → return True
      - If it is zero → return False
Time Complexity

O(n)

You traverse the string a constant number of times:

Once for calculating sums
Once for counting ? in the first half
Once for counting ? in the second half

Therefore:

Time = O(n)

Space Complexity

O(n)

Because you create:

first_half = num[:mid]
second_half = num[mid:]

which together contain n characters.

So:

Space = O(n)

If you avoided creating the two substring copies and processed num directly, the auxiliary space could be O(1).

'''     


        
        

        
        
        
        
        
        


