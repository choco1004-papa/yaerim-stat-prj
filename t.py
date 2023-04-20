import numpy as np

text = '  -22.3,-21.7, -23.1,-35.9,-  '
t_list = text.split(',')
t_array = np.array(t_list)
t_array = t_array.astype(np.float32)
print(t_array)