class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, nums, k):
        cnt = 0
        xorr = 0
        HashMap ={}

        for i in range(len(nums)):
            xorr = xorr ^ nums[i]
            if xorr ^ k in HashMap:
                cnt += HashMap[xorr^k]
            if xorr == k:
                cnt += 1
            if xorr in HashMap:
                HashMap[xorr] += 1
            else:
                HashMap[xorr] = 1
        return cnt
