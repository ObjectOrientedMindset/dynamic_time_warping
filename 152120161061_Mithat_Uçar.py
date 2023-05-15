# Modules
import numpy as np # pip install numpy
import pandas as pd # pip install pandas

# Dynamic Time Warping Algorithm
# Algorithm for calculating the distance between two arrays or time series with different length
def dtw(s, t):
    n, m = len(s), len(t)
    dtw_matrix = np.zeros((n+1, m+1))

    # Create DTW matchings table
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0
    
    # the distance between two arrays with length i and j equals the distance between the tails + 
    # the minimum of cost in arrays with length i-1, j , i, j-1 , and i-1, j-1
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(s[i-1] - t[j-1])
            # take last min from a square box
            last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix

# Print DTW results
def print_dtw(reference_data, aligned_data):
    matrix = dtw(reference_data, aligned_data)

    print("Distance is " , matrix[len(reference_data)][len(aligned_data)])
    print("DTW Matchings Table :")
    print(matrix)
    print("Minimum((i-1,j),(i,j-1),(i-1,j-1)) :")
    print(matrix[len(reference_data) -1][len(aligned_data)])
    print(matrix[len(reference_data)][len(aligned_data) -1])
    print(matrix[len(reference_data) -1][len(aligned_data) - 1])

# data1 init
data1 = pd.read_excel("data1.xlsx")
data1_reference = data1["Referance Data"].values.tolist()
data1_reference = data1_reference[:61]
data1_aligned = data1["Aligned Data"].values.tolist()
data1_aligned = data1_aligned[:31]

#data2 init
data2 = pd.read_excel("data2.xlsx")
data2_reference = data2["Referance Data"].values.tolist()
data2_reference = data2_reference[:75]
data2_aligned1 = data2["Aligned Data1"].values.tolist()
data2_aligned1 = data2_aligned1[:71]
data2_aligned2 = data2["Aligned Data2"].values.tolist()
data2_aligned2 = data2_aligned2[:91]
data2_aligned3 = data2["Aligned Data3"].values.tolist()
data2_aligned3 = data2_aligned3[:86]
data2_aligned4 = data2["Aligned Data4"].values.tolist()
data2_aligned4 = data2_aligned4[:89]
data2_aligned5 = data2["Aligned Data5"].values.tolist()
data2_aligned5 = data2_aligned5[:52]
data2_aligned6 = data2["Aligned Data6"].values.tolist()
data2_aligned6 = data2_aligned6[:75]
data2_aligned7 = data2["Aligned Data7"].values.tolist()
data2_aligned7 = data2_aligned7[:75]

# Main
def main():
    print_dtw(data1_reference,data1_aligned)
    # print_dtw(data2_reference,data2_aligned1)
    # print_dtw(data2_reference,data2_aligned2)
    # print_dtw(data2_reference,data2_aligned3)
    # print_dtw(data2_reference,data2_aligned4)
    # print_dtw(data2_reference,data2_aligned5)
    # print_dtw(data2_reference,data2_aligned6)
    # print_dtw(data2_reference,data2_aligned7)

if __name__ == "__main__":
    main()


