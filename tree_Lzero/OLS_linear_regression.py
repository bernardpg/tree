import numpy as np
from scipy import linalg
import os as os
def main(F1,F2,Label):
    #####
    ###feature_map
    A = np.c_[F1[:, np.newaxis],F2[:, np.newaxis]]
    ###feature_mean
    #feature_mean = np.mean(A, 0)
    #label_mean
    #label_mean=np.mean(Label,0)
    
    ####matrix multiply
    #OLS-min-least 
    ####
    W=(linalg.pinv(A)).dot(Label)
    #print(W)
    #solve-it
    ##### OLS algorithm utilize the mean-point to calculate the 常數
    ###feature_map
    #constant
    #const= (W[0]*feature_mean[0]+W[1]*feature_mean[1]-label_mean)
    #con=con.repeat(len(F1))
    ###utilize-the_mean_value to calculate it 
    #####
    LR = lambda x,y : W[0]*x + W[1]*y#-const
    x2 = y2 = np.arange(0, 60.0)
    X, Y = np.meshgrid(x2, y2)
    #zs = np.array([LR(x2,y2) for x2,y2 in zip(np.ravel(X), np.ravel(Y))])
    #s=np.array([LR(x2,y2) for feature_mean[0], feature_mean[1] in zip(np.ravel(X), np.ravel(Y))])
    ###vector_normal
    V=np.r_[1,W]
    V_normal=V/np.linalg.norm(V)
    #print(V_normal)#(z,x,y)
    return V_normal
#n = norm(X,option) 解完
if __name__ == "__main__":
    #data-input
    #F1_data
    #F1 = np.r_[45.9, 41.3, 10.8, 48.9, 32.8, 19.6, 2.1, 2.6, 5.8, 24, 35.1, 7.6, 32.9, 39.6, 20.5, 23.9, 27.7, 5.1, 15.9, 16.9, 12.6, 3.5, 29.3, 16.7, 27.1, 16, 28.3, 17.4, 1.5, 20, 1.4, 4.1, 43.8, 49.4, 26.7, 37.7, 22.3, 33.4, 27.7, 8.4, 25.7, 22.5, 9.9, 41.5, 15.8, 11.7]
    #F2_data
    #F2 = np.r_[69.3, 58.5, 58.4, 75, 23.5, 11.6, 1, 21.2, 24.2, 4, 65.9, 7.2, 46, 55.8, 18.3, 19.1, 53.4, 23.5, 49.6, 26.2, 18.3, 19.5, 12.6, 22.9, 22.9, 40.8, 43.2, 38.6, 30, 0.3, 7.4, 8.5, 5, 45.7, 35.1, 32, 31.6, 38.7, 1.8, 26.4, 43.3, 31.5, 35.7, 18.5, 49.9, 36.8]
    #label_data
    #Label = np.r_[9.3, 18.5, 12.9, 7.2, 11.8, 13.2, 4.8, 10.6, 8.6, 17.4, 9.2, 9.7, 19, 24.4, 11.3, 14.6, 18, 12.5, 5.6, 15.5, 9.7, 12, 15, 15.9, 18.9, 10.5, 21.4, 11.9, 9.6, 17.4, 9.5, 12.8, 25.4, 14.7, 10.1, 21.5, 16.6, 17.1, 20.7, 12.9, 8.5, 14.9, 10.6, 23.2, 14.8, 9.7]
    ####
    main(F1,F2,Label)
