class Solution(object):
    def maximumSum(self, a):
        """
        :type arr: List[int]
        :rtype: int
        """
        #given a list L, a suffix S is a subarray which necessarily includes the tail of L e.g.
        # _ _ X _ | _ _  <-- is the suffix S
                    # ^
            #         |
            #         S  <-- here is the "tail" of L which makes S a suffix of L
        #in case the a is empty or has only one element 
        #THIS IS A DP PROBLEM>>>READ THE CLRS TEXTBOOK FOR MORE INFO G

        answer = a[0]
        suf_no_del = a[0] #here we keep the [last] element
        suf_del = 0 # here we delete the [last] element 
        for i in range(1,len(a)):
            #increment i increases the suffix by one
            #only delete the suffix when it doesn't maximise the sum 
            suf_del = max(a[i]+suf_del, suf_no_del)
            #do not delete if the element (+previous sum) maximise the current sum
            suf_no_del = max(suf_no_del + a[i],a[i])
            answer = max(answer,suf_no_del, suf_del)
        return answer


if __name__ == "__main__":
    
    #input params

    input = [0,-5,2,3,5,0]

    s = Solution()
    print(s.maximumSum(input))