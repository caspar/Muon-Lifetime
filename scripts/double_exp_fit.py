import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt

def single_exp(t, N0, tau, b):
    return N0 * np.exp(- t / tau) + b

def f(t, N1, tau1, N2, tau2, C):
    return N1 * np.exp(- t / tau1) + N2 * np.exp(- t / tau2) + C

if __name__ == "__main__":
    nbins = 10
    N = 10000
    data = pd.read_csv("../data/first_dataset.txt").values
    counts, bin_edges = np.histogram(data, bins=nbins)
    p0 = [counts[0] , np.mean(data) , counts[0]/2, 1.5 * np.mean(data) , 1 ]
    xdata = (bin_edges[:-1] + bin_edges[1:]) / 2.
    x = np.linspace(xdata.min(), xdata.max(), N)
    popt, pcov = curve_fit(f, xdata, counts, p0=p0)
    print("Variance: \n" ,np.diag(pcov))
    plt.style.use('seaborn')
    print("Mean of counts: {}".format( p0[1] ))
    print("Fitted value for muon lifetime: {} (ns)".format( popt[1] ))

    # NOTE: the fitting converges and works well, but realize that the variance
    # on the parameters is enormous. hopefully more data will fix this issue.
    # can't even plot 1 sigma bounds for the fit
    fig,ax = plt.subplots(1, figsize=(10,10))
    ax.scatter(x=xdata, y=counts, label='data', color='black')
    ax.plot(x, f(x, *popt), label='Double Exponential Fit', color='green')
    ax.plot(x, single_exp(x, *popt[:3]), label='Signal',\
            linestyle='dashed',color='red')
    ax.plot(x, single_exp(x, *popt[3:]), label='Background', \
            linestyle='dashed',color='black')
    ax.set_xlabel(r"Time interval (ns)")
    ax.set_ylabel("Counts")
    ax.legend()
    ax.set_title("Double Exponential Fit")
    plt.show()
