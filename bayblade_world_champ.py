#''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys
import math
import numpy as np
#'Read the input from STDIN'
inlines=[]
for line in sys.stdin.readlines():
    inlines=inlines+line.split()
inlines=np.array(inlines)
inlines=inlines.astype(int)

#'Define the input to proper variables'

T=inlines[0]
T_inc=0
inlines=inlines[1:]
for i in range(T):

    N=inlines[T_inc]
    GRev=inlines[T_inc+1:T_inc+N+1]
    BB=inlines[T_inc+N+1:T_inc+2*N+1]
    T_inc=T_inc+2*N+1

    #'Sorting the power arrays'
    GRev_sort=np.sort(GRev)
    BB_sort=np.sort(BB)

    #'commencing the battle'
    count=0
    for x in BB_sort:
        GR_index=0
        for y in GRev_sort:
            if x<y:
                count=count+1
                GRev_sort=np.delete(GRev_sort,GR_index)
                break
            else:
                GR_index=GR_index+1

    print(count)
