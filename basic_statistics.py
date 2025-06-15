import fire
import numpy as np
import matplotlib.pyplot as plt


class BasicStatistics:
    def lorenz(self, data):
        """
        入力データからローレンツ曲線を描画します。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        values = np.sort(values)
        n = values.size
        cumvals = np.cumsum(values)
        lorenz_curve = np.insert(cumvals / cumvals[-1], 0, 0)

        area = np.trapezoid(lorenz_curve, dx=1/n)
        gini = 1 - 2 * area
        print(f"ジニ係数: {gini:.6f}")

        plot = plot_init(title="ローレンツ曲線", x_label="世帯累積比", y_label="所得累積比")
        plot.plot(np.linspace(0, 1, n+1), lorenz_curve, label="ローレンツ曲線")
        plot.plot([0,1], [0,1], color='gray', linestyle='--', label="完全平等線")
        plot.legend()
        plot.show()



def plot_init(title: str, x_label: str, y_label: str, figsize: str = (6,6)):
    plt.rcParams['font.family'] = ['Hiragino Sans']# , 'Yu Gothic', 'Meirio']
    plt.figure(figsize=figsize)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    return plt

if __name__ == "__main__":
    fire.Fire(BasicStatistics)
