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



        
        

        