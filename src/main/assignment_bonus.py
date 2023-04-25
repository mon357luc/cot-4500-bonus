"""This is a bonus assignment outlining the results of the Gauss-Seidel, Jacobi,
Newton-Raphson, Dvidied Differences, and Modified Euler methods"""

import numpy as np

convergence_matrix = np.array([[3,1,1,1],[1,4,1,3],[2,3,7,0]])
intial_convergence_guess = np.array([0,0,0])
tolerance = 1e-6
iterations = 50

def jacobi_method(c_matrix, t_val, i_val):
    "This function performs the jacobi method for convergence"
    solution_arr = np.zeros(c_matrix.shape[0])
    old_arr = solution_arr.copy()
    count = 0
    for iter in range(i_val):
        count += 1
        for i in range(c_matrix.shape[0]):
            solution_arr[i] = calculate_x_i(c_matrix, i, solution_arr)
        print(f'iteration {iter+1}: solution_arr={solution_arr}, old_arr={old_arr}')
        if np.all((abs(solution_arr - old_arr)) < t_val):
            break
        old_arr[:] = solution_arr
    print(count)

def calculate_x_i(c_matrix, row_i, old_est):
    "Calculates x_i based on given matrix and current row"
    calc_arr = c_matrix[row_i, :]/c_matrix[(row_i, row_i)]
    
    x_i = calc_arr[calc_arr.shape[0] - 1]
    x_i -= np.dot(calc_arr[~row_i], old_est[~row_i])
    return x_i

def diagonally_dominant_matrix(input_matrix):
    "This function creates a diagonally dominant matrix, if possible. Else it returns None"
    a_val = input_matrix.shape[0] if input_matrix.shape[0] < input_matrix.shape[1] \
        else input_matrix.shape[1]
    pos_arr = np.full(a_val, -1, int)
    for i in range(a_val):
        max_pos_val = 0
        for j in range(a_val):
            max_pos_val = max_pos_val if abs(input_matrix[(i, max_pos_val)]) >= \
                abs(input_matrix[(i, j)]) else j
        if max_pos_val in pos_arr:
            return None
        pos_arr[i] = max_pos_val
    for i in range(a_val):
        if i == pos_arr[i]:
            continue
        if abs(input_matrix[(i, i)]) < abs(input_matrix[(i, pos_arr[i])]):
            input_matrix[[i, pos_arr[i]], :] = input_matrix[[pos_arr[i], i], :]
    return input_matrix

convergence_matrix = diagonally_dominant_matrix(convergence_matrix)
if convergence_matrix is not None:
    jacobi_method(convergence_matrix, tolerance, iterations)
else:
    str = """This matrix is not diagonally dominant,
        and therefore cannot have the Jacobi nor
        gauss-Seidal methods applied to it"""
    print(str)
