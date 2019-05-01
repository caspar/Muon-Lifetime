

if __name__ == "__main__":
    import pandas as pd
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    times = pd.read_csv("../data/first_dataset.txt")
    print(times.describe())
    times.hist(bins=25, label='data')
    plt.ylabel("Counts")
    plt.xlabel("Time interval (ns)")
    plt.legend()
    plt.show()
