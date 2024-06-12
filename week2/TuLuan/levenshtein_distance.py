def levenshtein_distance(source, target):
    source_len = len(source)
    target_len = len(target)
    source = "#" + source
    target = "#" + target
    matrix = [[0 for _ in range(target_len + 1)]
              for _ in range(source_len + 1)]
    for i in range(source_len + 1):
        matrix[i][0] = i
    for i in range(target_len + 1):
        matrix[0][i] = i
    for i in range(1, source_len + 1):
        for j in range(1, target_len + 1):
            sub_cost = 1
            if source[i] == target[j]:
                sub_cost = 0
            matrix[i][j] = min(
                matrix[i-1][j] + 1, min(matrix[i][j - 1] + 1, matrix[i-1][j - 1] + sub_cost))
    print(matrix[source_len][target_len])


levenshtein_distance("yu", "you")
