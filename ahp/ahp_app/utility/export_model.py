import numpy as np

# Calculate the consistency ratio
RI_TABLE = [0, 0, 0.58, 0.90, 1.12, 1.24,
            1.32, 1.41, 1.45, 1.49]  # Look-up Table


class AHPModel:
    """AHP Model"""

    def __init__(self, CRITERIA, SUBCRITERIA, ALTERNATIVE):
        self.A = CRITERIA  # A is the criteria
        self.SUBCRITERIA = SUBCRITERIA
        self.ALTERNATIVE = ALTERNATIVE

    def get_size(self, A):
        row = len(A)
        col = len(A[0])
        return [row, col]

    def aggregate(self, A):
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

    def vector_sum_aggregate(self, R):
        r1, r2, r3 = 0, 0, 0
        for R_row in R:
            r1 = r1 + R_row[0]
            r2 = r2 + R_row[1]
            r3 = r3 + R_row[2]
        v_sum = [1/r1, 1/r2, 1/r3]
        v_sum = sorted(v_sum, reverse=False)
        return v_sum

    def find_fuzzy_weight(self, R, v_sum):
        w1, w2, w3 = [], [], []
        for R_row in R:
            w1.append(R_row[0] * v_sum[0])
            w2.append(R_row[1] * v_sum[1])
            w3.append(R_row[2] * v_sum[2])
        # Note that the Order of this Result is now in Columns instead of rows for the previous functions
        return [w1, w2, w3]

    def defuziffy(self, W):
        M = []
        L = len(W[0])
        for l in range(0, L):
            M.append((W[0][l] + W[1][l] + W[2][l])/3)
        return M

    def normalize(self, M):
        m_sum = sum(M)
        M_norm = []
        for m in M:
            M_norm.append(m/m_sum)
        return M_norm

    def eigen(self, M_norm):
        N = len(M_norm)
        W = []
        for m in M_norm:
            W.append(m/N)
        return W

    def get_consistency_ratio(self, eigenvector):
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

    def evaluate_criteria(self):
        # Aggregate Criteria
        R = self.aggregate(self.A)
        # Vector Sum
        v_sum = self.vector_sum_aggregate(R)
        # Get Fuzzy Weight
        W = self.find_fuzzy_weight(R, v_sum)
        # print(np.transpose(W))
        # Defuziffy
        M = self.defuziffy(W)
        # Normalize
        M_norm = self.normalize(M)
        # Engenvector
        eigenvector = self.eigen(M_norm)
        # Consistency Ratio
        consis_ratio = self.get_consistency_ratio(eigenvector)
        return [consis_ratio, eigenvector]

    def evaluate_subcriteria(self, criterialIndex):
        R = self.aggregate(self.SUBCRITERIA[criterialIndex])
        # Vector Sum
        v_sum = self.vector_sum_aggregate(R)
        # Get Fuzzy Weight
        W = self.find_fuzzy_weight(R, v_sum)
        # print(np.transpose(W))
        # Defuziffy
        M = self.defuziffy(W)
        # Normalize
        M_norm = self.normalize(M)
        # Engenvector
        eigenvector = self.eigen(M_norm)
        # Consistency Ratio
        consis_ratio = self.get_consistency_ratio(eigenvector)
        return [consis_ratio, eigenvector]

    def evaluate_alternative(self, SB_ALTERNATIVE):
        R = self.aggregate(SB_ALTERNATIVE)
        # Vector Sum
        v_sum = self.vector_sum_aggregate(R)
        # Get Fuzzy Weight
        W = self.find_fuzzy_weight(R, v_sum)
        # print(np.transpose(W))
        # Defuziffy
        M = self.defuziffy(W)
        # Normalize
        M_norm = self.normalize(M)
        # Engenvector
        eigenvector = self.eigen(M_norm)
        # Consistency Ratio
        consis_ratio = self.get_consistency_ratio(eigenvector)
        return [consis_ratio, eigenvector]

    def get_alternative_global_weights(self):
        sb_weights = self.get_global_weight()
        if sb_weights is None:
            return None
        sb_weights = np.ndarray.flatten(sb_weights)
        # Loop tru each of the subCriteria for the local weights of the Alternative realtive to each.
        alternative_local_weights = [[] for i in range(
            len(self.evaluate_alternative(self.ALTERNATIVE[0])))]
        for alt_mat in self.ALTERNATIVE:
            alt_local_weights = self.evaluate_alternative(alt_mat)
            for i in range(0, len(alt_local_weights)):
                alternative_local_weights[i].append(alt_local_weights)

        alternative_global_weights = []
        numOfAlternative = len(alt_local_weights)  # Number of Contractors
        for altIndex in range(0, numOfAlternative):
            givenAltWeight = []
            for sbIndex in range(0, len(sb_weights)):
                givenAltWeight.append(
                    sb_weights[sbIndex] * alternative_local_weights[altIndex][sbIndex])
            alternative_global_weights.append(givenAltWeight)
        return alternative_global_weights

    def rank_alternatives(self):
        alternative_global_weights = self.get_alternative_global_weights()
        priority_weight = []
        for each_weight in alternative_global_weights:
            priority_weight.append(sum(each_weight)/len(each_weight))
        priority_weight = sorted(((weight, index)
                                  for index, weight in enumerate(priority_weight)), reverse=True)
        return priority_weight

    def get_global_weight(self):
        criterial_weights = self.evaluate_criteria()
        globalWeights = []
        numOfCriteria = len(self.A)
        for crt in range(0, numOfCriteria):
            sb_local_weight = self.evaluate_subcriteria(crt)
            if sb_local_weight[0][1] == 'Acceptable':
                eigenvector = sb_local_weight[1]
                sb_weights = []
                for eig in eigenvector:
                    sb_weights.append(eig * criterial_weights[crt])
            else:
                return None
            globalWeights.append(sb_weights)
        return globalWeights

    def get_qualified_alternatives(self, threshold):
        priority_weights = self.rank_alternatives()
        return priority_weights[:threshold-1]

    def get_final_alternative(self, bid_price, estimated_price, threshold):
        selected_alternative = self.get_qualified_alternatives(threshold)
        selected_index = []
        selected_price = []
        for sel in selected_alternative:
            selected_index.append(sel[1])
            selected_price.append(estimated_price - bid_price[sel[1]])
        [selection, selectedIndex] = [
            min(selected_price), selected_index[np.argmin(selected_price)]]
        return selectedIndex

    def evaluate(self, bid_price, estimated_price, threshold, contractors):
        # Contractors - Names of the contractors
        selected_contractor = self.get_final_alternative(
            bid_price, estimated_price, threshold)
        selected_contractor = contractors[selected_contractor]
        return selected_contractor


# 
def generate_mirror_matrix(upper_matrix):
    """ A funtion for genration of lower matrix mirror for AHP model """





# TEST MODULE

C = [
    [[1, 1, 1], [1, 1, 1], [4, 5, 6], [6, 7, 8], [4, 5, 6]],
    [[1, 1, 1], [1, 1, 1], [4, 5, 6], [6, 7, 8], [6, 7, 8]],
    [[1/6, 1/5, 1/4], [1/6, 1/5, 1/4], [1, 1, 1], [1/4, 1/3, 1/2], [2, 3, 4]],
    [[1/8, 1/7, 1/6], [1/8, 1/7, 1/6], [2, 3, 4], [1, 1, 1], [1/6, 1/5, 1/4]],
    [[1/6, 1/5, 1/4], [1/8, 1/7, 1/6], [1/4, 1/3, 1/2], [4, 5, 6], [1, 1, 1]]
]

SBC1 = [
    [[1,1,1], [2,3,4], [0.111,0.111,0.124], [7,8,9]],
    [[0.25, 0.333, 0.5], [1,1,1], [4,5,6], [0.25, 0.333, 0.5]],
    [[8,9,9], [0.1667,0.2,0.25], [1,1,1], [7,8,9]],
    [[0.111, 0.125, 0.149], [2,3,4], [0.111, 0.125, 0.149], [1,1,1]]

]

SBC2 = [
    [[1,1,1], [5,6,7], [0.125,0.1429,0.1667], [1,2,3]],
    [[0.1429, 0.1667, 0.2], [1,1,1], [4,5,6], [0.25, 0.333, 0.5]],
    [[8,9,9], [0.1667,0.2,0.25], [1,1,1], [7,8,9]],
    [[0.111, 0.125, 0.149], [2,3,4], [0.111, 0.125, 0.149], [1,1,1]]

]

####################################################################
################  DATA STRUCTURE  ##################################
# STEP 1: Pairwise comaprison of the first level of the heirachy:
# CRITERIA and SubCriteria

CRITERIA_MATRIX = []   # TBD
SUBCRITERIA_MATRIX = []
ALTERNATIVE_MATRIX = []
bid_price = 0
estimated_price = 0
threshold = 0
contractor_names = []

cModel = AHPModel(CRITERIA_MATRIX, SUBCRITERIA_MATRIX, ALTERNATIVE_MATRIX)
global_weights = cModel.get_global_weight()
if global_weights is None:
    print('The CR is unacceptable, kindly review the pairwise comparison matrix.')
else:
    print(global_weights)


# STEP 2: The SubCriteria Matrix Local Weight
# Given that there are x subcriteria under criteria k, we will get the local weight for the subcriteria matrix under criteria k
