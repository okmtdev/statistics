import numpy as np
import matplotlib.pyplot as plt
import fire


class TimeSeries:
    def _parse_data(self, data):
        """カンマ区切りの文字列をnumpy配列に変換する"""
        if isinstance(data, str):
            return np.array([float(x) for x in data.split(",")])
        return np.array(data)

    def moving_average(self, data, window_size=5):
        """
        時系列データの移動平均を計算する
        使用法: python time_series_statistics.py moving_average --data='1,2,3,4,5,6,7' --window_size=3
        """
        parsed_data = self._parse_data(data)
        moving_average = np.convolve(
            parsed_data, np.ones(window_size) / window_size, mode="valid"
        )
        return moving_average

    def graph(
        self, data, title="Time Series", x_label="Time", y_label="Value"
    ):
        """
        時系列データを線グラフで可視化する
        使用法: python time_series_statistics.py graph --data='1,5,2,6,3,7,4'
        """
        parsed_data = self._parse_data(data)
        plot = plot_init(title, x_label, y_label)
        plot.plot(parsed_data)
        plot.show(block=True)

    def correlogram(
        self, data, title="Correlogram", x_label="Lag", y_label="Autocorrelation"
    ):
        """
        コレログラムの棒グラフを準備する
        使用法: python time_series_statistics.py correlogram --data='1,2,1,2,1,2,1,2'
        """
        parsed_data = self._parse_data(data)
        plot = plot_init(title, x_label, y_label)
        # データ長が短い場合にエラーにならないようにmaxlagsを調整
        maxlags = len(parsed_data) - 1 if len(parsed_data) > 1 else 0
        plot.acorr(parsed_data, maxlags=maxlags)
        plot.show(block=True)


def plot_init(title: str, x_label: str, y_label: str, figsize: str = (6, 6)):
    plt.rcParams["font.family"] = ["Hiragino Sans"]  # , 'Yu Gothic', 'Meirio']
    plt.figure(figsize=figsize)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    return plt


if __name__ == "__main__":
    fire.Fire(TimeSeries)
