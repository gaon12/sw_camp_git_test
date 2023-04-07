def radix_sort(arr):
    # 배열에서 최댓값의 자릿수를 구함
    max_val = max(arr)
    max_digit = len(str(max_val))

    # 자릿수별로 정렬
    for digit in range(max_digit):
        buckets = [[] for _ in range(10)]  # 0~9번 버킷을 생성
        for num in arr:
            # 해당 자릿수의 값을 구함
            digit_val = num // 10**digit % 10
            buckets[digit_val].append(num)

        arr = [num for bucket in buckets for num in bucket]

    return arr


arr = [521, 421, 125, 750, 390]
result = radix_sort(arr)
print(result)
