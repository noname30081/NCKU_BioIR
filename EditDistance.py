

def MED(sent_01, sent_02):
    n = len(sent_01)
    m = len(sent_02)
    matrix = [[i+j for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if sent_01[i-1] == sent_02[j-1]:
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)
    distance_score = matrix[n][m]
    return distance_score