# 2020 Taiwanese Presidential Election Data

## Raw Data Source

[中央選舉委員會](https://www.cec.gov.tw/pc/zh_TW/index.html)

+ [第15任總統(副總統)選舉](https://db.cec.gov.tw/histMain.jsp?voteSel=20200101A1&fbclid=IwAR0iO6jTQqKyJLz6FjfYy3I1QsJ4JkMbh2sKiRMofaBMUYgUkMM8eTlBAZc)
+ [第10屆立法委員選舉](https://db.cec.gov.tw/histMain.jsp?voteSel=20200101A2&fbclid=IwAR2npewc1KR14wRtmub-ag3Fj6MkAB5gZCpVvaptCBoa7yWVfyWuQ_LuJWY)

## Processed Data

The raw data is processed to be *analytically friendly*.

To directly download the processed archives:
https://github.com/everdark/TW_Presidential_Election_2020/releases/


### Presidential Election

All column names are reserved with newline char replaced with space.
Additional columns are created for ease of grouping and slicing.

There are 4 `.csv` files representing:

1. County-Level
2. Region-Level
3. Village-Level
4. Polling-Place-Level

Here is a partial snapshot of the county-level table:

| Header1          | By    | Region   |   (1) 宋楚瑜 余湘 |   (2) 韓國瑜 張善政 |   (3) 蔡英文 賴清德 |   有效票數A A=1+2+...+N |   無效票數B |   投票數C C=A+B |
|:-----------------|:------|:---------|------------------:|--------------------:|--------------------:|------------------------:|------------:|----------------:|
| 第15任總統副總統  | 中 央 | 臺北市   |             70769 |              685830 |              875854 |                 1632453 |       21381 |         1653834 |
| 第15任總統副總統  | 中 央 | 新北市   |            112620 |              959631 |             1393936 |                 2466187 |       28041 |         2494228 |
| 第15任總統副總統  | 中 央 | 桃園市   |             63132 |              529749 |              718260 |                 1311141 |       14066 |         1325207 |
| 第15任總統副總統  | 中 央 | 臺中市   |             84800 |              646366 |              967304 |                 1698470 |       20550 |         1719020 |
| 第15任總統副總統  | 中 央 | 臺南市   |             41075 |              339702 |              786471 |                 1167248 |       12341 |         1179589 |

### Legislative Election


## The Code

To reproduce the final output:

```sh
git clone git@github.com:everdark/TW_Presidential_Election_2020.git
cd TW_Presidential_Election_2020
pip install -r requirements.txt
python parse_raw.py
```

All processed `.csv` will be output under `data/processed` and the zip archives saved under `data/out`.