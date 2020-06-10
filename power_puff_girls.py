''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
import math
numbs=[]
for line in sys.stdin.readlines():
    words=line.split()
    count=len(words)
    for x in range(count):
        numbs=numbs+[int(words[x])]
N=numbs[0]
inc=numbs[1:N+1]
inv=numbs[N+1:N+N+1]

x_compare_ini=math.floor(inv[0]/inc[0])
for x in range(N-1):
    x_compare=math.floor(inv[x]/inc[x])
    if x_compare<=x_compare_ini:
        x_compare_ini=x_compare
print(x_compare_ini)
