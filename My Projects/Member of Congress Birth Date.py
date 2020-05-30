from urllib import request

#url_list = ['https://en.wikipedia.org/wiki/Chuck_Schumer',\
#           'https://en.wikipedia.org/wiki/Mitch_McConnell',\
#           'https://en.wikipedia.org/wiki/Paul_Ryan']

url_file_handle = open('c:\\users\\saraa\\Desktop\\1.txt')
url_list = url_file_handle.readlines()
url_file_handle.close()
print(url_list)
rep_dict = {}
bday_bytes = '<span class="bday">'.encode(encoding='UTF-8')
bday_end_bytes = '</span>'.encode(encoding='UTF-8')
sep_bytes = '/'.encode(encoding='UTF-8')
bday_length = len(bday_bytes)

for url in url_list:
    name_start = url.rfind('/')+1
    name = url[name_start::].strip()
    page = ""
    try:
        page = request.urlopen(url)
    except:
        print('This URL did not work.',url)
        continue
    line = page.readline()
    while line:
        if line.count(bday_bytes):
            bday_start = line.find(bday_bytes)+bday_length
            bday_end = line.find(bday_end_bytes)
            bday = line[bday_start:bday_end]
            rep_dict[name] = bday
        line = page.readline()
    page.close()

for rep_name in rep_dict.keys():
    print(rep_name, ':', rep_dict[rep_name])
