import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from sklearn.gaussian_process import GaussianProcess

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2017, 3, 27)

f = web.DataReader('F','google', start, end)
f = f['Close']

# f.plot(alpha=0.5, style='-')
# f.resample('BA').mean().plot(style=':')
# f.asfreq('BA').plot(style='--');
# plt.legend(['input', 'resample', 'asfreq'],
#            loc='upper left');

f = f.asfreq('D', method='pad')

ROI = 100 * (f.tshift(-7) / f - 1)
ROI.plot()
plt.ylabel('% Return on Investment');