def counting_sort(arr):
    max_val = max(arr)  # 배열에서 최댓값을 구함
    counts = [0] * (max_val+1)  # 카운트 배열을 생성
    sorted_arr = [0] * len(arr)  # 정렬된 배열을 생성

    # 각 숫자가 나타난 횟수를 카운트, 카운트 배열에 저장
    for num in arr:
        counts[num] += 1

    # 각 숫자의 누적합을 계산
    for i in range(1, max_val+1):
        counts[i] += counts[i-1]

    # 정렬된 배열을 생성
    for num in arr:
        index = counts[num] - 1
        sorted_arr[index] = num
        counts[num] -= 1

    return sorted_arr


arr = [5, 3, 7, 1, 9]
result = counting_sort(arr)
print(result)
