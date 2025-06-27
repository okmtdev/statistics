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
python basic.py mean -data=1,2,3,4,5

python basic.py variance -data=1,2,3,4,5

python basic.py std -data=1,2,3,4,5

python basic.py cv -data=1,2,3,4,5
```

## 統計量まとめ

```bash
python basic.py summary --data=1,2,3,4,5
```

- 平均値: 全てのデータを足して、データの個数で割ったもの
- 分散（Variance）: データが平均値からどれくらい散らばっているか
- 標準偏差（不偏）: 分散の平方根。元データと同じ単位で散らばり具合を表したもの
- 変動係数（CV）: 単位の異なるデータや平均値が大きく異なるデータ同士の散らばり具合を比較する指標
- 歪度: データの分布が左右対称であるか、どちらかに偏っているか
- 尖度: データの分布がどれくらい尖っているか、または平坦か


## Scatter

擬相関: xとzの間に相関があり、yとzの間に相関があるとき、xとyの相関が大きくなる見かけ上の相関

偏相関係数…zが，xとyの両方に相関があるとき，xからzの影響を除いた変量とyからzの影響を除いた変量の間の相関係数