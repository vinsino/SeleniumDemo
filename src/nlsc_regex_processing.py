import re

data = [
['汐止區', 
'基本資訊土地資訊地段資訊;建號列表公有土地行政區:新北市汐止區橋東里經緯度WGS84:121.666926,25.075045;(度)經緯度:121-40-00.9;25-04-30.1;(度分秒)國土利用現\
況調查:興建中;(2021年11月);TWD97坐標;E:317279.540;N:2774255.679汐止所;(FD1038)保安段;1-0地號;土地資訊;面積;2747.5;平方公尺;使用分區;使用地類別;登記日期;民國111年01月\
03日;公告土地現值;78810;元/平方公尺;權利人類別;本國人:98.81%本國私法人:1.19%;本查詢資料有時間落差，實際應以地政事務所地籍資料庫記載為準。;縣市;新北市;地政事務所;汐止\
;地段名稱;保安段;段代碼;1038;段延伸碼;無;鄉鎮市區代碼;28;地段原始資訊;測量方法;數值法;測量類別;地籍圖重測;成圖年月;2011-11;坐標系統;TWD97二度TM坐標;比例尺;500;數化年\
月;-;建號筆數：148;01485-000;01486-000;01487-000;01488-000;01489-000;01490-000;01491-000;01492-000;01493-000;01494-000;01495-000;01496-000;01497-000;01498-000;01499-000;01500-000;01501-000;01502-000;01503-000;01504-000;01505-000;01506-000;01507-000;01508-000;01509-000;01510-000;01511-000;01512-000;01513-000;01514-000;01515-000;01516-000;01517-000;01518-000;01519-000;01520-000;01521-000;01522-000;01523-000;01524-000;01525-000;01526-000;01527-000;01528-000;01529-000;01530-000;01531-000;01532-000;01533-000;01534-000;01535-000;01536-000;01537-000;01538-000;01539-000;01540-000;01541-000;01542-000;01543-000;01544-000;01545-000;01546-000;01547-000;01548-000;01549-000;01550-000;01551-000;01552-000;01553-000;01554-000;01555-000;01556-000;01557-000;01558-000;01559-000;01560-000;01561-000;01562-000;01563-000;01564-000;01565-000;01566-000;01567-000;01568-000;01569-000;01570-000;01571-000;01572-000;01573-000;01574-000;01575-000;01576-000;01577-000;01578-000;01579-000;01580-000;01581-000;01582-000;01583-000;01584-000;01585-000;01586-000;01587-000;01588-000;01589-000;01590-000;01591-000;01592-000;01593-000;01594-000;01595-000;01596-000;01597-000;01598-000;01599-000;01600-000;01601-000;01602-000;01603-000;01604-000;01605-000;01606-000;01607-000;01608-000;01609-000;01610-000;01611-000;01612-000;01613-000;01614-000;01615-000;01616-000;01617-000;01618-000;01619-000;01620-000;01621-000;01622-000;01623-000;01624-000;01625-000;01626-000;01627-000;01628-000;01629-000;01630-000;01631-000;01632-000;'], 
['汐止區',
 '基本資訊土地資訊地段資訊;建號列表公有土地行政區:新北市汐止區崇德里經緯度WGS84:121.672165,25.070491;(度)經緯度:121-40-19.7;25-04-13.7;(\
度分秒)國土利用現況調查:闊葉林;(2021年11月);TWD97坐標;E:317810.574;N:2773753.860汐止所;(FD1038)保安段;100-0地號;土地資訊;面積;2412.86;平方公尺;使用分區;使用地類別;登\
記日期;民國100年11月05日;公告土地現值;5500;元/平方公尺;權利人類別;本國人:100.00%;本查詢資料有時間落差，實際應以地政事務所地籍資料庫記載為準。;縣市;新北市;地政事務所;汐止;地段名稱;保安段;段代碼;1038;段延伸碼;無;鄉鎮市區代碼;28;地段原始資訊;測量方法;數值法;測量類別;地籍圖重測;成圖年月;2011-11;坐標系統;TWD97二度TM坐標;比例尺;500;數\
化年月;-;'], 
['汐止區',
 '基本資訊土地資訊地段資訊;建號列表公有土地行政區:新北市汐止區保安里經緯度WGS84:121.680510,25.070984;(度)經緯度:121-40-49.8;25-04-15.5;(度分秒\
)國土利用現況調查:倉儲;(2021年11月);TWD97坐標;E:318652.200;N:2773812.680汐止所;(FD1038)保安段;1000-0地號;土地資訊;面積;0.2;平方公尺;使用分區;使用地類別;登記日期;民國\
100年11月05日;公告土地現值;66000;元/平方公尺;權利人類別;本國人:100.00%;本查詢資料有時間落差，實際應以地政事務所地籍資料庫記載為準。;縣市;新北市;地政事務所;汐止;地段\
名稱;保安段;段代碼;1038;段延伸碼;無;鄉鎮市區代碼;28;地段原始資訊;測量方法;數值法;測量類別;地籍圖重測;成圖年月;2011-11;坐標系統;TWD97二度TM坐標;比例尺;500;數化年月;-;'],
['鹿野鄉',
 '基本資訊土地資訊地段資訊;建號列表公有土地行政區:臺東縣延平鄉鸞山村經緯度WGS84:121.142859,22.888436;(度)經緯度:121-08-34.2;22-53-18.3;(度分秒)國土利用\
現況調查:河川;(2022年6月);TWD97坐標;E:264656.821;N:2531936.509關山所;(VC0429)和平段;268-0地號;土地資訊;面積;1265.31;平方公尺;使用分區;河川區;使用地類別;水利用地;登記\
日期;民國110年11月26日;公告土地現值;270;元/平方公尺;權利人類別;國有:100.00%;本查詢資料有時間落差，實際應以地政事務所地籍資料庫記載為準。;縣市;臺東縣;地政事務所;關山;地段名稱;和平段;段代碼;0429;段延伸碼;無;鄉鎮市區代碼;09;地段原始資訊;測量方法;數值法;測量類別;地籍圖重測;成圖年月;2008-10;坐標系統;TWD97二度TM坐標;比例尺;500;數化年\
月;-;登記日期;(空白);登記原因;(空白);地目;(空白);公告現值;270;元/平方公尺;公告地價;42;元/平方公尺;公有土地所有權人資料;登記日期;登記原因;(空白);所有權人;中華民國;統\
一編號;0000000158;所有權人類別;國有;權利範圍類別;全部;權利範圍持分分母;1;權利範圍持分分子;1;申報地價;42;元/平方公尺;管理者名稱;經濟部水利署第八河川局;'],
['信義區',
'基本資訊土地資訊地段資訊;建號列表公有土地行政區:臺北市信義區景聯里經緯度WGS84:121.561166,25.029565;(度)經緯度:121-33-40.1;25-01-46.4;(度分秒)國土利用現況調查:純住宅\
;(2021年6月);TWD97坐標;E:306631.117;N:2769169.579松山所;(AD0624)三興段一小段;289-0地號;土地資訊;面積;138;平方公尺;使用分區;使用地類別;登記日期;民國068年11月22日;公告\
土地現值;337000;元/平方公尺;權利人類別;本國人:100.00%;本查詢資料有時間落差，實際應以地政事務所地籍資料庫記載為準。;縣市;臺北市;地政事務所;松山;地段名稱;三興段一小段;段代碼;0624;段延伸碼;無;鄉鎮市區代碼;17;地段原始資訊;測量方法;圖解法;測量類別;地籍圖重測;成圖年月;1979-6;坐標系統;TWD97二度TM坐標;比例尺;500;數化年月;1994-09;建號筆\
數：1;00032-000;'],
['信義區',
'基本資訊土地資訊地段資訊;建號列表公有土地行政區:臺北市信義區景聯里經緯度WGS84:121.560784,25.029828;(度)經緯度:121-33-38.8;25-01-47.3;(度分秒)國土利用現況調查:一般道路;(2021年6月);TWD97坐標;E:306592.445;N:2769198.551松山所;(AD0624)三興段一小段;290-0地號;土地資訊;面積;770;平方公尺;使用分區;使用地類\
別;登記日期;民國076年01月14日;公告土地現值;337000;元/平方公尺;權利人類別;本國人:4.79%國有:82.55%省市:12.66%;本查詢資料有時間落差，實際應以地政事務所地籍資料庫記載為\
準。;縣市;臺北市;地政事務所;松山;地段名稱;三興段一小段;段代碼;0624;段延伸碼;無;鄉鎮市區代碼;17;地段原始資訊;測量方法;圖解法;測量類別;地籍圖重測;成圖年月;1979-6;坐標\
系統;TWD97二度TM坐標;比例尺;500;數化年月;1994-09;登記日期;(空白);登記原因;(空白);地目;(空白);公告現值;337000;元/平方公尺;公告地價;86000;元/平方公尺;公有土地所有權人\
資料;登記日期;登記原因;(空白);所有權人;中華民國;統一編號;0000000158;所有權人類別;國有;權利範圍類別;權利範圍持分分母;1169;權利範圍持分分子;965;申報地價;86000;元/平方\
公尺;管理者名稱;財政部國有財產署;登記日期;登記原因;(空白);所有權人;臺北市;統一編號;0006300000;所有權人類別;直轄市有;權利範圍類別;權利範圍持分分母;1169;權利範圍持分分\
子;148;申報地價;86000;元/平方公尺;管理者名稱;臺北市政府工務局新建工程處;']
]

def regex_process(mat):
    processd_mat = []
    for arr in mat:
        processd_arr = []        
        processd_arr.append(arr[0])
        processd_arr.append(find_village(arr[1]))
        processd_arr.append(find_data(arr[1], '地段名稱'))
        processd_arr.append(find_data(arr[1], '使用分區', ';使用地類別'))
        processd_arr.append(find_data(arr[1], '使用地類別', ';登記日期'))
        processd_arr.append(find_data(arr[1], '面積'))
        processd_arr.append(find_data(arr[1], '公告土地現值'))
        processd_arr.append(find_data(arr[1], '權利人類別'))
        processd_arr.append(find_building_code(arr[1]))
        processd_arr.append(find_data(arr[1], '管理者名稱'))   
        processd_mat.append(processd_arr)
    return processd_mat
        


def find_data(str, keyword, stop=';'):
    # Use regular expression to find the value after the keyword
    # pattern = re.compile(fr'{keyword}\s*:\s*([\d.]+)')
    pattern = re.compile(fr'{keyword}\s*;\s*([\u4E00-\u9FFF\d.%:]+){stop}')
    match = pattern.search(str)

    if match:
        value = match.group(1)
        return value
        # print(f"The value after '{keyword}' is: {value}")
    else:
        return ''
        print(f"'{keyword}' not found in the string.")

def find_village(str):    
    pattern = re.compile(r'[區鎮鄉]([\u4E00-\u9FFF]+)經緯度WGS84')
    match = pattern.search(str)

    if match:
        value = match.group(1)
        return value
        # print(f"The village is: {value}")
    else:
        return ''
        # print(f"village not found in the string.")

def find_building_code(str):    
    pattern = re.compile(r'建號筆數：\d+;([\d;-]+)$')
    match = pattern.search(str)

    if match:
        value = match.group(1)
        return value
        # print(f"The building code is: {value}")
    else:
        return ''
        # print(f"building code not found in the string.")


# Example usage:
if __name__ == "__main__":
    
    for arr in data:
        print(arr[1])
        find_data(arr[1], '公告土地現值')
        find_data(arr[1], '權利人類別')
        find_data(arr[1], '地段名稱')
        find_data(arr[1], '使用分區', ';使用地類別') # optional
        find_data(arr[1], '使用地類別', ';登記日期') # optional
        find_data(arr[1], '面積') 
        find_data(arr[1], '管理者名稱')
        find_village(arr[1]) 
        find_building_code(arr[1])