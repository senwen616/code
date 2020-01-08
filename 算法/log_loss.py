from sklearn.metrics import log_loss
# from sklearn.preprocessing import OneHotEncoder
# import numpy as np
#
# from sklearn.preprocessing import LabelEncoder
# encoder = LabelEncoder()
#
# labels = encoder.fit_transform(["REAL","FAKE"])
# print labels
# print np.reshape(labels, (-1,1))

print log_loss(["REAL", "FAKE", "FAKE", "REAL"],
         [[.1, .9], [.9, .1], [.8, .2], [.35, 065]])
# one_hot = OneHotEncoder(n_values=2, sparse=False)
# print one_hot.fit_transform(np.reshape(labels, (-1,1)))