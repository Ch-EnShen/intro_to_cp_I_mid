# cython: language_level=3
import numpy as np
cimport numpy as np
cimport cython

cpdef np.ndarray[np.int_t, ndim = 2] IC_gen_quanta_arr(np.ndarray[np.int_t, ndim = 1] quanta_arr, np.ndarray[np.int_t, ndim = 1] maxquanta, int operations_i, int pos):
    cdef int increments = 0
    cdef int doubleN = len(maxquanta)
    cdef np.ndarray[np.int_t, ndim = 2] quanta_comb
    quanta_comb = np.zeros((operations_i, doubleN), dtype = np.int_)
    while increments < operations_i:
        # termination step for one layer of for loop / one iteration of position 
        if quanta_arr[pos] == maxquanta[pos] - 1:
            quanta_arr[pos] = 0
            pos -= 1
        
        # execution for each index in one layer of for loop / one iteration of position
        else:
            quanta_arr[pos] += 1
            increments += 1
            pos = doubleN - 1 #increment the innermost loop
            np.copyto(quanta_comb[(increments - 1), :], quanta_arr)
    
    return quanta_comb
