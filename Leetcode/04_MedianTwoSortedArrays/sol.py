import random  
class Solution:
    def fastMedian(self, nums1: [int], nums2:[int]) -> float:
        nums = sorted(nums1+nums2)  ; 
        l = len(nums) ; 
        if l % 2 == 1:
            return float(nums[(l-1)//2]) ; 
        else:
            return (nums[l//2]+nums[l//2-1])/2 ; 

    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        m = len(nums1) ; 
        n = len(nums2) ; 
        if m+n < 10:
            return self.fastMedian(nums1, nums2) ; 
        
        if m > n:
            nums1, nums2 = nums2, nums1 ; 
            m,n = n,m ; 

        low,up = 0, m ; 
        while low <= up:
            i = (low+up)//2 ;
            j = (m+n+1)//2 - i ; 

            if j > 0 and i < m and nums2[j-1] > nums1[i]:
                # i is too small
                low = i+1 ;

            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                # i is too big
                up = i-1 ; 

            else:  # i is perfect
                if i == 0: 
                    max_of_left = nums2[j-1] ; 
                elif j == 0: 
                    max_of_left = nums1[i-1] ;
                else:
                    max_of_left = max(nums1[i-1],nums2[j-1]) ;

                if (m+n) % 2 == 1: return max_of_left ; 

                if i == m:
                    min_of_right = nums2[j] ; 
                elif j == n:
                    min_of_right = nums1[i] ; 
                else:
                    min_of_right = min(nums1[i], nums2[j]) ; 

                return (max_of_left+min_of_right)/2.0;


###### test ########
def genArray(size):
    result = [] ; 
    for i in range(size):
        result.append(random.randint(0, 20)) ; 
    return sorted(result) ; 

def test():
    total = 100 ; 
    count = 0 ; 
    s = Solution() ; 
    for i in range(total):
        len1 = random.randint(1, 10) ;
        len2 = random.randint(1, 10) ; 
        nums1 = genArray(len1) ; 
        nums2 = genArray(len2) ; 
        r1 = s.fastMedian(nums1, nums2) ; 
        r2 = s.findMedianSortedArrays(nums1, nums2) ; 
        if r2 is not None and abs(r1-r2) < 10**(-6):
            count += 1 ; 
        else:
            print(nums1) ; # debug 
            print(nums2) ; # debug
            print('r1={0},r2={1}'.format(r1, r2)) ; # debug

    print('{0}/{1} cases passed'.format(count, total)) ; 
    return ;

def main():
    test() ; 
    return ;

if __name__ == "__main__":
    main() ; 
