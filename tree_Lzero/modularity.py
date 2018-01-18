
import scipy as sp
import numpy as np

def main():
### load data
### 多少branch (L-zero)
### load length_ratio
    length_ma=[]
    theta_ma=[]
    def length_ratio(length_ratio):
        
        length=((sum(leangth_ratio)/len(length_ratio))**2)
        length_ma.append(length)
     
####
##length-ratio : (aftering squaring the feature then add it ) 在算距離 
###
    def theta_ratio(theta_ratio):
        theta_r=np.array(theta_ratio)
        theta=(np.square(theta_r)/len(theta_ratio))
        theta_ma.append(theta)
     
    
####
##theta-ratio : (相加square ) 在算距離
####

if __name__ == "__main__":
  main()
