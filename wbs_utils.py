# This file contians functions used within the main data analysis script
import numpy as np 
import math

# # Function to calculate the cumulative sum statistic defiend in the Wild Binary Segmentation Paper
# def cusum_stat(timeseries, s, e, b):

#     timeseries_subset = timeseries[s:(e+1)]
#     n = e - s + 1

#     c_1 = math.sqrt((e - b) / (n * (b - s + 1)))
#     c_2 = math.sqrt((b - s + 1) / (n * (e - b)))

#     X_1 = c_1 * timeseries[s:(b+1)].cumsum()

#     X_2 = -c_2 * timeseries[(b+1):(e+1)].cumsum()

#     alt_weights = np.concatenate((X_1, X_2))

#     return np.dot(alt_weights, timeseries_subset)

# # Function to calculate the critical value of the test
# def critical_val(timeseries, c):
#     return c * np.sqrt(2 * np.log(len(timeseries)))

# # Function to calculate the subsamples which we use for the first loop of the WBS algo
# def gen_sub_samples(s, e, m = 20):
    
#     sub_samples = []
#     while len(sub_samples) < m:
#         end_pt_1 = round(np.random.uniform(low=s, high=e))
#         end_pt_2 = round(np.random.uniform(low=s, high=e))

#         if np.abs(end_pt_1 - end_pt_2) >= 15:
#             sub_samples.append((min(end_pt_1, end_pt_2), max(end_pt_1, end_pt_2)))

#     return sub_samples
    
# # Function to find the breakpoint with the highest CUSUM statistic given the start and end points
# def max_break_point(timeseries, s, e):

#     max_cusum_stat = -math.inf
#     max_break_index = None

#     for i in range(s+1, e):
#         cusum_result = cusum_stat(timeseries, s = s, e = e, b = i)
#         if cusum_result > max_cusum_stat:
#             max_cusum_stat = cusum_result
#             max_break_index = i
    
#     return max_break_index, max_cusum_stat

# # TRIPLE CHECK THIS TO MAKE SURE IT IS CORRECT
# def recurs_wild_binary_seg(timeseries, s, e, c_t, final_breakpoints):
#     #print(s, "   ", e, "    ")
#     if e - s < 15:
#         return final_breakpoints
    
#     # Generate subsamples to start get the best starting breakpoint
#     starting_samples = gen_sub_samples(s = s, e = e, m = 4000)
    
#     max_crit_value = -math.inf
#     start_end_values = (0,0)
#     bp = -1
    
#     # Loop over the initial subsamples to get the first breakpoint
#     for (start, end) in starting_samples:
#         outputs = max_break_point(timeseries, s=start, e = end)
#         if outputs[1] > max_crit_value:
#             max_crit_value = outputs[1]
#             bp = outputs[0]


#     if max_crit_value > c_t:
#         #print("sig at:  ", bp)

#         final_breakpoints.append((bp, max_crit_value))
        
#         #Call wild_binary_seg recursively with everything before BP
#         recurs_wild_binary_seg(timeseries, s = s, e = bp, c_t = c_t, final_breakpoints = final_breakpoints)

#         #Call wild_binary_seg recursively with everything after BP
#         recurs_wild_binary_seg(timeseries, s = bp + 1, e = e, c_t = c_t, final_breakpoints = final_breakpoints)

#     else:
#         return final_breakpoints


# def newest_func(a):
#     print(a)
#     return