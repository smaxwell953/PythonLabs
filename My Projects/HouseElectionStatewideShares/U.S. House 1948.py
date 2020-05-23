file_handle = open('C:\\Users\\saraa\\Desktop\\1948 House.txt', 'w')

state_name_list = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

state_dict_dict = {
'Alabama':{"al_dem":19778+21271+16279+17282+20549+13968+21552+19060+33781,"al_rep":3054+2994+2510+5006},
'Arizona':{"az_dem":42565+54066,"az_prog":1478,"az_proh":481+381,"az_rep":29864+30140},
'Arkansas':{"ar_dem":34676+29922+25754+29338+36440+40291+32982},
'California':{"ca_dem":68951+74318+56624+91268+78555+194985+194782+73704+72826+89581+105687+72900+61383+112534,"ca_ind":1013,"ca_indprog":30878+1949+40670+2573+27168+14582+19631+2904+27007+8232+1915+46232+2422+2017,"ca_rep":166571+116347+161743+67448+87143+141509+131933+115697+82947+68875+78534+66563+62951+44611+121198+92721+28698+204710+47411+87138,"ca_scatter":109+27+18+3+158+6+45+13+15+58+1667+47+25+91+87+205+15+16+160+4+121,"ca_writein":304+6157},
'Colorado':{"co_dem":106096+66579+65114+34695,"co_rep":57541+71868+63312+32206},
'Connecticut':{"ct_dem":127802+69339+84449+92618+58300+429348,"ct_peoples":2604+2224+1242+10329,"ct_rep":103294+64916+83310+117727+62804+433311,"ct_socialist":3116+643+6363},
'Delaware':{"de_dem":68909,"de_proh":399,"de_rep":71127,"de_socialist":100},
'Florida':{"fl_dem":66348+57595+30730+63665+46939+31933,"fl_rep":5413+14912+19501+15977},
'Georgia':{"ga_dem":42677+26815+32098+33522+54637+29446+45195+35788+29699+35479},
'Idaho':{"id_dem":46846+59006,"id_prog":2176+954,"id_rep":41404+61690,"id_socialist":93},
'Illinois':{"il_dem":98690+91648+91204+89557+114660+127918+133199+101098+91271+78533+80750+88795+58340+44050+57296+54481+42226+56688+59397+52235+69619+56893+53885+56262+101927+51028,"il_ind":4566,"il_prog":5669+5683+2834+4969,"il_rep":43034+85119+81175+82310+43610+53548+47602+54316+73301+109031+78269+98956+123978+94962+74213+76840+71220+61652+69733+59067+61452+64625+57800+57732+44728+54993,"il_writein":1+1+1},
'Indiana':{"in_dem":78898+57245+86382+66689+91861+65931+74396+89990+55333+67081+103046,"in_prog":1076,"in_proh":752+1032+1042+1139+2281+847+1349+910+851+1737+946,"in_rep":50194+71907+78935+63403+82730+66414+62855+71634+59787+76036+98451,"in_socialist":241},
'Iowa':{"ia_dem":60860+60272+56002+49894+57370+44002+44857+45796+615,"ia_prog":752+509+291,"ia_proh":443+293+362+140,"ia_rep":70959+82139+78838+53384+60103+55641+59173+56970,"ia_socialist":78},
'Kansas':{"ks_dem":44711+63431+38391+70778+41614+40553,"ks_rep":68395+68324+46935+88605+77160+55013},
'Kentucky':{"ky_dem":50270+54586+64877+45538+47518+60659+39788+52328,"ky_prog":686,"ky_proh":315,"ky_rep":31527+74168+31062+24240+39251+26007+34127+60309,"ky_writein":2821+1+4+2+2+2},
'Louisiana':{"la_dem":36748+61316+26587+32045+34362+47515+36053+33613,"la_rep":13337},
'Maine':{"me_dem":31528+24698+15888,"me_rep":52536+50552+38692},
'Maryland':{"md_dem":27034+99157+32138+38486+45902+48304,"md_prog":4172+1448+6552,"md_rep":29700+76235+13131+21084+30997+59856},
'Massachusetts':{"ma_dem":56604+81775+104601+89064+100333+72625+63275+52022+106366+125105+69050+55369,"ma_rep":75582+67267+36855+61448+139288+108179+26339+75965+82750+118741+89913+87973,"ma_scatter":3+813+13+7+10+2+6+1},
'Michigan':{"mi_dem":101954+50148+42146+31429+46972+72681+47040+37125+35805+27742+27265+32485+76947+99227+92579+97826+103390,"mi_prog":453+457+504+194,"mi_proh":422+854+1875+1073+853+1267+781+1347+887+789+580+433+297+297+266+618+620,"mi_rep":19609+65006+64637+61059+74191+73465+68903+61394+51771+49206+48633+42955+45761+74474+49286+57730+116427,"mi_scatter":1+1+1,"mi_socialist":196+84+148+132+93+141+79+68+57+49+32+39+203+244+255+261+317},
'Minnesota':{"mn_dem":50533+46894+87171+78476+65113+66601+57863+88501+47476,"mn_rep":80345+82886+72402+53574+76313+62194+63879+44306+57189,"mn_scatter":1+4+4+1},
'Mississippi':{"ms_dem":16800+13771+17369+15290+22641+29751+36663,"ms_rep":252},
'Missouri':{"mo_dem":56226+66062+74599+74752+59961+63390+52255+60081+56669+67564+78162+132920+77245,"mo_prog":93+252+2027+667,"mo_rep":41355+50372+52290+41576+47371+59959+61242+44887+35232+26760+40719+107861+32217,"mo_socialist":288,"mo_soclabor":11+13+24},
'Montana':{"mt_dem":64276+58711,"mt_rep":29937+61124,"mt_socialist":501},
'Nebraska':{"ne_dem":57031+58443+38846+37511,"ne_rep":76359+55199+71513+65549},
'Nevada':{"nv_dem":29733,"nv_rep":28972},
'New Hampshire':{"nh_dem":42371+30339+51262+43290,"nh_prog":696+816,"nh_rep":57371+55116+64794+59505},
'New Jersey':{"nj_dem":77012+38194+59810+77018+66387+61465+56095+59043+54682+58668+52644+58495+84487+76881,"nj_ind":4705+1612+3795,"nj_prog":1526+764+1957+2033+4258+3088+2409,"nj_proh":234+151+1605+345+864+266,"nj_rep":89211+62804+87538+48204+92286+83285+72873+59191+90153+52868+50920+63232+39661+45564,"nj_socialist":583+775+413,"nj_socworkers":2387},
'New Mexico':{"nm_dem":108529+105300,"nm_rep":76695+73661},
'New York':{"ny_amlabor":3720+5401+8985+7681+11994+9092+19803+22067+20340+6968+14440+29502+6991+13401+36278+15727+24903+43933+30112+18379+7109+6614+4454+4674+5354+4257+2083+2964+4883+1900+2002+1874+3427+3322+3062+2093+12732+7867+28608+18593+14682+11971+2990+4916,"ny_dem":48816+65247+62190+31211+43777+35503+48222+45155+35406+58765+76928+72808+52430+53170+52605+58941+64143+51837+57997+64752+66220+48420+43690+58833+63764+49972+51552+76337+51262+75697+81098+64283+43299+46247+45817+56979+87376+50695+61790+69939+36421+80589+67779+71045+78305,"ny_liberal":6120+4667+3374+5886+5583+598+1166+3377+6285+4020+5627+7106+10561+10831+3184+8114+13190+2765+8411+4861+10102+21247+16372+9805+15637+10358+3258+3036+1816+884+1236+1100+1364+1065+908+851+1511+1343+1490,"ny_rep":101924+144052+104476+58192+72012+55844+25773+26700+32290+41289+29061+44718+21703+45623+74581+20697+34819+14012+57061+81144+88822+79229+91649+77725+65341+98618+70715+62717+78409+65848+66695+70659+90305+67882+75842+66729+71275+58340+37856+25734+26038+45820+28814+13904+47372,"ny_socworkers":109},
'North Carolina':{"nc_dem":31850+36227+34997+57658+47575+50659+43292+46941+51586+48043+40009+52036,"nc_prog":116+278+784+1709+231+227,"nc_rep":2507+1406+9407+15866+17041+17906+7839+27924+35008+32321+21614+30456},
'North Dakota':{"nd_dem":56702,"nd_prog":1758,"nd_rep":132343+128454},
'Ohio':{"oh_dem":69240+75062+110204+45534+32076+46944+36685+85409+27913+32667+87770+38264+125346+45575+79859+53651+65475+134408+64241+72417+141018+1455972,"oh_ind":1273,"oh_rep":73952+66968+79162+57321+34950+41492+71737+43929+73394+38330+33796+95575+55408+92535+35294+71871+60234+55455+63079+22932+170085+1342388},
'Oklahoma':{"ok_dem":77949+46949+57300+53419+95248+47857+39380+42417,"ok_rep":68423+20412+11007+20716+45985+17100+10236+30687},
'Oregon':{"or_dem":32931+45904+30743+66436,"or_prog":5570+13171,"or_rep":88587+42730+99464+65606},
'Pennsylvania':{"pa_dem":70165+82863+70075+70129+77221+65535+56263+42878+36677+64289+68628+44345+40415+25484+30457+42118+21339+46586+24800+54041+54152+30454+42084+56282+51391+62061+64943+54402+63454+56233+58113+80600+74508,"pa_prog":5630+1339,"pa_proh":224,"pa_rep":48760+61165+69604+76009+50236+75007+86755+91394+62229+74726+45587+63797+68089+37261+47715+84997+38735+81704+43520+37904+46701+46451+35384+29768+56966+50005+39517+65276+53609+56932+75147+30328+33107+48536,"pa_socialist":2690},
'Rhode Island':{"ri_dem":95002+98617,"ri_rep":58402+66556},
'South Carolina':{"sc_dem":24527+27677+19181+26098+14544+21703,"sc_rep":2987+1020+421+1410+428+639,"sc_scatter":13+6},
'South Dakota':{"sd_dem":85957+18988,"sd_rep":99062+36713},
'Tennessee':{"tn_antijewish":934,"tn_dem":31743+44683+21445+27777+28951+28058+25170+26033+49371,"tn_ind":9806++547,"tn_prog":3670,"tn_rep":54439+43849+20740+11910+6056+11229+2555,"tn_scatter":1+6},
'Texas':{"tx_dem":40162+55072+36411+38211+66484+18731+27945+100721+55606+45007+40795+1558+61206+44274+59163+27402+37173+34078+48985+58585+43709+45274,"tx_prog":1060+33+158+198,"tx_rep":3978+4642+17124+7480+7262+6266+2724+14376},
'Utah':{"ut_dem":66641+92770,"ut_rep":46229+68693},
'Vermont':{"vt_dem":47767,"vt_rep":74076,"vt_scatter":125},
'Virginia':{"va_dem":24746+28071+33950+22029+23879+29589+25799+33563+33550,"va_ind":775+1168,"va_prog":1912+1125,"va_rep":5753+15800+11291+15854+16890+25420+30466,"va_scatter":2+6+2+1+4,"va_socialist":440+122+532+309,"va_writein":112},
'Washington':{"wa_dem":100030+83824+56947+51195+56343+54166,"wa_prog":4672+3753+5314,"wa_rep":92215+48413+61856+58105+67757+72988},
'West Virginia':{"wv_dem":68829+61786+68055+72378+71664+99842,"wv_rep":51381+51226+51123+64001+38446+59900},
'Wisconsin':{"wi_dem":61791+62953+30650+89391+91072+47844+37307+53487+39523,"wi_prog":5051+980+599+748+3004,"wi_rep":67387+74306+69727+63161+76782+60675+64531+70905+76903+52124,"wi_scatter":1+1+21+26+59+5+48+12,"wi_socialist":604+680+411+2326+3651+793+418+235+708+441},
'Wyoming':{"wy_dem":47246,"wy_rep":50218},
}

def party_print(party_dict, file_handle, stateName="US,"):
    party_keys = party_dict.keys()
    total = 0
    for key in party_keys:
        total += party_dict[key]
    print('state:', stateName)
    print('state:', stateName, file=file_handle)
    for key in party_keys:
        print(key,'-->', party_dict[key]*100/total)
        print(key,'-->', party_dict[key]*100/total, file=file_handle)
    print(key,'-->', total)
    print()
    print(file=file_handle)

for state in state_name_list:
    party_print(state_dict_dict[state], file_handle, state)
file_handle.close()
