# Basic Statistical Calculations

A simple Python CLI tool for basic statistical analysis, including Lorenz curve visualization.

## Usage

Show help:
```bash
uv run python basic_statistics.py --help
```

## Lorenz Curve

ローレンツ曲線とは不均衡の度合いを示すのに使われる折れ線グラフのこと

To plot a Lorenz curve from a comma-separated list of numbers:
```bash
uv run python basic_statistics.py lorenz --data=1,2,3,4,5
```

経済におけるジニ係数の理想値は0.2～0.3であり、0.4を超えると警戒ライン

## A

```bash
python basic_statistics.py mean 1,2,3,4,5

python basic_statistics.py variance 1,2,3,4,5

python basic_statistics.py std 1,2,3,4,5

python basic_statistics.py cv 1,2,3,4,5
```

