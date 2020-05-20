# arr= [1,2,3]
# i=0
# j=0
# for i in range(i, len(arr)):
#     for j in range(i, len(arr)):
#     print(arr[:,i])
    # i += 1
# for j in range(j,len(arr)):
#     print(arr[j],arr[j+1])
#     # j += 1


# arr = [1, 2, 3, 4]
# start = 0
# while start < len(arr):
#     end = start
#     while end < len(arr):
#         print(arr[start:end + 1])
#         end += 1
#    start += 1
# arr = [1,2,3]
# for i in range (len(arr)):
#
#     for j in range (len(arr)):
#         sub_arr = []
#         sub_arr = sub_arr.append(arr[j])
#     print(sub_arr)


arr = [1, 3, 2, -3, 5, -5]
mx = -10000000000
con_sum = 0
for i in range(len(arr)):
    con_sum += arr[i]
    if con_sum > mx:
        mx = con_sum

    if con_sum < 0:
        con_sum = 0
print(mx)


