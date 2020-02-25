import pandas as pd
import seaborn as sn
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats

weatherData = pd.read_csv('C:/Users/sajith/Desktop/normalize1.csv')
weatherD = weatherData[['Page_Rank','Hub','Authority','Similarity','pr']]
correalationWeather = weatherD.corr()

sn.heatmap(correalationWeather,annot=True, fmt='.1f',cmap='Blues_r')
sn
