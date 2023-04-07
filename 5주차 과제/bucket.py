def bucket_sort(arr):
    # 버킷 크기를 정함
    bucket_size = 10

    # 입력 배열의 최댓값과 최솟값을 구함
    max_val, min_val = max(arr), min(arr)

    # 버킷 리스트를 생성
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # 배열의 값을 버킷에 할당
    for num in arr:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)

    # 각 버킷을 정렬하고, 정렬된 값들을 리스트에 병합
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

arr = [5, 3, 7, 1, 9]
result = bucket_sort(arr)
print(result)
