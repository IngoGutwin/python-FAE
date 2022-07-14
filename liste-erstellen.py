

def build_Multi_Arr(inner_arr):
    new_Arr = []
    inner_arr_len = 5
    for i in range(0, inner_arr):
        new_Arr += [[]]
        for j in range(0, inner_arr_len):
            new_Arr[i] += [j]

    return new_Arr


some_arr = build_Multi_Arr(8)

print(some_arr)
