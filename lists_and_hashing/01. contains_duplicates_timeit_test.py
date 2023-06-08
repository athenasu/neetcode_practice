import timeit

setup = 'from contains_duplicates import Solution'

test_method_dict = '''
def test():
    my_list = [1, 2, 3, 1]
    my_solutions = Solution()
    return my_solutions.contains_dupe_using_dict(my_list)
'''

test_method_set = '''
def test_set():
    my_list = [1, 2, 3, 1]
    my_solutions = Solution()
    return my_solutions.contains_dupe_using_set(my_list)
'''

times_using_dict = timeit.repeat(setup= setup, stmt=test_method_dict, repeat=5)
times_using_set = timeit.repeat(setup= setup, stmt=test_method_set, repeat=5)
print(f'Min time using dictionary:{min(times_using_dict)}')
print(f'Min time using set:{min(times_using_set)}')