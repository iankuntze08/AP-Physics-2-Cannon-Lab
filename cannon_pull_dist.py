import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

def main():
    sheet1 = pd.read_csv("AP Physics 2 Cannon Lab - Sheet1.csv", skiprows=1)
    pull_cm, pull_m, range, init_vel = np.squeeze(np.hsplit(pd.DataFrame.to_numpy(sheet1), 4))
    sheet2 = pd.read_csv("AP Physics 2 Cannon Lab - Sheet2.csv", skiprows=1)
    epe, ke = np.squeeze(np.hsplit(pd.DataFrame.to_numpy(sheet2), 2))
    efficiency = ke / epe

    arrayx = pull_cm
    arrayy = efficiency

    l = stats.linregress(arrayx, arrayy)

    font = {"family": "serif",
            "color":  "black",
            "weight": "normal",
            "size": 12
    }

    fig, ax = plt.subplots()
    ax.set_xlabel("Pull Distance (cm)", fontdict=font)
    ax.set_ylabel("Effiency (KE/EPE)", fontdict=font)
    ax.set_title("Cannon Pull Distance Consistency", fontdict=font)
    ax.text(3.1, 0.09, f"ŷ = {l.slope:.3f}x + {l.intercept:.3f}", fontdict=font)
    _y = [l.intercept, l.slope * np.max(arrayx) + l.intercept]
    _x = [np.min(arrayx), np.max(arrayx)]
    ax.plot(_x, _y, c="orange")
    ax.scatter(arrayx, arrayy)
    plt.savefig("cannon_pull_distance_plot.png", format="png")
    plt.show()

if __name__ == "__main__":
    main()
