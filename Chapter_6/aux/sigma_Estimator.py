import numpy as np
from math import sqrt, log
from scipy.linalg import qr, norm, det

def sigma_estimate(N, n, dim, eta):
    """
    Runs N computation of secret key and returns the median value of the GS norm of (rot(s1) rot(s2)).
    """
    res_lambda_n = []
    
    for loop in range(N):
        #if(loop%100==0):
        #    print(loop)
        #the first coordinate of s1 is 1.
        s1 = np.random.randint(-eta,eta+1,size=n*(dim-1))
        xn2s1 = [(-1)**((i%n-n//2)//n)*s1[(i//n)*n+((i-n//2)%n)] for i in range(len(s1))]
        s = [s1[i]+xn2s1[i] for i in range(len(s1))]
        res_lambda_n.append(sqrt(norm(s)**2+2))
    return((sqrt(2*log(n-1+n*2**65)/np.pi)*np.nanquantile(res_lambda_n, 0.5)))

N = 1000
res1 = sigma_estimate(N,256,6,1)
print(res1)
#res2 = sigma_estimate(N,256,7,1)
#print(res2)
#print(sigma_estimate(N,256,8,2))
#res2 = sigma_estimate(N,256,9,1)
#print(res2)
#res3 = sigma_estimate(N,256,11,1)
#print(res3)
