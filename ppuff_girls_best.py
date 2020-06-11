''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
import math
import numpy as np

numbs_str=[]
for line in sys.stdin.readlines():
    words=line.split()
    count=len(words)
    numbs_str=numbs_str+words

numbs1=np.array(numbs_str)
numbs=numbs1.astype(int)
N=numbs[0]
inc=numbs[1:N+1]
inv=numbs[N+1:N+N+1]
counts=np.divide(inv,inc)
min_ppg=math.floor(min(counts))
print(min_ppg)
