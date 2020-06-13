def main():
    T=int(input())

    for i in range(T):

        N=int(input())
        GRev_in=input().split()
        GRev=[]
        for x in GRev_in:
            GRev.append(int(x))
        BB_in=input().split()
        BB=[]
        for x in BB_in:
            BB.append(int(x))

        #'Sorting the power arrays'
        GRev.sort()
        BB.sort()

        #'commencing the battle'
        

        count=0
        for x in BB:
            for y in GRev:
                if x<y:
                    count+=1
                    GRev.remove(y)
                    break
        print(count)

main()
