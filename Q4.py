import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
from scipy.stats import norm

#some initial parameters setting
CL = 95
alpha = 100 - CL

start = "2016-01-01"
end = "2016-12-31"

tickers = ["AAPL", "IBM", "GOOG", "BP", "XOM", "COST", "GS"]
weights = np.array([.15, .20, .20, .15, .10, .15, .05])


#quesion a 

#get the close price for those stocks
data = pdr.get_data_yahoo(tickers, start, end)['Close']
returns = data.pct_change()*100
returns = returns.iloc[1:,:]

PnL = (weights * returns.values).sum(axis=1)

# historic VAR95%
historic_var = np.percentile(PnL, alpha)
print('historic VAR95% is ' + str(round(-historic_var, 2)))

# CVAR95%
historic_cvar = PnL[np.where(PnL < historic_var)].mean()
print('historic CVAR95% is ' + str(round(-historic_cvar, 2)))

'''
historic VAR95% is 1.42
historic CVAR95% is 2.13
'''
# all in percentage, need to multiply the capital to get the VaR


#question b
mean_return = returns.mean()
cov_matrix = returns.cov()
port_mean = mean_return.dot(weights)
port_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

def parametric_var_cvar(mean, std, CL):
    
    VAR = norm.ppf(CL/100) * std - mean
    CVAR = (alpha/100) ** -1 * norm.pdf(norm.ppf(alpha/100))* std - mean
    return VAR, CVAR

results = parametric_var_cvar(port_mean, port_std, CL = 95)

VAR = results[0]
print('parametric method VAR95% is ' + str(round(VAR, 2)))

CVAR = results[1]
print('parametric method CVAR95% is ' + str(round(CVAR, 2)))

'''
parametric method VAR95% is 1.44
parametric method CVAR95% is 1.82
'''

#question c
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import  risk_models
from pypfopt import expected_returns

# set the risk-free rate during that time is 1.7%
risk_free_rate = 0.017

#get the end of month time point
eom = pd.date_range(start, end, freq='M')

'''
Assume the optimal portfolio is based on the max_sharpe,
from the tangency portfolio of Efficient Frontier
'''

def get_optimal_weights(df):
    mean = expected_returns.mean_historical_return(df)
    cov = risk_models.sample_cov(df)
    
    ef = EfficientFrontier(mean, cov, weight_bounds = (None, None))
    
    #set the optimal weights coming from max_sharpe
    weight = ef.max_sharpe(risk_free_rate)
    
    
    return weight

weights = []
for i in eom:
    wei = get_optimal_weights(data[:i])
    weights.append(wei) 

#get the monthly rebalanced weights    
print(pd.DataFrame(weights, index = [i for i in range(1,13)]))
