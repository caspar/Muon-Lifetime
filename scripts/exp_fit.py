import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt

def f(t, N0, tau, b):
    return N0 * np.exp(- t / tau) + b

if __name__ == "__main__":
    nbins = 10
    N = 10000
    # data = pd.read_csv("../data/spring_break_data.txt").values
    data = pd.read_csv("../data/first_dataset.txt").values
    counts, bin_edges = np.histogram(data, bins=nbins)
    p0 = [counts[0], np.mean(data), 1]
    xdata = (bin_edges[:-1] + bin_edges[1:]) / 2.
    x = np.linspace(xdata.min(), xdata.max(), N)
    popt, pcov = curve_fit(f, xdata, counts, p0=p0)
    print("Standard deviation in the parameters: ", np.sqrt(np.diag(pcov)))
    plt.style.use('seaborn')
    print("Mean of counts: {}".format( p0[1] ))
    print("Fitted value for muon lifetime: {} (ns)".format( popt[1] ))
    plt.scatter(x=xdata, y=counts, label='data', color='black')
    plt.plot(x, f(x, *popt), label='Fit', color='r')
    plt.plot(x, f(x, *popt-np.sqrt(np.diag(pcov))), label='Fit',\
            color='r',alpha=0.2,linestyle='dashed')
    plt.plot(x, f(x, *popt+np.sqrt(np.diag(pcov))), label='Fit',\
            color='r',alpha=0.2,linestyle='dashed')
    plt.fill_between( x ,\
            f(x,*popt-np.sqrt(np.diag(pcov))),f(x,*popt+np.sqrt(np.diag(pcov))),alpha=0.5)
    plt.xlabel(r"Time interval (ns)")
    plt.ylabel("Counts")
    plt.title("Single Exponential Fit")
    plt.show()
