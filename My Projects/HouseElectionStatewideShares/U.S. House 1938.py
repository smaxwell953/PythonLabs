file_handle = open('C:\\Users\\saraa\\Desktop\\1938 House.txt', 'w')

state_name_list = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

state_dict_dict = {
'Alabama':{"al_dem":9853+15569+10089+11115+16587+10246+17903+10266+12627,"al_ind":49,"al_rep":1488+7207+878},
'Arizona':{"az_dem":83556,"az_rep":20502},
'Arkansas':{"ar_dem":23274+18513+22141+22272+23949+17662+16145},
'California':{"ca_comm":8271+7015+817+5104+2951+2070,"ca_dem":64452+96258+73636+119236+62599+68681+84791+59993+75003+67588+83086+56513+51874+75819+65243,"ca_prog":3821+6643+3774+3384,"ca_rep":71496+118632+91868+91128+97407+44808+66402+40842+50504+84084+41194+68712+40457+31375+51483+26891+52216+42710,"ca_scatter":62+53+850+469+30+28+81+198+228+119+468+710+612+133+420+146+35+88,"ca_townsend":43320+12713+7903+16045+8870,"ca_writein":327+3536+32863},
'Colorado':{"co_dem":83517+65448+72736+43596,"co_proh":688,"co_rep":42758+60259+54007+24805,"co_socialist":913+810},
'Connecticut':{"ct_comm":176+15369,"ct_dem":64483+48290+55893+44626+39824+250013,"ct_labor":177+252+734,"ct_rep":68690+45056+55751+61660+39652+271329,"ct_scatter":3+5,"ct_socialist":24718+6333+17111+35328+99717,"ct_soclabor":6862,"ct_union":1477},
'Delaware':{"de_dem":46989,"de_indrep":816,"de_prog":105,"de_rep":60661},
'Florida':{"fl_dem":43837+24830+20174+29621+27894,"fl_rep":6705},
'Georgia':{"ga_dem":10920+5137+5987+5413+6906+4363+5622+4929+8934+9044,"ga_ind":1+1+8+3+443+94,"ga_rep":79+197+6},
'Idaho':{"id_dem":48318+47199,"id_rep":28640+54527},
'Illinois':{"il_dem":30207+129620+127597+61504+32104+154818+192750+31823+44064+102234+48876+43631+23708+41682+39779+35081+29023+45691+55956+37184+52173+66743+49537+40633+59203+1572870+1560283,"il_proh":9339+8808,"il_rep":26396+108483+100357+18962+10842+109031+162069+10440+39512+141685+94565+67326+45177+44243+47703+61012+45235+56587+59446+29907+51651+60518+42572+38889+53999+1472638+1456529,"il_scatter":1040+1161+13+1+1+38},
'Indiana':{"in_dem":56630+57860+59359+52293+60643+70128+74725+76780+70237+64176+65646+65368,"in_rep":46370+79304+61836+72567+73102+71883+78146+59254+64541+73782+61627+56319,"in_socialist":73},
'Iowa':{"ia_dem":33765+48155+30158+44601+43452+37056+37992+30632+46705,"ia_farmerlabor":395+386+520+362+251+523+996,"ia_prog":200+411,"ia_proh":137,"ia_rep":46636+47535+45541+48640+50860+53505+54922+51934+46366},
'Kansas':{"ks_dem":43374+54582+49117+32443+43990+40466+38357,"ks_rep":65945+70608+56361+55419+43480+69989+72895},
'Kentucky':{"ky_dem":35332+36170+57227+32179+28383+38139+27655+39006+21327,"ky_ind":210,"ky_rep":11153+20566+36361+22139+13095+20471+24337+27308+42901},
'Louisiana':{"la_dem":50453+47746+5236+10661+11644+12225+5313+9088,"la_ind":44},
'Maine':{"me_dem":40103+46900+29771,"me_rep":57642+55718+51485},
'Maryland':{"md_dem":38926+91231+29891+37416+46678+46200,"md_ind":957,"md_prog":1402,"md_rep":23096+44699+22909+37126+19604+44734,"md_scatter":4,"md_union":1599},
'Massachusetts':{"ma_dem":45397+41935+58600+53266+35323+27967+83618+62152+68258+43093+56939+86618+39939+43876+45867,"ma_proglabor":884,"ma_rep":64886+68106+54557+62874+104912+82434+47533+50711+70059+78052+25678+86389+63608+66054,"ma_scatter":1+1+1+1+71+2+11+1+1+2},
'Michigan':{"mi_commonweallth":37+47+29,"mi_constdem":286+116+153+110+160+146,"mi_dem":71533+32468+29832+33912+34991+54491+28259+36758+29397+22615+38707+43453+48443+62872+57401+49101+39784,"mi_rep":16752+58921+58128+49279+50473+66612+62910+52250+40849+44818+40904+40587+50123+45967+48429+39623+63769,"mi_scatter":1+1+2+1,"mi_socialist":314+226+204+220+177+70+203,"mi_soclabor":60+27+47+27+47+94},
'Minnesota':{"mn_dem":40340+53258+14073+12619+10598+10448+19330+8945+20425,"mn_farmerlabor":25060+50505+40558+45568+36023+42572+54381+44017,"mn_ind":4742,"mn_rep":74493+43919+53442+60252+67722+79900+49394+67960+40383},
'Mississippi':{"ms_dem":4384+4134+2172+3502+11540+4873+4834},
'Missouri':{"mo_dem":43607+51451+50501+71940+75810+52774+49396+56489+40686+44182+63332+78481+59202,"mo_rep":36064+37294+40801+17560+17809+52159+63758+45673+26510+30804+38866+71831+26476,"mo_socialist":51+48+13+136+47+58+252+648+111,"mo_soclabor":9+1+11+19+59+89+24},
'Montana':{"mt_dem":41319+63506,"mt_rep":49253+54632},
'Nebraska':{"ne_bypetition":6153+2244+3206,"ne_dem":45178+46927+25862+42957+57192,"ne_rep":45527+32685+78765+59794+31225},
'Nevada':{"nv_dem":27406+30156,"nv_rep":19078+15285},
'New Hampshire':{"nh_dem":84920+44681+34452,"nh_rep":100633+52174+49696},
'New Jersey':{"nj_comm":88+343+494+564+767+121,"nj_dem":58450+55344+64621+38921+54690+38667+35628+42030+43641+36273+38885+36736+89287+86128,"nj_farmerlabor":413,"nj_ind":3999+489,"nj_kenney":527,"nj_laborchoice":2627,"nj_peoples":47,"nj_progind":301,"nj_proh":262+91+111+146+252+85,"nj_rep":96518+57090+63345+62123+71661+63583+64147+61988+64903+51025+43747+48854+22459+23166,"nj_rooseveltind":222+23,"nj_socialist":450+139+1005+460+305,"nj_soclabor":239,"nj_socworkers":574+2067},
'New Mexico':{"nm_citizens":268,"nm_dem":90608,"nm_rep":64281},
'New York':{"ny_amlabor":18960+15033+67273+19020+8009+4898+8352+9734+12199+4527+3541+3103+6120+3440+6141+40931+4051+2786+2882+5460+3907+339328+329028,"ny_comm":1043+105681,"ny_dem":37216+28289+175009+31881+43881+17295+23722+24500+84629+36937+37452+38535+35456+50083+63325+39287+2363463+2352159+116733+99521+28317+45387+78530+29823+134461+60164+40407+13313+22237+26581+25817+43134+12376+34094+120474+46730+88037+40004+19784+19631+37195+20636+28292+50705+45516+2024135+2023131,"ny_freedom":492,"ny_ind":9537+414,"ny_indprog":10753+10103,"ny_indusgovt":5080+4291,"ny_rep":69939+111252+22037+2000814+1980352+184539+81534+10174+10620+23410+9930+37740+14852+23220+1865+3809+10392+7477+40421+12952+22741+36034+12177+49235+79537+94865+58565+54610+74888+58691+49240+60947+63857+67330+90078+48344+57648+80963+65489+92271+46784+36326+53261+1990061+1970249,"ny_socialist":870+2317+333+280+665+2473+561+3009+945+436+277+211+571+233+498+320+284+403+1159+469+2457+579+286+206+278+469+213+191+344+305+409+451+355+777+336+551+393+274+25214+24990,"ny_townsend":7638},
'North Carolina':{"nc_dem":12083+9955+17507+26932+25472+15730+17175+34757+43912+48590+61508,"nc_ind":5188,"nc_rep":15209+11087+5501+28187+28202+37360+34912},
'North Dakota':{"nd_dem":55125+44691,"nd_ind":8109,"nd_rep":153106+149047},
'Ohio':{"oh_dem":45536+42773+58139+33284+28109+43646+50163+33972+56306+24198+33764+62026+24749+87303+42573+60382+51305+55809+76268+54185+53180+87635+1068916+1015041,"oh_ind":4616,"oh_rep":63285+61480+73534+56399+37027+42847+68185+40772+55441+47036+31004+64409+56204+76346+38903+62176+46300+56468+69214+22775+24240+109494+1177982+1101193},
'Oklahoma':{"ok_dem":55253+38058+42616+44233+47692+33808+24986+34113+306241,"ok_ind":141,"ok_proh":272+336+209+470+1850,"ok_rep":31755+15335+7286+17506+18271+14617+7862+33438+137733},
'Oregon':{"or_dem":49666+35200+66498,"or_rep":119965+25557+69049,"or_scatter":7+1},
'Pennsylvania':{"pa_dem":63790+51028+55502+40413+54819+54880+45694+43604+53434+52034+54888+51565+61686+60514+56492+62524+57046+40324+43055+43928+66626+98715+69817+34678+36096+38908+32931+34578+63180+43276+47045+39762+55211+48025,"pa_ind":215+5+440,"pa_proh":187+485+546+1+1281+391+270+893+345+512+529,"pa_rep":81690+57392+56958+60307+79468+77354+47692+46248+51343+63877+59548+84077+84103+56589+78986+94108+31068+58571+63241+72225+53067+65542+41665+55565+61372+44604+38549+59754+44196+46856+53541+27440+51427+55055,"pa_royaloak":425+410+1101+3205+717+250+212+281+1201+532+449,"pa_socialist":8446+460,"pa_statesrights":207+107},
'Rhode Island':{"ri_dem":72484+66408,"ri_rep":87934+73394},
'South Carolina':{"sc_dem":45351+7649+7236+10028+8995+6191+5707,"sc_ind":3+26+48,"sc_rep":508+136+60+43+58+13,"sc_scatter":2+3},
'South Dakota':{"sd_dem":95353+25932,"sd_rep":111796+41335},
'Tennessee':{"tn_dem":10609+21824+25220+16819+14318+19554+18173+43976,"tn_ind":4382+1230+598+16079+1999+1749+1957+1146+709,"tn_rep":23251+32222+7708+881},
'Texas':{"tx_dem":16069+12816+14979+16523+10344+15619+16467+36989+16680+14476+14664+12972+20620+23438+18558+9195+17107+19048+16372+16703+21671,"tx_ind":37,"tx_rep":201+349+508+631+207+298+1621,"tx_scatter":8+3+5+1+11+7+2+3+2+2+2},
'Utah':{"ut_dem":102353+52927+58456,"ut_rep":81071+35790+35359},
'Vermont':{"vt_dem":38673+40483,"vt_rep":73990+71901,"vt_scatter":161+168},
'Virginia':{"va_dem":7191+15276+5560+5805+5761+11509+11398+13796+21235,"va_ind":2142,"va_rep":9083+6449+10612,"va_scatter":19+94+18+9+21+4+1+56+4},
'Washington':{"wa_dem":90768+58313+52305+38647+52782+64871,"wa_indsoc":849,"wa_rep":56293+36442+34394+37969+38858+24002},
'West Virginia':{"wv_dem":47051+53277+53722+65965+55501+67818,"wv_rep":57043+44334+43407+58749+34989+40965},
'Wisconsin':{"wi_dem":14573+11185+6887+33559+31154+25842+9727+28221+5066,"wi_ind":2568+7498+1442,"wi_prog":29478+40656+36509+30817+29874+13258+32442+29035+42880+45874,"wi_rep":45247+42154+43495+34196+47032+46082+41662+33354+32375+33854,"wi_scatter":3+3+41+3+2+3+8,"wi_union":225+794+981+800+1506},
'Wyoming':{"wy_dem":44525,"wy_rep":49975},
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