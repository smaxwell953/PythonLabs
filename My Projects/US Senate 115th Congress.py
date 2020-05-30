from urllib import request

url_list = ['https://en.wikipedia.org/wiki/Luther_Strange',\
            'https://en.wikipedia.org/wiki/Richard_Shelby',\
            'https://en.wikipedia.org/wiki/Dan_Sullivan_(U.S._Senator)',\
            'https://en.wikipedia.org/wiki/Lisa_Murkowski',\
            'https://en.wikipedia.org/wiki/Jeff_Flake',\
            'https://en.wikipedia.org/wiki/John_McCain',\
            'https://en.wikipedia.org/wiki/Tom_Cotton',\
            'https://en.wikipedia.org/wiki/John_Boozman',\
            'https://en.wikipedia.org/wiki/Dianne_Feinstein',\
            'https://en.wikipedia.org/wiki/Kamala_Harris',\
            'https://en.wikipedia.org/wiki/Cory_Gardner',\
            'https://en.wikipedia.org/wiki/Michael_Bennet',\
            'https://en.wikipedia.org/wiki/Chris_Murphy_(Connecticut_politician)',\
            'https://en.wikipedia.org/wiki/Richard_Blumenthal',\
            'https://en.wikipedia.org/wiki/Tom_Carper',\
            'https://en.wikipedia.org/wiki/Chris_Coons',\
            'https://en.wikipedia.org/wiki/Bill_Nelson_(politician)',\
            'https://en.wikipedia.org/wiki/Marco_Rubio',\
            'https://en.wikipedia.org/wiki/David_Perdue',\
            'https://en.wikipedia.org/wiki/Johnny_Isakson',\
            'https://en.wikipedia.org/wiki/Mazie_Hirono',\
            'https://en.wikipedia.org/wiki/Brian_Schatz',\
            'https://en.wikipedia.org/wiki/Jim_Risch',\
            'https://en.wikipedia.org/wiki/Mike_Crapo',\
            'https://en.wikipedia.org/wiki/Dick_Durbin',\
            'https://en.wikipedia.org/wiki/Tammy_Duckworth',\
            'https://en.wikipedia.org/wiki/Joe_Donnelly',\
            'https://en.wikipedia.org/wiki/Todd_Young',\
            'https://en.wikipedia.org/wiki/Joni_Ernst',\
            'https://en.wikipedia.org/wiki/Chuck_Grassley',\
            'https://en.wikipedia.org/wiki/Pat_Roberts',\
            'https://en.wikipedia.org/wiki/Jerry_Moran',\
            'https://en.wikipedia.org/wiki/Mitch_McConnell',\
            'https://en.wikipedia.org/wiki/Rand_Paul',\
            'https://en.wikipedia.org/wiki/Bill_Cassidy',\
            'https://en.wikipedia.org/wiki/John_Neely_Kennedy',\
            'https://en.wikipedia.org/wiki/Angus_King',\
            'https://en.wikipedia.org/wiki/Susan_Collins',\
            'https://en.wikipedia.org/wiki/Ben_Cardin',\
            'https://en.wikipedia.org/wiki/Chris_Van_Hollen',\
            'https://en.wikipedia.org/wiki/Elizabeth_Warren',\
            'https://en.wikipedia.org/wiki/Ed_Markey',\
            'https://en.wikipedia.org/wiki/Debbie_Stabenow',\
            'https://en.wikipedia.org/wiki/Gary_Peters_(politician)',\
            'https://en.wikipedia.org/wiki/Amy_Klobuchar',\
            'https://en.wikipedia.org/wiki/Al_Franken',\
            'https://en.wikipedia.org/wiki/Roger_Wicker',\
            'https://en.wikipedia.org/wiki/Thad_Cochran',\
            'https://en.wikipedia.org/wiki/Claire_McCaskill',\
            'https://en.wikipedia.org/wiki/Roy_Blunt',\
            'https://en.wikipedia.org/wiki/Jon_Tester',\
            'https://en.wikipedia.org/wiki/Steve_Daines',\
            'https://en.wikipedia.org/wiki/Deb_Fischer',\
            'https://en.wikipedia.org/wiki/Ben_Sasse',\
            'https://en.wikipedia.org/wiki/Dean_Heller',\
            'https://en.wikipedia.org/wiki/Catherine_Cortez_Masto',\
            'https://en.wikipedia.org/wiki/Jeanne_Shaheen',\
            'https://en.wikipedia.org/wiki/Maggie_Hassan',\
            'https://en.wikipedia.org/wiki/Bob_Menendez',\
            'https://en.wikipedia.org/wiki/Cory_Booker',\
            'https://en.wikipedia.org/wiki/Martin_Heinrich',\
            'https://en.wikipedia.org/wiki/Tom_Udall',\
            'https://en.wikipedia.org/wiki/Kirsten_Gillibrand',\
            'https://en.wikipedia.org/wiki/Chuck_Schumer',\
            'https://en.wikipedia.org/wiki/Thom_Tillis',\
            'https://en.wikipedia.org/wiki/Richard_Burr',\
            'https://en.wikipedia.org/wiki/Heidi_Heitkamp',\
            'https://en.wikipedia.org/wiki/John_Hoeven',\
            'https://en.wikipedia.org/wiki/Sherrod_Brown',\
            'https://en.wikipedia.org/wiki/Rob_Portman',\
            'https://en.wikipedia.org/wiki/Jim_Inhofe',\
            'https://en.wikipedia.org/wiki/James_Lankford',\
            'https://en.wikipedia.org/wiki/Jeff_Merkley',\
            'https://en.wikipedia.org/wiki/Ron_Wyden',\
            'https://en.wikipedia.org/wiki/Bob_Casey_Jr.',\
            'https://en.wikipedia.org/wiki/Pat_Toomey',\
            'https://en.wikipedia.org/wiki/Sheldon_Whitehouse',\
            'https://en.wikipedia.org/wiki/Jack_Reed_(politician)',\
            'https://en.wikipedia.org/wiki/Lindsey_Graham',\
            'https://en.wikipedia.org/wiki/Tim_Scott',\
            'https://en.wikipedia.org/wiki/Mike_Rounds',\
            'https://en.wikipedia.org/wiki/John_Thune',\
            'https://en.wikipedia.org/wiki/Bob_Corker',\
            'https://en.wikipedia.org/wiki/Lamar_Alexander',\
            'https://en.wikipedia.org/wiki/Ted_Cruz',\
            'https://en.wikipedia.org/wiki/John_Cornyn',\
            'https://en.wikipedia.org/wiki/Orrin_Hatch',\
            'https://en.wikipedia.org/wiki/Mike_Lee_(U.S._politician)',\
            'https://en.wikipedia.org/wiki/Bernie_Sanders',\
            'https://en.wikipedia.org/wiki/Patrick_Leahy',\
            'https://en.wikipedia.org/wiki/Tim_Kaine',\
            'https://en.wikipedia.org/wiki/Mark_Warner',\
            'https://en.wikipedia.org/wiki/Maria_Cantwell',\
            'https://en.wikipedia.org/wiki/Patty_Murray',\
            'https://en.wikipedia.org/wiki/Joe_Manchin',\
            'https://en.wikipedia.org/wiki/Shelley_Moore_Capito',\
            'https://en.wikipedia.org/wiki/Tammy_Baldwin',\
            'https://en.wikipedia.org/wiki/Ron_Johnson_(U.S._politician)',\
            'https://en.wikipedia.org/wiki/John_Barrasso',\
            'https://en.wikipedia.org/wiki/Mike_Enzi']

rep_dict = {}
bday_bytes = '<span class="bday">'.encode(encoding='UTF-8')
bday_end_bytes = '</span>'.encode(encoding='UTF-8')
sep_bytes = '/'.encode(encoding='UTF-8')
bday_length = len(bday_bytes)

for url in url_list:
    name_start = url.rfind('/')+1
    name = url[name_start::]
    page = request.urlopen(url)
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
