# Split-Array-Same-Average
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.) 
Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty. 
## Sample input: 
[1,2,3,4,5,6,7,8] 
## Sample output:
True 
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average 
of 4.5. 
## Note: 
The length of A will be in the range [1, 30]. 
A[i] will be in the range of [0, 10000].

## Solution: 
A solution to this problem exists if and only if:  
*sum\*i%n==0* where sum is the sum of elements in A, n-the numbers of A's elements and i and iterator over A array  
How is this possible?  
If we want to split the A array into two sub-arrays B and C we observe that *sum(Bi)/nB = sum(Ci)/nC* beacause the two sub-arrays have the same average.  
If we do some more calculation we reach to the formula:  
*sum(Bi)=nB\*sum/n*.  
How the algorithm works?  
First of all it checks if it it possible to split the array using the formula above.  
Then, generates all combinations up to n/2+1 elements (if we found one sub-array the other one consist of the remaining elements from A (we need to stop at n/2+1 because for sure one sub-array will not contain more than n/2+1 elements).  
We compute the sum for each combination and if it is equal to the average of initial sub-array A we return True.  

