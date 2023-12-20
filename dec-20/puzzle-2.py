# The value of the rx is determined by the conjunction node dd
# dd should send L value to rx inorder to satisfy the condition
# For that, dd needs to get the input as H from it's all input nodes (4 nodes in the input)
# Here values of the cycle size of each of those nodes to become H
# In order to find the least value, LCM needs to be taken of all of those

import math

print(math.lcm(4013, 3851, 4001, 3911))
