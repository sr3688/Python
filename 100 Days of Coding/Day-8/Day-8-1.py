# one cane of paint is used for painting 5 metre square of the wall find the no. of canes if the height and width of the wall is given to be painted
import math
wall_height=int(input("Enter the height of the wall(m): "))
wall_width=int(input("Enter the width of the wall(m): "))

def cane_no_calc(height,weidth):
    no_of_canes= (height*weidth)/5
    return no_of_canes

print(f"The number of canes rquired to piant the desired wall is {math.floor(cane_no_calc(wall_height,wall_width))}")