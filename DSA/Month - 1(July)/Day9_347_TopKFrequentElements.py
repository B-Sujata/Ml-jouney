class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return [nums[0]]
        lst = []
        
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
                
        for key,value in freq.items():
            max_val = max(freq.values())
            last.append(max_val) # Need to append key here
            del freq[max_val]  # Confused about how do I find the key of it now
            k-=1
            if k==0:
                return lst
            else:
                max_val = max(freq.values())
                lst.append(max_val) # Need to append key here
        
        return lst



# Finally

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        freq = {}

        if len(nums)==1:
            return [nums[0]]
        
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        
        lst = list(freq.items())

        

        while k>0:
            max_val = max(lst, key=lambda x: x[1])
            for i in lst:
                if i==max_val:
                    answer.append(i[0])
                    lst.remove(i)
                    k-=1
                

                if k==0:
                    return answer
                else:
                    max_val = max(lst, key=lambda x: x[1])

                                                            
        return answer


'''
Approach
Create a frequency dictionary to count how many times each element appears in the array.
Convert the dictionary into a list of (element, frequency) tuples so that both the element and its frequency remain together.
While k > 0:
Find the tuple having the maximum frequency using max() with a custom comparison based on the second element of each tuple.
Append the element (first value of the tuple) to the answer.
Remove that tuple from the list so it is not selected again.
Decrease k.
Return the answer list containing the top k frequent elements.
Algorithm
Initialize an empty dictionary freq.
Traverse the input array and store the frequency of each element in the dictionary.
Convert the dictionary into a list of tuples using list(freq.items()).
Initialize an empty answer list.
Repeat while k > 0:
Find the tuple with the highest frequency using max(lst, key=lambda x: x[1]).
Append the element (tuple[0]) to the answer.
Remove the selected tuple from the list.
Decrement k.
Return the answer list.
Time Complexity
Building the frequency dictionary: O(n)
Converting dictionary to list: O(m), where m is the number of distinct elements.
max(lst, key=...) scans the entire list each time: O(m)
Removing the tuple from the list: O(m)

Since these operations are performed k times:

Overall Time Complexity:

O(n+k×m)
	​


where:

n = size of the input array
m = number of distinct elements
Worst Case

If every element is unique, then m = n.

So the worst-case complexity becomes:

O(n+kn)
	​


If k = n, then:

O(n
2
)
	​

Space Complexity
Frequency dictionary: O(m)
List of tuples: O(m)
Answer list: O(k)

Overall:

O(m+k)
	​

Worst Case

If all elements are unique (m = n) and k = n:

O(n)
	​

Placement Interview Note

This solution is correct in terms of logic, but it is not the optimal solution for LeetCode 347 because repeatedly searching for the maximum and removing it leads to a quadratic worst-case time complexity. In interviews (including companies like Infosys), interviewers often appreciate arriving at a working solution first and then discussing how it could be optimized afterward.


'''

# But thi is not an optimal solution and while trying to find out the optimal solution I leanrt a really cool DSA Trick now let's try implementing it
        
        

        