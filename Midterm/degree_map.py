def create_d_map(n):
    d_map=[]
    for x in range(n):
        d_map.append([])
        for y in range(n):
            d_map[x].append(8)

    for step in range(n):
        d_map[0][step]=4
        d_map[n-1][step]=4
        d_map[step][0]=4
        d_map[step][n-1]=4
        for (i,j) in [(0,0),(n-1,n-1),(0,n-1),(n-1,0)]:
            d_map[i][j]=2
        for (i,j) in [(0,1),(1,0),(n-2,0),(n-1,1),(0,n-2),(1,n-1),(n-2,n-1),(n-1,n-2)]:
            d_map[i][j]=3


    for step in range(n-2):
        d_map[1][step+1]=6
        d_map[n-2][step+1]=6
        d_map[step+1][1]=6
        d_map[step+1][n-2]=6
        for (i,j) in [(1,1),(1,n-2),(n-2,1),(n-2,n-2)]:
            d_map[i][j]=4

    # #print ans
    # for x in range(n):
    #     for y in range(n):
    #         print(format(d_map[x][y],'5'),end='')
    #     print('\n')

    return d_map



# def main():
#     while True:
#         n=int(input('n='))
#         if n== -1:
#             break;
#         create_d_map(n)
#
#
#
# main()
