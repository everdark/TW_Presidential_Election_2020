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

Tables for legislative election data are grouped by the class and/or the polling area,
resulting in 138 `.csv` tables in total:

```
legislative_第10屆區域立法委員:新北市第10選舉區.csv
legislative_第10屆區域立法委員:新北市第11選舉區.csv
legislative_第10屆區域立法委員:新北市第12選舉區.csv
legislative_第10屆區域立法委員:南投縣第1選舉區.csv
legislative_第10屆區域立法委員:嘉義縣第1選舉區.csv
legislative_第10屆區域立法委員:屏東縣第1選舉區.csv
legislative_第10屆區域立法委員:彰化縣第1選舉區.csv
legislative_第10屆區域立法委員:新北市第1選舉區.csv
legislative_第10屆區域立法委員:新竹縣第1選舉區.csv
legislative_第10屆區域立法委員:桃園市第1選舉區.csv
legislative_第10屆區域立法委員:臺中市第1選舉區.csv
legislative_第10屆區域立法委員:臺北市第1選舉區.csv
legislative_第10屆區域立法委員:臺南市第1選舉區.csv
legislative_第10屆區域立法委員:苗栗縣第1選舉區.csv
legislative_第10屆區域立法委員:雲林縣第1選舉區.csv
legislative_第10屆區域立法委員:高雄市第1選舉區.csv
legislative_第10屆區域立法委員:南投縣第2選舉區.csv
legislative_第10屆區域立法委員:嘉義縣第2選舉區.csv
legislative_第10屆區域立法委員:屏東縣第2選舉區.csv
legislative_第10屆區域立法委員:彰化縣第2選舉區.csv
legislative_第10屆區域立法委員:新北市第2選舉區.csv
legislative_第10屆區域立法委員:新竹縣第2選舉區.csv
legislative_第10屆區域立法委員:桃園市第2選舉區.csv
legislative_第10屆區域立法委員:臺中市第2選舉區.csv
legislative_第10屆區域立法委員:臺北市第2選舉區.csv
legislative_第10屆區域立法委員:臺南市第2選舉區.csv
legislative_第10屆區域立法委員:苗栗縣第2選舉區.csv
legislative_第10屆區域立法委員:雲林縣第2選舉區.csv
legislative_第10屆區域立法委員:高雄市第2選舉區.csv
legislative_第10屆區域立法委員:彰化縣第3選舉區.csv
legislative_第10屆區域立法委員:新北市第3選舉區.csv
legislative_第10屆區域立法委員:桃園市第3選舉區.csv
legislative_第10屆區域立法委員:臺中市第3選舉區.csv
legislative_第10屆區域立法委員:臺北市第3選舉區.csv
legislative_第10屆區域立法委員:臺南市第3選舉區.csv
legislative_第10屆區域立法委員:高雄市第3選舉區.csv
legislative_第10屆區域立法委員:彰化縣第4選舉區.csv
legislative_第10屆區域立法委員:新北市第4選舉區.csv
legislative_第10屆區域立法委員:桃園市第4選舉區.csv
legislative_第10屆區域立法委員:臺中市第4選舉區.csv
legislative_第10屆區域立法委員:臺北市第4選舉區.csv
legislative_第10屆區域立法委員:臺南市第4選舉區.csv
legislative_第10屆區域立法委員:高雄市第4選舉區.csv
legislative_第10屆區域立法委員:新北市第5選舉區.csv
legislative_第10屆區域立法委員:桃園市第5選舉區.csv
legislative_第10屆區域立法委員:臺中市第5選舉區.csv
legislative_第10屆區域立法委員:臺北市第5選舉區.csv
legislative_第10屆區域立法委員:臺南市第5選舉區.csv
legislative_第10屆區域立法委員:高雄市第5選舉區.csv
legislative_第10屆區域立法委員:新北市第6選舉區.csv
legislative_第10屆區域立法委員:桃園市第6選舉區.csv
legislative_第10屆區域立法委員:臺中市第6選舉區.csv
legislative_第10屆區域立法委員:臺北市第6選舉區.csv
legislative_第10屆區域立法委員:臺南市第6選舉區.csv
legislative_第10屆區域立法委員:高雄市第6選舉區.csv
legislative_第10屆區域立法委員:新北市第7選舉區.csv
legislative_第10屆區域立法委員:臺中市第7選舉區.csv
legislative_第10屆區域立法委員:臺北市第7選舉區.csv
legislative_第10屆區域立法委員:高雄市第7選舉區.csv
legislative_第10屆區域立法委員:新北市第8選舉區.csv
legislative_第10屆區域立法委員:臺中市第8選舉區.csv
legislative_第10屆區域立法委員:臺北市第8選舉區.csv
legislative_第10屆區域立法委員:高雄市第8選舉區.csv
legislative_第10屆區域立法委員:新北市第9選舉區.csv
legislative_第10屆區域立法委員:嘉義市選舉區.csv
legislative_第10屆區域立法委員:基隆市選舉區.csv
legislative_第10屆區域立法委員:宜蘭縣選舉區.csv
legislative_第10屆區域立法委員:新竹市選舉區.csv
legislative_第10屆區域立法委員:澎湖縣選舉區.csv
legislative_第10屆區域立法委員:臺東縣選舉區.csv
legislative_第10屆區域立法委員:花蓮縣選舉區.csv
legislative_第10屆區域立法委員:連江縣選舉區.csv
legislative_第10屆區域立法委員:金門縣選舉區.csv
legislative_第10屆山地原住民立法委員:南投縣.csv
legislative_第10屆山地原住民立法委員:嘉義市.csv
legislative_第10屆山地原住民立法委員:嘉義縣.csv
legislative_第10屆山地原住民立法委員:基隆市.csv
legislative_第10屆山地原住民立法委員:宜蘭縣.csv
legislative_第10屆山地原住民立法委員:屏東縣.csv
legislative_第10屆山地原住民立法委員:彰化縣.csv
legislative_第10屆山地原住民立法委員:新北市.csv
legislative_第10屆山地原住民立法委員:新竹市.csv
legislative_第10屆山地原住民立法委員:新竹縣.csv
legislative_第10屆山地原住民立法委員:桃園市.csv
legislative_第10屆山地原住民立法委員:澎湖縣.csv
legislative_第10屆山地原住民立法委員:臺中市.csv
legislative_第10屆山地原住民立法委員:臺北市.csv
legislative_第10屆山地原住民立法委員:臺南市.csv
legislative_第10屆山地原住民立法委員:臺東縣.csv
legislative_第10屆山地原住民立法委員:花蓮縣.csv
legislative_第10屆山地原住民立法委員:苗栗縣.csv
legislative_第10屆山地原住民立法委員:連江縣.csv
legislative_第10屆山地原住民立法委員:金門縣.csv
legislative_第10屆山地原住民立法委員:雲林縣.csv
legislative_第10屆山地原住民立法委員:高雄市.csv
legislative_第10屆平地原住民立法委員:南投縣.csv
legislative_第10屆平地原住民立法委員:嘉義市.csv
legislative_第10屆平地原住民立法委員:嘉義縣.csv
legislative_第10屆平地原住民立法委員:基隆市.csv
legislative_第10屆平地原住民立法委員:宜蘭縣.csv
legislative_第10屆平地原住民立法委員:屏東縣.csv
legislative_第10屆平地原住民立法委員:彰化縣.csv
legislative_第10屆平地原住民立法委員:新北市.csv
legislative_第10屆平地原住民立法委員:新竹市.csv
legislative_第10屆平地原住民立法委員:新竹縣.csv
legislative_第10屆平地原住民立法委員:桃園市.csv
legislative_第10屆平地原住民立法委員:澎湖縣.csv
legislative_第10屆平地原住民立法委員:臺中市.csv
legislative_第10屆平地原住民立法委員:臺北市.csv
legislative_第10屆平地原住民立法委員:臺南市.csv
legislative_第10屆平地原住民立法委員:臺東縣.csv
legislative_第10屆平地原住民立法委員:花蓮縣.csv
legislative_第10屆平地原住民立法委員:連江縣.csv
legislative_第10屆平地原住民立法委員:金門縣.csv
legislative_第10屆平地原住民立法委員:雲林縣.csv
legislative_第10屆平地原住民立法委員:高雄市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:南投縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:嘉義市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:嘉義縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:基隆市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:宜蘭縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:屏東縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:彰化縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:新北市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:新竹市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:新竹縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:桃園市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:澎湖縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:臺中市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:臺北市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:臺南市.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:臺東縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:花蓮縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:苗栗縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:連江縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:金門縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:雲林縣.csv
legislative_第10屆全國不分區及僑居國外國民立法委員:高雄市.csv
```

Here is a partial snapshot of results for `第10屆全國不分區及僑居國外國民立法委員`:

| By     | Region   | Village   |   Place |   (1)  合一行動聯盟 |   (2)  中華統一促進黨 |   (3)  親民黨 |   (4)  安定力量 |   (5)  台灣基進 |   (6)  時代力量 |
|:-------|:---------|:----------|--------:|--------------------:|----------------------:|--------------:|----------------:|----------------:|----------------:|
| 苗栗縣 | 苗栗市   | 中苗里    |    0320 |                   1 |                     0 |            40 |               3 |              14 |              71 |
| 苗栗縣 | 苗栗市   | 青苗里    |    0321 |                   0 |                     1 |            26 |               7 |              10 |              68 |
| 苗栗縣 | 苗栗市   | 維祥里    |    0322 |                   0 |                     3 |            28 |               1 |              13 |              79 |
| 苗栗縣 | 苗栗市   | 維祥里    |    0323 |                   1 |                     1 |            32 |               1 |               6 |              67 |
| 苗栗縣 | 苗栗市   | 維祥里    |    0324 |                   0 |                     2 |            22 |               0 |              14 |              69 |

## The Code

To reproduce the final output:

```sh
git clone git@github.com:everdark/TW_Presidential_Election_2020.git
cd TW_Presidential_Election_2020
pip install -r requirements.txt
python parse_raw.py
```

All processed `.csv` will be output under `data/processed` and the zip archives saved under `data/out`.
