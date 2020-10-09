from urllib import request

url_file_handle = open('c:\\users\\saraa\\OneDrive\\Desktop\\1.txt')
url_list = url_file_handle.readlines()
url_file_handle.close()
rep_dict = {}
dday_bytes = '<th scope="row">Died</th>'.encode(encoding='UTF-8')
dday_end_bytes = ' (aged'.encode(encoding='UTF-8')
sep_bytes = '/'.encode(encoding='UTF-8')
dday_length = len(dday_bytes)

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
        if line.count(dday_bytes):
            dday_start = line.find(dday_bytes)+dday_length
            dday_end = line.find(dday_end_bytes)
            dday = line[dday_start:dday_end]
            rep_dict[name] = dday
        line = page.readline()
    page.close()

for rep_name in rep_dict.keys():
    print(rep_name, ':', rep_dict[rep_name])
