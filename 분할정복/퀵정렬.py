def quick_sort(data):
    # 데이터의 길이가 1이라면 더이상 정렬할 필요가 없다.
    if len(data) <= 1:
        return data

    pivot = data[0]
    left_data = []
    right_data = []

    for i in data[1:]:
        if i >= pivot:
            right_data.append(i)
        else:
            left_data.append(i)
	
    # 각각 정렬된 값들을 다시 붙이기
    return quick_sort(left_data) + [pivot] + quick_sort(right_data)
