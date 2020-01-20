# 2020 Taiwanese Presidential Election Data

## Raw Data Source

[中央選舉委員會 Central Election Commission](https://www.cec.gov.tw/pc/zh_TW/index.html)

+ [第15任總統(副總統)選舉 The 15th Taiwanese Presidential Election](https://db.cec.gov.tw/histMain.jsp?voteSel=20200101A1&fbclid=IwAR0iO6jTQqKyJLz6FjfYy3I1QsJ4JkMbh2sKiRMofaBMUYgUkMM8eTlBAZc)
+ [第10屆立法委員選舉 The 10th Taiwanese Legislative Election](https://db.cec.gov.tw/histMain.jsp?voteSel=20200101A2&fbclid=IwAR2npewc1KR14wRtmub-ag3Fj6MkAB5gZCpVvaptCBoa7yWVfyWuQ_LuJWY)

## Processed Data

The raw data is processed to be *analytically friendly*.

To directly download the processed archives:
https://github.com/everdark/TW_Presidential_Election_2020/releases/

## Visualization

[Visualization for TW General Election](https://everdark.github.io/k9/projects/tw_election_2020/tw_election_2020.nb.html)

The notebook uses the processed data to generate visual descriptions about the election results.

### Presidential Election

All column names are reserved with newline char replaced with space.
Additional columns are created for ease of grouping and slicing.

There are 4 `.csv` files representing:

1. County-Level 各縣市
2. Region-Level 各鄉鎮市區
3. Village-Level 各村里
4. Polling-Place-Level 各投開票所

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
resulting in 76 `.csv` tables in total.
There are classes of the legislative election:

1. Highland Aborigine 山地原住民立委
2. Lowland Aborigine 平地原住名立委
3. Party-List 不分區立委
4. Constituency 分區立委

Data for highland/lowland aborigine and party-list are grouped into one table per each class.
Data for constituency is divided by district since the numbers of candidates are varying.
Though one can reshape the original wide format into a long format to get a full single table for constituency,
we keep the data as raw as possible.

Here are all the files for legislative outcome:

```
legislative_constituency_changhua_1.csv
legislative_constituency_changhua_2.csv
legislative_constituency_changhua_3.csv
legislative_constituency_changhua_4.csv
legislative_constituency_chiayi_city.csv
legislative_constituency_chiayi_county_1.csv
legislative_constituency_chiayi_county_2.csv
legislative_constituency_hsinchu_city.csv
legislative_constituency_hsinchu_county_1.csv
legislative_constituency_hsinchu_county_2.csv
legislative_constituency_hualien.csv
legislative_constituency_kaohsiung_1.csv
legislative_constituency_kaohsiung_2.csv
legislative_constituency_kaohsiung_3.csv
legislative_constituency_kaohsiung_4.csv
legislative_constituency_kaohsiung_5.csv
legislative_constituency_kaohsiung_6.csv
legislative_constituency_kaohsiung_7.csv
legislative_constituency_kaohsiung_8.csv
legislative_constituency_keelung.csv
legislative_constituency_kinmen.csv
legislative_constituency_lienkiang.csv
legislative_constituency_miaoli_1.csv
legislative_constituency_miaoli_2.csv
legislative_constituency_nantou_1.csv
legislative_constituency_nantou_2.csv
legislative_constituency_new_taipei_1.csv
legislative_constituency_new_taipei_10.csv
legislative_constituency_new_taipei_11.csv
legislative_constituency_new_taipei_12.csv
legislative_constituency_new_taipei_2.csv
legislative_constituency_new_taipei_3.csv
legislative_constituency_new_taipei_4.csv
legislative_constituency_new_taipei_5.csv
legislative_constituency_new_taipei_6.csv
legislative_constituency_new_taipei_7.csv
legislative_constituency_new_taipei_8.csv
legislative_constituency_new_taipei_9.csv
legislative_constituency_penghu.csv
legislative_constituency_pingtung_1.csv
legislative_constituency_pingtung_2.csv
legislative_constituency_taichung_1.csv
legislative_constituency_taichung_2.csv
legislative_constituency_taichung_3.csv
legislative_constituency_taichung_4.csv
legislative_constituency_taichung_5.csv
legislative_constituency_taichung_6.csv
legislative_constituency_taichung_7.csv
legislative_constituency_taichung_8.csv
legislative_constituency_tainan_1.csv
legislative_constituency_tainan_2.csv
legislative_constituency_tainan_3.csv
legislative_constituency_tainan_4.csv
legislative_constituency_tainan_5.csv
legislative_constituency_tainan_6.csv
legislative_constituency_taipei_1.csv
legislative_constituency_taipei_2.csv
legislative_constituency_taipei_3.csv
legislative_constituency_taipei_4.csv
legislative_constituency_taipei_5.csv
legislative_constituency_taipei_6.csv
legislative_constituency_taipei_7.csv
legislative_constituency_taipei_8.csv
legislative_constituency_taitung.csv
legislative_constituency_taoyuan_1.csv
legislative_constituency_taoyuan_2.csv
legislative_constituency_taoyuan_3.csv
legislative_constituency_taoyuan_4.csv
legislative_constituency_taoyuan_5.csv
legislative_constituency_taoyuan_6.csv
legislative_constituency_yilan.csv
legislative_constituency_yulin_1.csv
legislative_constituency_yulin_2.csv
legislative_highland_aborigine.csv
legislative_lowland_aborigine.csv
legislative_partylist.csv
```

Here is a partial snapshot of the party-list result:

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
