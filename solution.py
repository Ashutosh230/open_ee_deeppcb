# solar_panels 
import math 
  
def isPerfectSquare(x): 
  
    # Find floating point value of  
    # square root of x. 
    sr = math.sqrt(x) 
   
    # If square root is an integer 
    return ((sr - math.floor(sr)) == 0) 
  
def solution(area):
    square_list = list()
    actual_area = area
    while(area>0):
        if(isPerfectSquare(area)):
            square_list.append(area)
            area = actual_area - area
            actual_area = area
        else:
            area-=1
    return square_list



