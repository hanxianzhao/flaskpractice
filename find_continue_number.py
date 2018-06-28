'''
一组数中有几段连续的数，怎么把这几段连续的数字取出来？
如：
一组数
a=[ 11 12 13 14 15 22 23 24 25 26 27 34 35 36 37 38 41 42]
取出结果
[11 12 13 14 15]
[22 23 24 25 26 27]
[34 35 36 37 38]
[41 42]
'''

def find(old_list):
    new_list=[]
    n=1
    while n < len(old_list):
        if old_list[n]-old_list[n-1] == 1:
            new_list.append(old_list[n-1])
            if n==len(old_list)-1:
                new_list.append(old_list[n])
                print(new_list)
                return
        else:
            if len(new_list)>=2:
                new_list.append(old_list[n-1])
                print(new_list)
                new_list=[]
            else:
                pass
        n+=1
old_list=[11,12,13,14,15,22,23,24,25,26,27,34,35,36,37,38,39,41,42]
find(old_list)