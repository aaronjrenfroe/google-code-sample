def solution(P, K):
    # write your code in Python 3.6
    # P is list
    # K is number of groups
    bed = ['.'] * len(P)
    
    for i, val in enumerate(P):
        bed[val - 1] = '1'
        bed_str = ''.join(bed)
        print(bed_str)
        bed_str = [lst for lst in bed_str.split('.') if len(lst) > 0]
        
        if len(bed_str) == K:
            print(bed_str)
            return i + 1

    return 'impossible'

print(solution([3,1,5,4,2], 3))

