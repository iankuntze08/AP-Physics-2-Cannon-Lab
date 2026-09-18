import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

def main():
    text = pd.read_csv("AP Physics 2 Cannon Lab - Sheet2.csv", skiprows=1)
    arrayx, arrayy = np.squeeze(np.hsplit(pd.DataFrame.to_numpy(text), 2))
    l = stats.linregress(arrayx, arrayy)

    font = {"family": "serif",
            "color":  "black",
            "weight": "normal",
            "size": 12
    }

    fig, ax = plt.subplots()
    ax.set_xlabel("EPE (J)", fontdict=font)
    ax.set_ylabel("KE (J)", fontdict=font)
    ax.set_title("Cannon Efficiency", fontdict=font)
    ax.text(0.4, 0.1, f"ŷ = {l.slope:.3f}x + {l.intercept:.3f}", fontdict=font)
    _y = [l.intercept, l.slope * np.max(arrayx) + l.intercept]
    _x = [np.min(arrayx), np.max(arrayx)]
    ax.plot(_x, _y, c="orange")
    ax.scatter(arrayx, arrayy)
    plt.savefig("cannon_efficency_plot.png", format="png")
    plt.show()

if __name__ == "__main__":
    main()
