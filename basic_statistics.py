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

        area = np.trapezoid(lorenz_curve, dx=1 / n)
        gini = 1 - 2 * area
        print(f"ジニ係数: {gini:.6f}")

        plot = plot_init(
            title="ローレンツ曲線", x_label="世帯累積比", y_label="所得累積比"
        )
        plot.plot(np.linspace(0, 1, n + 1), lorenz_curve, label="ローレンツ曲線")
        plot.plot([0, 1], [0, 1], color="gray", linestyle="--", label="完全平等線")
        plot.legend()
        plot.show()

    def mean(self, data):
        """
        入力データの平均値を計算します。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        mean_value = np.mean(values)
        print(f"平均値: {mean_value}")

    def variance(self, data):
        """
        入力データの分散を計算します（不偏分散）。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        var_value = np.var(values, ddof=1)
        print(f"分散（不偏分散）: {var_value}")

    def std(self, data):
        """
        入力データの標準偏差を計算します（不偏標準偏差）。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        std_value = np.std(values, ddof=1)
        print(f"標準偏差（不偏）: {std_value}")

    def cv(self, data):
        """
        入力データの変動係数（CV）を計算します。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        mean_value = np.mean(values)
        std_value = np.std(values, ddof=1)
        if mean_value != 0:
            cv_value = std_value / mean_value
            print(f"変動係数（CV）: {cv_value}")
        else:
            print("平均値が0のため変動係数は計算できません。")

    def summary(self, data):
        """
        入力データの平均、分散、標準偏差、変動係数をまとめて出力します。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        mean_value = np.mean(values)
        var_value = np.var(values, ddof=1)
        std_value = np.std(values, ddof=1)
        if mean_value != 0:
            cv_value = std_value / mean_value
            cv_str = f"{cv_value}"
        else:
            cv_str = "平均値が0のため計算不可"
        print("統計量まとめ:")
        print(f"  平均値: {mean_value}")
        print(f"  分散（不偏分散）: {var_value}")
        print(f"  標準偏差（不偏）: {std_value}")
        print(f"  変動係数（CV）: {cv_str}")


def plot_init(title: str, x_label: str, y_label: str, figsize: str = (6, 6)):
    plt.rcParams["font.family"] = ["Hiragino Sans"]  # , 'Yu Gothic', 'Meirio']
    plt.figure(figsize=figsize)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    return plt


if __name__ == "__main__":
    fire.Fire(BasicStatistics)
