def get_arr_from_input():
    return [int(x) for x in input().split()]

N,Q = get_arr_from_input()
arr_length = N
arr = get_arr_from_input()

for _ in range(Q):
    query = get_arr_from_input()
    if query[0] == 1:
        arr[query[1]-1] = int(not arr[query[1]])
        continue
    elif arr[query[2]-1] == 0:
        print("EVEN")a
    else:
        print("ODD")

# def query_1(arr):
#     query, flip_bit = [int(x) for x in input().split()]
#     if query == 1:
#         if arr[flip_bit-1] == 1:
#             arr[flip_bit-1] = 0
#         else:
#             arr[flip_bit-1] = 1
#
#
# def query_0(arr):
#     query,start,end = [int(x) for x in input().split()]
#     if query == 0:
#         if arr[end-1] == 1:
#             print("ODD")
#         else:
#             print("EVEN")
#
# for i in range(Q):
#     query_1(arr) or  query_0(arr)
