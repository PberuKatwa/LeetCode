# Consider an array arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}, and the target = 23.

def find_target( array:list, target:int ):
    start = 0
    end = len(array) - 1

    for i in range(1,len(array)):
        
        while start < end:

            mid = ( start + end  ) // 2

            print("start end",start, end,"midddd", mid, "numss", array[mid])

            if array[mid] == target:
                return mid
            elif array[mid] < target:
                start = mid + 1
            else:
                end = mid - 1


    return -1


print( find_target( [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 26 ) )