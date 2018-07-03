from __future__ import print_function

import tensorflow as tf

a = 1
b = 1
c = 1

matrix_a = tf.constant([[a, a], [a, a]])
matrix_b = tf.constant([[b, b], [b, b]])
matrix_c = tf.constant([[c, c], [c, c]])

"""
First, matrix_a is raised to the 2nd power, then added to matrix_b.
The result of that computation is the multiplied by matrix_c. 
"""
result = tf.matmul(tf.add(tf.pow(matrix_a, 2), matrix_b), matrix_c)

with tf.Session() as _session:
    answer = _session.run(result)
    print(answer)
