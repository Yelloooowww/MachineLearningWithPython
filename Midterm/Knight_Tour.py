from degree_map import create_d_map

eight_moves = [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]
def init_dic_position_degree(n):
    dic_position_degree={}
    for x in range(n):
        for y in range(n):
            dic_position_degree[(x,y)]=create_d_map(n)[x][y]
    return dic_position_degree

#note: dictionary are mutable
def update_dic_position_degree( x,y ,dic_position_degree):
    dic_position_degree[(x,y)]=999999
    for (i,j) in dic_position_degree.keys():
        for (k,l) in eight_moves:
            if (i+k,j+l)==(x,y) and dic_position_degree[(i,j)]>=1:
                dic_position_degree[(i,j)]-=1

def knightTour(n, start_x, start_y):
    dic_position_steps={}
    dic_position_degree=init_dic_position_degree(n)
    next=(start_x, start_y)

    for step in range(n*n):
        (x,y)=next
        dic_position_steps[(x,y)]=step
        update_dic_position_degree(x,y,dic_position_degree)

        tmp=999999
        for (i,j) in eight_moves:
            if (x+i)>=0 and (x+i)<n and (y+j)>=0 and (y+j)<n and dic_position_degree[(x+i),(y+j)]<tmp:
                tmp=dic_position_degree[(x+i),(y+j)]
                next=((x+i),(y+j))
        if next==(x,y) and step!=n*n-1:
            # print('step=',step,' I stay at (',x,',',y,') with no possible movement')
            return dic_position_steps,1
        if dic_position_degree[next]>8 and step!=n*n-1:
            # print('step=',step,' I don\'t know how to do  at (',x,',',y,').')
            return dic_position_steps,2

    return dic_position_steps,0




(dic,err)=knightTour(10, 0, 0)
if err==0:
    for x in range(10):
        for y in range(10):
            print(format(dic[x,y],'5'),end='')
        print('\n')

# for N in range(8,31,1):
#     for x in range(N):
#         for y in range(N):
#             (dic,err)=knightTour(N,x,y)
#             if err!=0:
#                 print('N=',N,'start at:',x,',',y,'errCode:',err)
