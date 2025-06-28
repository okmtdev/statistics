import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


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

    def covariance_and_correlation(self, x, y):
        """
        共分散と相関係数を計算します。

        Args:
            x (tuple): カンマ区切りの数値列 例: "1,2,3,4"
            y (tuple): カンマ区切りの数値列 例: "4,5,6,7"
        """
        x_str = ",".join(str(i) for i in x)
        y_str = ",".join(str(i) for i in y)
        x_values = np.array([float(i) for i in x_str.split(",") if i.strip() != ""])
        y_values = np.array([float(i) for i in y_str.split(",") if i.strip() != ""])

        if len(x_values) != len(y_values):
            print("エラー：xとyのデータ数が異なります。")
            return

        covariance = np.cov(x_values, y_values)[0, 1]
        correlation = np.corrcoef(x_values, y_values)[0, 1]

        print(f"共分散: {covariance}")
        print(f"相関係数: {correlation}")

    def scatter(self, x, y):
        """
        xとyの散布図を描画します。

        Args:
            x (tuple): カンマ区切りの数値列 例: "1,2,3,4"
            y (tuple): カンマ区切りの数値列 例: "4,5,6,7"
        """
        x_str = ",".join(str(i) for i in x)
        y_str = ",".join(str(i) for i in y)
        x_values = np.array([float(i) for i in x_str.split(",") if i.strip() != ""])
        y_values = np.array([float(i) for i in y_str.split(",") if i.strip() != ""])

        if len(x_values) != len(y_values):
            print("エラー：xとyのデータ数が異なります。")
            return

        plot = plot_init(title="散布図", x_label="x", y_label="y")
        plot.scatter(x_values, y_values)
        plot.show()

    def skewness(self, data):
        """
        入力データの歪度を計算します。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        skewness_value = skew(values, bias=False)
        print(f"歪度: {skewness_value}")

    def kurtosis(self, data):
        """
        入力データの尖度を計算します。

        Args:
            data (tuple): カンマ区切りの数値列 例: "1,2,3,4,5"
        """
        data_str = ",".join(str(x) for x in data)
        values = np.array([float(x) for x in data_str.split(",") if x.strip() != ""])
        kurtosis_value = kurtosis(values)
        print(f"尖度: {kurtosis_value}")

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
        skewness_value = skew(values, bias=False)
        kurtosis_value = kurtosis(values)
        print("統計量まとめ:")
        print(f"  平均値: {mean_value}")
        print(f"  分散（不偏分散）: {var_value}")
        print(f"  標準偏差（不偏）: {std_value}")
        print(f"  変動係数（CV）: {cv_str}")
        print(f"  歪度: {skewness_value}")
        print(f"  尖度: {kurtosis_value}")


def plot_init(title: str, x_label: str, y_label: str, figsize: str = (6, 6)):
    plt.rcParams["font.family"] = ["Hiragino Sans"]  # , 'Yu Gothic', 'Meirio']
    plt.figure(figsize=figsize)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    return plt


if __name__ == "__main__":
    data = "1,2,3,4,5"
    basic_stats = BasicStatistics()
    basic_stats.summary(data)
