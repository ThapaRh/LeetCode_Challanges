'''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
'''
#Monotonic Queue
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minMonQ = deque([0])
        maxMonQ = deque([0])
        length = 0
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        i = 1
        while(i<len(nums)):
            val = nums[i]
            while(minMonQ):
                if nums[minMonQ[-1]]>val:
                    minMonQ.pop()
                else:
                    break
            minMonQ.append(i)
            while(maxMonQ):
                if nums[maxMonQ[-1]]<val:
                    maxMonQ.pop()
                else:
                    break
            maxMonQ.append(i)

            print(minMonQ, maxMonQ)

            while(minMonQ and maxMonQ):
                minVal = nums[minMonQ[0]]
                maxVal = nums[maxMonQ[0]]
                diff = maxVal - minVal
                print("---",minMonQ,maxMonQ)
                print(minVal,maxVal)
                if diff <= limit:
                    minV = min(minMonQ[0],minMonQ[-1],maxMonQ[0],maxMonQ[-1])
                    maxV = max(minMonQ[0],minMonQ[-1],maxMonQ[0],maxMonQ[-1])
                    length = max(length,maxV-minV+1)
                    print(length)
                    break
                else:
                    if maxMonQ[0]<minMonQ[0]:
                        maxMonQ.popleft()
                    else:
                        minMonQ.popleft()
            i+=1
        return length
                