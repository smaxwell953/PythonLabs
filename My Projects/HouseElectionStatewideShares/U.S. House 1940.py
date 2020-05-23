file_handle = open('C:\\Users\\saraa\\Desktop\\1940 House.txt', 'w')

state_name_list = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

state_dict_dict = {
'Alabama':{"al_dem":25993+33433+22906+24870+31966+18881+27696+29020+39660,"al_ind":342,"al_rep":81+3428+11368,"al_writein":1},
'Arizona':{"az_dem":99424,"az_rep":40360},
'Arkansas':{"ar_dem":33127+26105+21060+28999+36067+27972+26994,"ar_rep":8566},
'California':{"ca_comm":5647+2751+1322+5232+5426+1707+5186+3826+6003+1152+4434+2732+2004+7017+1118+1355+806,"ca_dem":125845+61341+103547+135461+127167+72838+99494+73137+94435+75109+60764+84931+69874,"ca_prog":5649,"ca_proh":36406+10539,"ca_rep":71033+131584+170504+119122+148180+99708+188049+71667+75369+56808+54731+37939+32862+73932+75495+66132,"ca_scatter":284+7+16+2+11+22+133+56+394+799+44+113+74+49+368+25+55+145,"ca_writein":1828+122+37},
'Colorado':{"co_comm":272,"co_dem":110078+66662+65269+44095,"co_peace":341,"co_rep":59427+76859+70842+30126,"co_socialist":577+478},
'Connecticut':{"ct_dem":109880+63021+84439+62783+407868+90942,"ct_rep":56825+90239+51049+365851+92207+72870,"ct_scatter":10+6+29,"ct_socialist":374+4262+479+6640+610,"ct_soclabor":1383,"ct_union":851+163+208+250},
'Delaware':{"de_dem":68205,"de_libdem":2189,"de_rep":64384},
'Florida':{"fl_dem":88158+68797+36562+84594+49715,"fl_rep":8382+27815+16214},
'Georgia':{"ga_dem":28601+19443+2+22882+25609+41674+3+21966+32280+23633+25461+18291,"ga_ind":111+636+2+626+52+119+1,"ga_inddem":119,"ga_rep":36+47+21+5062+821+4025},
'Idaho':{"id_dem":62107+61726,"id_rep":37999+69804},
'Illinois':{"il_dem":34641+115698+148382+74977+35637+187393+229161+40074+49816+125827+70581+58945+31502+55451+50820+57567+36102+56744+74091+44824+63740+98162+64072+43050+67891+1968143+1913950,"il_ind":7377+7191+6786+6621,"il_rep":30698+146927+141768+21858+14540+146253+220793+11232+56806+199418+128645+90744+65698+60909+65639+79780+56712+64409+75933+41806+67896+84381+61521+49731+69165+2050493+2020006,"il_scatter":442+1+1+1+3+1+1+16},
'Indiana':{"in_dem":71606+63290+70208+58157+65200+73499+74746+87141+69227+71478+79070+80954,"in_rep":45947+87652+73914+80259+78691+80595+81632+69761+71624+80725+73867+72174},
'Iowa':{"ia_dem":46040+75774+43709+51558+58718+64314+50644+46597+67017,"ia_proh":214,"ia_rep":70120+69298+65425+66691+66940+70707+71633+64687+64877},
'Kansas':{"ks_dem":41375+62787+48971+34947+58486+44702+42518,"ks_rep":64766+73659+60381+58183+52901+69627+75349},
'Kentucky':{"ky_dem":60777+69905+96253+55561+51954+74463+44185+61881+43013,"ky_rep":64053+39447+32981+48700+33574+44736+69415},
'Louisiana':{"la_dem":58234+56026+27081+33704+33462+41173+28518+28904,"la_ind":9,"la_rep":13988},
'Maine':{"me_dem":32018+31334+23934,"me_rep":55503+57152+46732},
'Maryland':{"md_dem":36057+113495+38540+50120+58418+60037,"md_ind":4+1+1,"md_rep":30810+59223+24153+38444+23857+52258},
'Massachusetts':{"ma_dem":54634+54428+72839+60988+37593+35214+89966+71127+81523+54093+68041+97588+48606+55241+53581,"ma_proh":1130+2194+1187,"ma_rep":72750+76373+60676+70542+120435+88834+52701+57217+74922+78029+13176+27302+92651+65780+73358,"ma_scatter":3+4+1+1+2+3+4+1},
'Michigan':{"mi_comm":387+83+329+294+195,"mi_dem":87451+43733+45138+40443+56172+73629+39416+43297+39667+32289+45826+47429+66985+80463+85239+73956+68195,"mi_proh":59+161+82+105+66+72+64+47+49,"mi_rep":21399+72235+74614+65666+65240+77340+73926+68265+52343+52685+48087+44733+55115+55910+52131+51276+82809,"mi_socialist":279+224+335+82+350+352+329+306},
'Minnesota':{"mn_dem":27479+57673+28321+15050+20720+52504+21796+23845+15507,"mn_farmerlabor":20700+11534+50222+32898+52289+42356+39252+48999,"mn_ind":4488,"mn_rep":88814+66610+63854+68525+79491+84023+65958+74521+48324},
'Mississippi':{"ms_dem":19330+16939+13864+15329+24079+26879+29799},
'Missouri':{"mo_dem":62461+77922+77424+72331+63202+67902+59344+64263+60204+69859+85722+108605+82417,"mo_rep":61123+66794+67757+48181+53390+78746+86547+61567+48704+51755+68088+127005+45626,"mo_soclabor":4+12+19+3+22+77+17},
'Montana':{"mt_dem":47352+83101,"mt_rep":56616+49710,"mt_socialist":1196},
'Nebraska':{"ne_dem":51524+68760+19253+29311+63025,"ne_ind":3461+19807,"ne_rep":64431+52669+90561+66966+45548},
'Nevada':{"nv_dem":32714,"nv_rep":18032},
'New Hampshire':{"nh_dem":55434+49260,"nh_rep":57982+55530},
'New Jersey':{"nj_15pension":163,"nj_comm":67+309+158+198+337+43,"nj_dem":77931+60392+76048+54909+65200+62888+44527+50622+54254+46934+46130+53677+92356+84538,"nj_fusion":2014,"nj_ind":375+19+293+128,"nj_indlabor":205,"nj_indlincoln":240,"nj_indprog":32,"nj_libind":67,"nj_pension":2255,"nj_proh":110+35+29+29+42+864+40+45+64+18+1978+166+24+10,"nj_rep":97547+55382+70890+69834+82840+78381+82287+72197+91352+64699+61606+67996+39274+44839,"nj_roosevelt":98,"nj_socialist":257+66+211+1527+122+64,"nj_soclabor":134+40},
'New Mexico':{"nm_dem":106972,"nm_rep":75085},
'New York':{"ny_amlabor":10879+20827+3636+31945+52972+11743+5193+3664+2534+6103+4623+3874+5625+3612+9209+16529+5931+50293+35233+5742+4071+6134+3308+3254+2483+3405+2563+4508+2814+2552+4945+8572+7244+11006+10517+2370+6231+2848+5432+5639+5894+1775+367621+361720,"ny_comm":2570+5287+8711+1564+8081+5350+227,"ny_dem":141774+216309+36995+130391+217599+80816+46616+17176+18334+26455+26314+28837+45339+31151+71018+15160+108139+44296+190396+161577+64889+59739+47610+89592+43588+51270+30105+52469+41027+69730+40929+38878+37939+54723+42945+46280+32937+79966+45285+71036+57204+58356+39205+2831398+2821216,"ny_proh":5679+5212,"ny_rep":276873+170004+17839+25207+51428+58507+18765+103753+67901+21358+42631+2976+8367+13940+13158+31020+53316+24312+32821+46324+23532+88083+136835+125412+68715+65618+59344+82328+66159+58727+71782+72412+93990+97688+64507+76630+92866+73316+119972+57335+44866+67520+2830517+2812066+14737,"ny_workers":411},
'North Carolina':{"nc_dem":36722+41217+33760+57610+53778+55549+41663+57879+60875+87156+75763,"nc_ind":15259,"nc_rep":2851+11248+14926+15872+7168+28232+28287+37736+34104},
'North Dakota':{"nd_dem":63662+63027,"nd_ind":23399+20845,"nd_rep":148227+111125},
'Ohio':{"oh_dem":61382+60410+103291+47765+31063+52769+59667+44605+86956+33698+43548+87115+40274+121037+57359+92469+56343+79718+122075+72395+79602+126273+1483879+1384745,"oh_ind":2527,"oh_rep":84622+77769+93002+65534+48040+48257+83415+49218+71927+48217+37398+91767+62442+108016+40233+71629+69102+66666+75016+34605+23658+165322+1519559+1386627},
'Oklahoma':{"ok_dem":93366+50351+68344+69040+93457+52338+39884+41417+479433,"ok_ind":212+183+840+1639,"ok_proh":451+566+391+3267,"ok_rep":56112+30630+18145+28046+34942+22343+16246+48737+245384},
'Oregon':{"or_dem":63940+44832+80930,"or_ind":2642,"or_rep":145675+33529+84275,"or_scatter":4,"or_soclabor":3524+1344+1207},
'Pennsylvania':{"pa_americanway":65,"pa_comm":228+402+202+396+177+315+98+98+125+335+216,"pa_dem":64599+62844+77436+74458+76724+82550+76054+58389+50632+53333+65368+101854+68501+48140+35696+39988+45616+34328+62298+44914+52530+60848+44263+54631+58442+62273+69736+58772+21924+62450+76819+62121+70824+75004,"pa_ind":845+699,"pa_nowagetax":146+718,"pa_proglabor":2175+359,"pa_proh":70+105+229+173+183+408+1096+202+772+523+370+376+160,"pa_rep":39770+39489+44757+42578+60109+51313+79416+79601+55919+72843+58831+74305+70647+31839+54981+61167+75006+46595+74420+64188+40863+49532+600+57027+41641+37357+64669+75243+44528+50147+62097+59960+28196+57737+64336,"pa_scatter":3+1+1+5+6+2+4+8+2+8+2+2+5+6+2+2+5+2+1,"pa_socialist":194+187+241+347+383+195+411+4980,"pa_statesrights":270},
'Rhode Island':{"ri_dem":87327+87253,"ri_rep":64517+74296},
'South Carolina':{"sc_dem":16626+14920+15977+23825+14754+12074,"sc_ind":4,"sc_rep":278+206+108+657+120+123},
'South Dakota':{"sd_dem":91967+24127,"sd_rep":135406+47051},
'Tennessee':{"tn_dem":18051+31663+35332+38278+20933+24536+25590+32002+55952,"tn_ind":34565+2760+2309,"tn_rep":39577+41274+16099+4777+3459},
'Texas':{"tx_comm":76,"tx_dem":27030+43597+43139+46333+57789+33546+30385+89796+52754+48442+37227+54108+50076+59009+31800+34516+45456+51015+53510+47075+49468,"tx_rep":8273+565+4925+1894+2628+1858+9296+3832},
'Utah':{"ut_dem":62654+86874,"ut_rep":47021+50332},
'Vermont':{"vt_dem":50804,"vt_rep":89637,"vt_scatter":36},
'Virginia':{"va_comm":95,"va_dem":22493+29788+34885+19043+25631+30046+26233+33031+32412,"va_ind":1126,"va_rep":13864+13964+8794+24109,"va_scatter":20+12+15+1+10+19+4+7,"va_socialist":788+186},
'Washington':{"wa_comm":230,"wa_dem":113988+66314+60529+50493+67582+71536,"wa_rep":71110+49209+48700+48003+54258+42334},
'West Virginia':{"wv_dem":72717+77045+79441+82979+81903+105927,"wv_rep":63906+56911+60810+74491+48223+65762},
'Wisconsin':{"wi_dem":26520+18237+11806+57381+37872+30162+14495+6763+17284,"wi_prog":28308+60481+52131+52907+54501+19387+40558+49005+61009+50776,"wi_rep":69276+58121+54457+50796+73728+66821+58696+61987+47825+37819,"wi_scatter":18+3+5+41+58+1+8+3+147},
'Wyoming':{"wy_dem":57030,"wy_prog":157,"wy_rep":49701},
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
