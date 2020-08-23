import re, requests, xlrd, xlwt
from bs4 import BeautifulSoup

excel = xlrd.open_workbook('DataBase.xls')
excel.sheet_names()
table = excel.sheet_by_name('data')
worldlist = table.col_values(0)
hmrt = table.col_values(17)
rtl = dict(zip(worldlist, hmrt))
print('DataBase加载完成~')

excel = xlrd.open_workbook('CorpusCharacterlist.xls')
excel.sheet_names()
table = excel.sheet_by_name('zifreq')
worldlist = table.col_values(1)
worldrate = table.col_values(3)
zpl = dict(zip(worldlist, worldrate))
print('CorpusCharacterlist加载完成~')


ccd = {'cc1':'字表一', 'cc2':'字表二'}
ccl = []
for i, item0 in enumerate(ccd.keys()):
    response = requests.get('https://www.zdic.net/zd/zb/'+item0)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find_all('div', class_='bs_index3')
    cc = []
    for item in div:
        li = item.find_all('li')
        for item in li:
            cc.append(item.a.get_text())
    ccl.append(cc)
    print('获取字表：' + ccd[item0])

# f = xlwt.Workbook()
# sheet1 = f.add_sheet(u'list1', cell_overwrite_ok=True)
# sheet2 = f.add_sheet(u'list2', cell_overwrite_ok=True)

# for i, item in enumerate(ccl[0]):
#     response = requests.get('https://www.zdic.net/hans/'+item)
#     py = re.findall('class="z_d song">(.*?)<span class="ptr">', response.text)
#     bh = re.findall('总笔画</span>  (.*?)</p>', response.text)
#     jg = re.findall('<td class="dsk_2_1">(.*?)</td>', response.text)
#     cx = re.findall('<span class="cino">\\(1\\)</span> \\((.*?)。', response.text)
#     cx.append('无')
#     if item in rtl.keys():
#         rt = rtl[item]
#     else:
#         rt = 0
#     if item in zpl.keys():
#         zp = zpl[item]
#     else:
#         zp = 0
#     data = [item, py[0:int(len(py)/4)], bh[0], jg[3], cx[0], '字表一', rt, zp]
#     for j in range(len(data)):
#         sheet1.write(i,j,data[j])
#     print('成功保存：'+item)
# print('字表一保存成功~')

# for i, item in enumerate(ccl[1]):
#     response = requests.get('https://www.zdic.net/hans/'+item)
#     py = re.findall('class="z_d song">(.*?)<span class="ptr">', response.text)
#     bh = re.findall('总笔画</span>  (.*?)</p>', response.text)
#     jg = re.findall('<td class="dsk_2_1">(.*?)</td>', response.text)
#     cx = re.findall('<span class="cino">\\(1\\)</span> \\((.*?)。', response.text)
#     cx.append('无')
#     if item in rtl.keys():
#         rt = rtl[item]
#     else:
#         rt = 0
#     if item in zpl.keys():
#         zp = zpl[item]
#     else:
#         zp = 0
#     data = [item, py[0:int(len(py)/4)], bh[0], jg[3], cx[0], '字表二', rt, zp]
#     for j in range(len(data)):
#         sheet2.write(i,j,data[j])
#     print('成功保存：'+item)
# print('字表二保存成功~')

# f.save('HanList.xls')
# print('汉语常用字表保存成功~')

excel = xlrd.open_workbook('hans.xls')
table = excel.sheet_by_index(0)
hans = table.col_values(0)
newhans = xlwt.Workbook()
sheet = newhans.add_sheet(u'newhans', cell_overwrite_ok=True)

for i, item in enumerate(hans):
    response = requests.get('https://www.zdic.net/hans/'+item)
    py = re.findall('class="z_d song">(.*?)<span class="ptr">', response.text)
    bh = re.findall('总笔画</span>  (.*?)</p>', response.text)
    jg = re.findall('<td class="dsk_2_1">(.*?)</td>', response.text)
    cx = re.findall('<span class="cino">\\(1\\)</span> \\((.*?)。', response.text)
    cx.append('无')
    if item in ccl[0]:
        zb = '字表一'
    elif item in ccl[1]:
        zb = '字表二'
    else:
        zb = '字表三'
    if item in rtl.keys():
        rt = rtl[item]
    else:
        rt = 0
    if item in zpl.keys():
        zp = zpl[item]
    else:
        zp = 0
    data = [item, py[0:int(len(py)/4)], bh[0], jg[3], cx[0], zb, rt, zp]
    for j in range(len(data)):
        sheet.write(i,j,data[j])
    print('查询：'+item)

newhans.save('hans.xls')
print('汉字信息查询完毕~')
