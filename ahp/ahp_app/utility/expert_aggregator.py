import numpy as np


def get_size(A):
    row = len(A)
    col = len(A[0])
    return [row, col]


def aggregate(A):
    ri = []
    for Ar in A:
        r1, r2, r3 = 1, 1, 1
        for k in range(0, len(Ar)):
            r1 = r1 * Ar[k][0]
            r2 = r2 * Ar[k][1]
            r3 = r3 * Ar[k][2]
        r = [pow(r1, 1/len(Ar)), pow(r2, 1/len(Ar)), pow(r3, 1/len(Ar))]
        ri.append(r)
    return ri


def vector_sum_aggregate(R):
    r1, r2, r3 = 0, 0, 0
    for R_row in R:
        r1 = r1 + R_row[0]
        r2 = r2 + R_row[1]
        r3 = r3 + R_row[2]
    v_sum = [1/r1, 1/r2, 1/r3]
    v_sum = sorted(v_sum, reverse=False)
    return v_sum


def find_fuzzy_weight(R, v_sum):
    w1, w2, w3 = [], [], []
    for R_row in R:
        w1.append(R_row[0] * v_sum[0])
        w2.append(R_row[1] * v_sum[1])
        w3.append(R_row[2] * v_sum[2])
    # Note that the Order of this Result is now in Columns instead of rows for the previous functions
    return [w1, w2, w3]


def defuziffy(W):
    M = []
    L = len(W[0])
    for l in range(0, L):
        M.append((W[0][l] + W[1][l] + W[2][l])/3)
    return M


def normalize(M):
    m_sum = sum(M)
    M_norm = []
    for m in M:
        M_norm.append(m/m_sum)
    return M_norm


def eigen(M_norm):
    N = len(M_norm)
    W = []
    for m in M_norm:
        W.append(m/N)
    return W


# 18-08-2018
# Calculate the consistency ratio
RI_TABLE = [0, 0, 0.58, 0.90, 1.12, 1.24,
            1.32, 1.41, 1.45, 1.49]  # Look-up Table


def get_consistency_ratio(eigenvector):
    # CI - Index
    # RI - Random Consistency Index
    n = len(eigenvector)
    #  Get A = wi/wj = eigenvector/wj
    A = []
    for i in range(0, len(eigenvector)):
        Wr, w = [], eigenvector[i]
        for wc in eigenvector:
            Wr.append(w/wc)
        A.append(Wr)
    # Get A*wi
    AWi = np.matmul(A, eigenvector)
    # wi - eigenvector
    lamda_max = sum(AWi) / sum(eigenvector)
    lamda_max = lamda_max/n

    CI = (lamda_max - n)/(n-1)
    # Get RI
    if n > 10 or n < 1:
        n = 10
    RI = RI_TABLE[n - 1]
    consistency_ratio = CI/RI
    if consistency_ratio < 0.1:
        status = 'Acceptable'
    else:
        status = 'Unacceptable'
    return [consistency_ratio, status]


#  NOTE That The EigenVaecto is the same as the Local Weight



# TEST
C = [
    [[1, 1, 1], [1, 1, 1], [4, 5, 6], [6, 7, 8], [4, 5, 6]],
    [[1, 1, 1], [1, 1, 1], [4, 5, 6], [6, 7, 8], [6, 7, 8]],
    [[1/6, 1/5, 1/4], [1/6, 1/5, 1/4], [1, 1, 1], [1/4, 1/3, 1/2], [2, 3, 4]],
    [[1/8, 1/7, 1/6], [1/8, 1/7, 1/6], [2, 3, 4], [1, 1, 1], [1/6, 1/5, 1/4]],
    [[1/6, 1/5, 1/4], [1/8, 1/7, 1/6], [1/4, 1/3, 1/2], [4, 5, 6], [1, 1, 1]]
]
print('Aggregate Criteria')
R = aggregate(C)
print(R)
print('Vector Sum')
print(vector_sum_aggregate(R))

print('Get Fuzzy Weight')
v_sum = vector_sum_aggregate(R)

print(find_fuzzy_weight(R, v_sum))
print('Defuziffy')
W = find_fuzzy_weight(R, v_sum)
print('Fuzzy Weight Transposed: ')
print(np.transpose(W))

print(defuziffy(W))


print('Normalize')
M = defuziffy(W)
print(normalize(M))
print('Engenvector')
M_norm = normalize(M)
print(eigen(M_norm))

eigenvector = eigen(M_norm)
consis_ratio = get_consistency_ratio(eigenvector)
print('Consistency Ratio')
print(consis_ratio)
