import numpy as np

line = '123456,1234566,1234555,2141243'

bid_1 = line.strip().split(',')

linw_2 = 'safasdf,sdadfa,q4r4r3q'

bid_2 = linw_2.strip().split(',')

bid_items = np.vstack((bid_1, bid_2))

print(bid_items)
