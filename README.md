# Basic Statistical Calculations

A simple Python CLI tool for basic statistical analysis, including Lorenz curve visualization.

## Usage

Show help:
```bash
uv run python basic.py --help
```

## Lorenz Curve

ローレンツ曲線とは不均衡の度合いを示すのに使われる折れ線グラフのこと

To plot a Lorenz curve from a comma-separated list of numbers:
```bash
uv run python basic.py lorenz --data=1,2,3,4,5
```

経済におけるジニ係数の理想値は0.2～0.3であり、0.4を超えると警戒ライン

## 平均

```bash
uv run python basic.py mean -data=1,2,3,4,5

uv run python basic.py variance -data=1,2,3,4,5

uv run python basic.py std -data=1,2,3,4,5

uv run python basic.py cv -data=1,2,3,4,5
```

## 統計量まとめ

```bash
uv run python basic.py summary --data=1,2,3,4,5
```

- 平均値: 全てのデータを足して、データの個数で割ったもの
- 分散（Variance）: データが平均値からどれくらい散らばっているか
- 標準偏差（不偏）: 分散の平方根。元データと同じ単位で散らばり具合を表したもの
- 変動係数（CV）: 単位の異なるデータや平均値が大きく異なるデータ同士の散らばり具合を比較する指標
- 歪度: データの分布が左右対称であるか、どちらかに偏っているか
- 尖度: データの分布がどれくらい尖っているか、または平坦か


## Scatter

擬相関: xとzの間に相関があり、yとzの間に相関があるとき、xとyの相関が大きくなる見かけ上の相関

偏相関係数…zが、xとyの両方に相関があるとき、xからzの影響を除いた変量とyからzの影響を除いた変量の間の相関係数

# 時系列データ

- 自己相関: 自分自身に対する相関を調べたもので、過去の自分と現在の自分の関係性を探る。定量的に指標を自己相関係数という。統計学ではピアソンの積率相関係数という指標にあたる
- 偏自己相関: 一次の自己相関の影響を無視して二次の自己相関を検討したいというときに用いる指標
- トレンド: 
- 季節性
- 外因性
- ノイズ

- 傾向変動: 長期にわたる動きを表す変動
- 季節変動: 1年を周期として循環する変動
- 不規則変動: 傾向変動や季節変動以外の変動（予測が困難な偶然の変動）

移動平均: 時系列データに対して，３期の平均や４期の平均などが１期ごとにどのように変動するかを調べ，長期的な傾向を捉えやすくする手法

コレログラム: コレログラムとは、元データxから時間をずらしたデータyとの相関係数を表すグラフであり、横軸にラグ、縦軸に自己相関をとる。データの周期性と掴むことができる。

- ラグ：元データからどれほどデータがずれているかを表す指標
- 自己相関：ずらしたデータと元データの相関関係を表す指標

```bash
uv run python time_series_statistics.py calculate_moving_average -data=1,2,3,4,5

uv run python time_series_statistics.py calculate_moving_average --data=1,2,3,4,5,6,7 --window_size=3
```

変化率: 物価上昇率など基準となる時期の値に対して比較対象の時期の値がどれだけ増えたかを表す。比較時から基準時を引いたものを基準時で割り、100をかけた

- ラスパイレス関数:
- パーシェ指数: