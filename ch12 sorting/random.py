from quicksort import quick_sort
import random
random_items = [random.randint(0,1000) for c in range(1000)]

import time
start = time.clock()
quicksort.quick_sort(random_items)
end = time.clock()
elapsed_time = end - start
print('elasped time for sort_method ()',elapsed_time)