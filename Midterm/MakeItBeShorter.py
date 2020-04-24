from visualization import visualize
def update_dic_position_degree( x,y ,dic_position_degree):#note: dictionary are mutable
    dic_position_degree[(x,y)]=999999
    for (i,j) in dic_position_degree.keys():
        for (k,l) in [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]:
            if (i+k,j+l)==(x,y) and dic_position_degree[(i,j)]>=1:
                dic_position_degree[(i,j)]-=1

def knightTour(n, start_x, start_y):
    d_map=[[8 for x in range(n)] for y in range(n)]
    for step in range(n):
        d_map[0][step]=4
        d_map[n-1][step]=4
        d_map[step][0]=4
        d_map[step][n-1]=4
    for step in range(n-2):
        d_map[1][step+1]=6
        d_map[n-2][step+1]=6
        d_map[step+1][1]=6
        d_map[step+1][n-2]=6
    for (i,j) in [(0,0),(n-1,n-1),(0,n-1),(n-1,0)]:
        d_map[i][j]=2
    for (i,j) in [(0,1),(1,0),(n-2,0),(n-1,1),(0,n-2),(1,n-1),(n-2,n-1),(n-1,n-2)]:
        d_map[i][j]=3
    for (i,j) in [(1,1),(1,n-2),(n-2,1),(n-2,n-2)]:
        d_map[i][j]=4
    dic_position_degree={(x,y):d_map[x][y] for x in range(n) for y in range(n)}#key=position,value=degree
    dic_position_steps={}#key=position,value=which step
    next=(start_x, start_y)
    for step in range(n*n):
        (x,y)=next #stand at (x,y) now
        dic_position_steps[(x,y)]=step #update dic_position_steps
        update_dic_position_degree(x,y,dic_position_degree)
        tmp=999999 #find the next move
        for (i,j) in [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]:
            if (x+i)>=0 and (x+i)<n and (y+j)>=0 and (y+j)<n and dic_position_degree[(x+i),(y+j)]<tmp:
                tmp=dic_position_degree[(x+i),(y+j)]
                next=((x+i),(y+j))
        if dic_position_degree[next]>8 and step!=n*n-1: #The KnightTour couldn't be finished
            return n,dic_position_steps,2
    return n,dic_position_steps,0
(N,dic,errCode)=knightTour(20, 4, 5) #20*20 Matrix ,start at (4,5)
visualize( N,dic,errCode )
