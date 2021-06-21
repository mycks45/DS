
import numpy
# while True:
#     y = int(input('enter no whose table you want: '))

#     for x in range(1,11):
#         ans = x*y
#         print(x,'x',y,'= ',ans)

#     res = input('Continue Y/N : ')

#     if res == 'N' or res == 'n':
#         break


# time =[
#     [{1:False},{3:False},{4:False},{5:False}],
#     [{1:False},{3:False},{4:False},{5:False}],
#     [{1:False},{3:False},{4:False},{5:False}],
    
# ]
# vist = [False,False]
# print(time[1][0])
# print(vist)
# print(len(time[2]))



checkRiverSize = [
    [1,2,4,6,3],
    [1,2,8,6,3],
    [1,2,4,6,3],
]
visited = [ [False] * len(checkRiverSize[0]) ] * len( checkRiverSize )
sizes = []


print(visited)

a='fhfgfghf'
b=list(a)
b[2] ='6'
y=''
gh=y.join(b)
print(gh)