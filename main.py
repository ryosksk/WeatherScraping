place_codeA = [11, 11, 12, 13, 13, 14, 15, 16, 16, 16, 17, 17, 17, 18, 19, 20, 20, 21, 21, 22, 23, 24, 31, 31, 31, 31, 32, 33, 33, 33, 34, 34, 35, 35, 35, 36, 36, 36, 36, 40, 40, 41, 41, 42, 43, 43, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 46, 48, 48, 48, 48, 48, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 51, 51, 52, 52, 53, 53, 53, 53, 54, 54, 54, 55, 55, 56, 56, 57, 57, 60, 60, 61, 61, 62, 63, 63, 63, 63, 64, 65, 65, 66, 66, 67, 67, 67, 68, 68, 68, 69, 69, 69, 71, 71, 72, 72, 73, 73, 74, 74, 74, 74, 81, 81, 81, 82, 82, 83, 83, 84, 84, 84, 84, 84, 84, 85, 86, 86, 86, 86, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 88, 91, 91, 91, 91, 91, 91, 91, 91]
place_codeB = [47401, 47402, 47407, 47404, 47406, 47412, 47413, 47411, 47433, 47421, 47405, 47435, 47409, 47420, 47418, 47417, 47440, 47424, 47423, 47426, 47430, 47428, 47576, 47575, 47574, 47581, 47582, 47584, 47585, 47512, 47592, 47590, 47587, 47520, 47588, 47595, 47570, 47597, 47598, 47629, 47646, 47690, 47615, 47624, 47626, 47641, 47662, 47675, 47677, 47678, 47971, 47991, 47648, 47682, 47674, 47672, 47670, 47610, 47622, 47618, 47620, 47637, 47638, 47640, 47639, 47657, 47668, 47656, 47654, 47655, 47666, 47639, 47636, 47653, 47617, 47632, 47684, 47649, 47651, 47663, 47602, 47604, 47612, 47606, 47607, 47600, 47605, 47616, 47631, 47761, 47751, 47750, 47759, 47772, 47747, 47769, 47770, 47776, 47780, 47777, 47778, 47756, 47768, 47767, 47765, 47766, 47740, 47741, 47755, 47742, 47746, 47744, 47895, 47894, 47891, 47890, 47887, 47892, 47893, 47899, 47897, 47898, 47754, 47784, 47762, 47809, 47807, 47814, 47815, 47800, 47805, 47812, 47817, 47818, 47843, 47813, 47819, 47821, 47824, 47838, 47822, 47830, 47829, 47835, 47823, 47827, 47831, 47837, 47909, 47836, 47942, 47940, 47936, 47918, 47927, 47929, 47917, 47912, 47945]
place_name = ["稚内", "北見枝幸", "旭川", "羽幌", "留萌", "札幌", "岩見沢", "小樽", "倶知安", "寿都", "雄武", "紋別", "網走", "根室", "釧路", "帯広", "広尾", "苫小牧", "室蘭", "浦河", "函館", "江差", "むつ", "青森", "深浦", "八戸", "秋田", "盛岡", "宮古", "大船渡", "石巻", "仙台", "酒田", "新庄", "山形", "福島", "若松", "白河", "小名浜", "水戸", "つくば（館野）", "奥日光（日光）", "宇都宮", "前橋", "熊谷", "秩父", "東京", "大島", "三宅島", "八丈島", "父島", "南鳥島", "銚子", "千葉", "勝浦", "館山", "横浜", "長野", "軽井沢", "松本", "諏訪", "飯田", "甲府", "河口湖", "富士山", "三島", "網代", "静岡", "浜松", "御前崎", "石廊崎", "富士山", "名古屋", "伊良湖", "高山", "岐阜", "四日市", "上野", "津", "尾鷲", "相川", "新潟", "高田", "伏木", "富山", "輪島", "金沢", "福井", "敦賀", "彦根", "伊吹山", "舞鶴", "京都", "大阪", "豊岡", "姫路", "神戸", "洲本", "奈良", "和歌山", "潮岬", "津山", "岡山", "福山", "広島", "呉", "西郷", "松江", "浜田", "境", "鳥取", "米子", "徳島", "剣山", "高松", "多度津", "松山", "宇和島", "高知", "室戸岬", "宿毛", "清水", "萩", "山口", "下関", "飯塚", "福岡", "日田", "大分", "厳原", "平戸", "佐世保", "長崎", "雲仙岳", "福江", "佐賀", "熊本", "阿蘇山", "人吉", "牛深", "延岡", "宮崎", "都城", "油津", "阿久根", "鹿児島", "枕崎", "種子島", "名瀬", "屋久島", "沖永良部", "名護", "那覇", "石垣島", "宮古島", "久米島", "西表島", "与那国島", "南大東（南大東島）"]

# place_codeA = [40]
# place_codeB = [47629]
# place_name = ["水戸"]

import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=%s&block_no=%s&year=%s&month=%s&day=1&view=p1"

def str2float(str):
  try:
    return float(str)
  except:
    return 0.0


if __name__ == "__main__":
  for place in place_name:
    All_list = [['年月日', '陸の平均気圧(hPa)', '海の平均気圧(hPa)', '降水量(mm)', '平均気温(℃)', '平均湿度(%)', '平均風速(m/s)', '日照時間(h)', '天気概況(昼)', '天気概況(夜)']]
    print(place)
    index = place_name.index(place)
    for year in range(2010,2020):
      print(year)
      for month in range(1,13):
        r = requests.get(base_url%(place_codeA[index], place_codeB[index], year, month))
        r.encoding = r.apparent_encoding

        # 対象である表をスクレイピング。
        soup = BeautifulSoup(r.text)
        rows = soup.findAll('tr',class_='mtx') 

        rows = rows[4:]

        for row in rows:
          data = row.findAll('td')

          rowData = []
          rowData.append(str(year) + "/" + str(month) + "/" + str(data[0].string))
          rowData.append(str2float(data[1].string))
          rowData.append(str2float(data[2].string))
          rowData.append(str2float(data[3].string))
          rowData.append(str2float(data[6].string))
          rowData.append(str2float(data[9].string))
          rowData.append(str2float(data[11].string))
          rowData.append(str2float(data[16].string))
          rowData.append(data[19].string)
          rowData.append(data[20].string)

          All_list.append(rowData)

    with open(place + '.csv', 'w') as file:
      writer = csv.writer(file, lineterminator='\n')
      writer.writerows(All_list)