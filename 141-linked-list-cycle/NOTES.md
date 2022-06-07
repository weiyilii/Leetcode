### Proof of time complexity O(N) for fast and slow solution
mathematical explain and time complexity:  
generally, walker enters the cycle at node N(0) at time point t(0), while at t(0) runner is at N(d - 1). There are M nodes in the cycle.  
At any time point t, t >= t(0), the walker arrives at N(t mod M), the runner arrives at N(2t + d mod M)         
if we can solve:  
t mod M = (2t + d) mod M,  
we can ensure the walker and the runner will meet at the solution time point        
we can change the equation to:  
t = pM + x           (1)     
2t + d = qM + x      (2)    
p, q are positive integers, x is non-negative integer        
(2) - (1):        
t = (p-q)M - d         
find the smallest t, we will get the solution. so t = M - d        
and time complexity is O(n)        
