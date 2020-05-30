from urllib import request

#url_list = ['https://en.wikipedia.org/wiki/Chuck_Schumer',\
#           'https://en.wikipedia.org/wiki/Mitch_McConnell',\
#           'https://en.wikipedia.org/wiki/Paul_Ryan']

url_file_handle = open('c:\\users\\saraa\\Desktop\\1.txt')
url_list = url_file_handle.readlines()
url_file_handle.close()
print(url_list)
rep_dict = {}
demo_bytes = 'The median income for a household'.encode(encoding='UTF-8')
demo_end_bytes = 'older were living below the poverty line.'.encode(encoding='UTF-8')
sep_bytes = '/'.encode(encoding='UTF-8')
demo_length = len(demo_bytes)

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
        if line.count(demo_bytes):
            demo_start = line.find(demo_bytes)+demo_length
            demo_end = line.find(demo_end_bytes)
            demo = line[demo_start:demo_end]
            rep_dict[name] = demo
        line = page.readline()
    page.close()

for rep_name in rep_dict.keys():
    print(rep_name, ':', rep_dict[rep_name])
