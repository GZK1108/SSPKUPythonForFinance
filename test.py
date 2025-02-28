import numpy as np

policy = np.random.rand(25, 5)
policy /= policy.sum(axis=1)[:, np.newaxis]
