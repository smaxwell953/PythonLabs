file_handle = open('C:\\Users\\saraa\\Desktop\\1966 House.txt', 'w')

state_name_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

state_dict_dict = {
'Alabama':{"al_dem":30474+40832+61015+51863+68486+37131+73987+65982,"al_rep":58515+49203+36953+64435+40972+25404,"al_scatter":3+5+1},
'Alaska':{"ak_dem":31867,"ak_rep":34040},
'Arizona':{"az_dem":49913+66813+43219,"az_rep":102007+45326+57145},
'Arkansas':{"ar_dem":74009+86887,"ar_rep":83938+46804},
'California':{"ca_dem":77000+131145+143177+67942+56476+40514+84644+92263+97311+70013+77605+31787+56240+108668+81733+118063+76962+76346+82592+46730+74216+94420+45141+46115+63345+103289+49785+81007+69115+72173+92875+34609+89071+127976+69873+44365+80060+83216,"ca_rep":143755+53753+69057+46337+22778+132506+46763+48727+56784+156549+113679+108070+116701+83878+61550+47329+49615+96699+50068+128896+13294+82207+93320+148190+70154+62441+93890+211404+66079+36506+53708+139328+102401+101410+189582+119274+50817+69444,"ca_scatter":888+54+17+7+1017+24+15+10+88+52+69+206+5+187+7+13+46+63+12+29+13+141+13+20+42+80+8+20+22+17+8+5+21+340+63+114},
'Colorado':{"co_dem":92688+86685+76270+84107,"co_newhispano":2263,"co_rep":72732+95123+71213+59404},
'Connecticut':{"ct_amind":8730+5731,"ct_dem":100447+90298+86029+89709+96801+79865,"ct_peopleschoice":1299,"ct_rep":71353+69402+67226+86337+67094+81907,"ct_scatter":124+181+10+105+24+6,"ct_veteran":939},
'Delaware':{"de_dem":72142,"de_rep":90961},
'Florida':{"fl_dem":55547+71565+72038+70155+50772+64498+43275+76328+51636+62195+62457,"fl_rep":22281+75875+37586+105019+80989+47226,"fl_scatter":2862+4+71+18+197+102+1+10+961+94+13},
'Georgia':{"ga_dem":53413+54487+42425+54891+36751+74175+65614+60059+61930+54141,"ga_rep":38619+26255+55249+55423+35048+35383+17926+28547,"ga_scatter":4+1+693+3+2+1+7+1},
'Hawaii':{"hi_dem":140880+140110,"hi_rep":67281+62473},
'Idaho':{"id_dem":65446+33348,"id_rep":70410+79024},
'Illinois':{"il_dem":91119+83471+83857+48673+85770+84126+82962+94631+96746+58376+105996+40502+50107+51385+39123+33274+50350+57100+71050+62343+103128+55818+95156+82513,"il_rep":34421+57629+77442+125365+66735+63374+19650+63377+64875+132650+102244+90483+158769+130442+102018+89990+104240+80293+77895+102609+80382+96453+73463+32915,"il_scatter":8+12},
'Indiana':{"in_dem":71040+71825+75321+54331+76176+63342+67135+90887+89392+54515+65624,"in_ind":1363,"in_rep":50804+97161+59731+94457+72873+124087+79864+94924+76661+94428+52096},
'Iowa':{"ia_amcon":1007+712+414+145,"ia_dem":60534+76281+48530+61074+72875+53917+44529,"ia_rep":64795+65079+79343+65259+46981+73274+64217,"ia_scatter":1+1},
'Kansas':{"ks_con":2349,"ks_dem":44569+50336+51108+39625+55933,"ks_rep":97487+85128+60107+86944+86944},
'Kentucky':{"ky_dem":57736+51311+46240+56902+21452+58182+65522,"ky_rep":24085+35770+66577+66801+65596+31266+29541,"ky_writein":143},
'Louisiana':{"la_dem":68523+90149+46533+48345+38660+86958+34655+33183,"la_rep":41209+31444+26599},
'Maine':{"me_dem":81302+85956,"me_ind":7098,"me_rep":72984+65476},
'Maryland':{"md_dem":28025+79963+56980+57572+55676+29637+61959+59568,"md_rep":69940+35476+19930+47703+72360+19584+71050},
'Massachusetts':{"ma_dem":95985+126664+137681+47377+66675+119543+102104+87879+92516+141465+80473,"ma_rep":109370+51646+140702+127744+40930+96675+47705+98372,"ma_scatter":15+10+38+1+12+2},
'Michigan':{"mi_dem":89808+62536+62984+37177+40629+41695+60408+36967+46266+41410+65875+84379+60660+77851+72987+71787+90541+48627+57907,"mi_rep":16853+65205+68912+78190+87914+85669+71166+85657+92710+85754+70820+45199+12393+52490+34619+42738+40334+102501+76884,"mi_scatter":809+3+4+3+1+1+1+7+3+6},
'Minnesota':{"mn_dem":56547+47899+64861+91271+86953+76439+49388+116969,"mn_rep":109312+93855+122775+79667+58816+80710+84914},
'Mississippi':{"ms_dem":47359+53620+71377+52138+58080,"ms_ind":14700+6805+15218+1736,"ms_rep":10622+26027+24865},
'Missouri':{"mo_dem":62143+52527+59014+54330+46674+55418+52421+61128+68472+48985,"mo_rep":35053+102985+23953+34952+29641+40185+86626+44035+55405+31263},
'Montana':{"mt_dem":67123+50308,"mt_rep":64925+76015},
'Nebraska':{"ne_dem":89363+46235+42920,"ne_rep":93628+83082+115893,"ne_scatter":6+11+6},
'Nevada':{"nv_dem":86467,"nv_rep":41383},
'New Hampshire':{"nh_dem":56740+32835,"nh_rep":72869+66179},
'New Jersey':{"nj_con":916+991+3300+2857+2702+3387+4536+2236,"nj_dem":61469+65494+81382+82271+41476+48738+51204+80725+74320+71699+64023+37790+90488+87741+81959,"nj_ind":1907,"nj_peaceequal":185+1043+726,"nj_rep":68248+72014+72043+63730+108375+106406+101253+51784+71756+36508+44803+116701+35486+36828+59706,"nj_soclabor":192+1259+480+279+2921+640,"nj_socworkers":1014},
'New Mexico':{"nm_dem":140057+126984,"nm_rep":110441+124536},
'New York':{"ny_con":12731+14820+10035+17863+16070+13726+9463+8818+1214+4479+8949+8159+13946+3578+3280+5903+10493+1695,"ny_dem":101963+49749+81959+46555+88602+93758+115310+76439+87651+43182+71889+67334+74215+63173+84540+106952+79414+84940+61216+36273+45761+95671+54303+92222+52919+45621+75915+39386+95511+45308+53581+40787+42291+39203+91174+36195+90044+93746+37129+46201+35785,"ny_indsoc":3502,"ny_liberal":4900+6048+9182+4174+20557+3954+11349+3552+3412+3683+2546,"ny_peace":3562,"ny_rep":10603+86356+56754+40181+53346+24340+80882+87230+28491+91526+107671+94331+58296+79649+81122+86677+34644+36573+16702+12200+29390+28750+13482+69492+10711+20560+12414+21735+88769+107031+74816+78258+113759+75680+88378+62559+48668+110541+104342+82137+85801,"ny_unitedforpeace":1489+2013+2358+2167,"ny_writein":432},
'North Carolina':{"nc_dem":43539+36849+33809+46673+46035+42617+40512+22465+46882+52117+72855,"nc_rep":27434+19888+60686+40729+40000+56382+80989+40741+65187},
'North Dakota':{"nd_dem":33694+46933,"nd_rep":66011+50801},
'Ohio':{"oh_dem":62580+42367+53658+37855+26503+35345+38787+83261+52258+38206+39140+36751+52646+38805+55775+59031+73657+86975+63629+81210+56803+37489+43418,"oh_rep":70366+102313+62471+66142+80906+74847+81225+78933+53777+56659+86273+70102+69862+77819+57993+87597+73132+41165+34037+20034+18205+71927+102513+61194},
'Oklahoma':{"ok_dem":46286+62324+43049+36719+96464+48755,"ok_rep":106259+53919+12697+36355+42088+51474},
'Oregon':{"or_dem":49841+94346+114687+56007,"or_rep":114361+54789+56598+94154,"or_scatter":9+7+60+20},
'Pennsylvania':{"pa_dem":90100+76372+64575+98793+86128+91538+58766+48845+48656+57615+110877+53044+51024+83967+80947+36721+55761+52714+65907+93068+80472+50017+50017+85193+92073+83687+51928,"pa_rep":46280+51079+49434+91620+59515+71508+101042+70435+81516+115765+54032+107374+134414+39024+73404+82527+109169+107677+70445+48229+44800+103808+103808+68955+50639+46957+108731},
'Rhode Island':{"ri_dem":79046+117911,"ri_rep":60093+64438},
'South Carolina':{"sc_dem":59055+27013+42874+43611+41550+43090,"sc_rep":48742+31331+26702,"sc_scatter":345},
'South Dakota':{"sd_dem":40236+41155,"sd_rep":80592+63063},
'Tennessee':{"tn_dem":23538+37720+72621+55685+50758+45083+53338+43553,"tn_ind":12819+8061+12987+872,"tn_rep":86421+87777+67705+32706+43118+17608+47489,"tn_writein":2+8+1+1},
'Texas':{"tx_con":2102+3671,"tx_const":488+849+2390+1898,"tx_dem":50072+55134+35081+51895+39977+42017+39958+38497+47604+55424+39140+27070+43820+52861+33129+33179+52169+30822+56792+41067+60497+60817+50322,"tx_rep":30588+25563+53756+3207+18343+32960+45209,"tx_scatter":1+35+2+1+3+13+17+4+4+1+17+1+4},
'Utah':{"ut_dem":50260+61001,"ut_rep":99750+96426},
'Vermont':{"vt_dem":46643,"vt_rep":89097,"vt_scatter":8},
'Virginia':{"va_dem":51016+33761+51576+45226+32312+13113+42532+37929+42571+41502,"va_ind":14827,"va_rep":25203+55342+29249+50782+49413+58105,"va_scatter":117+1+191+7907+20+7+10+21+4},
'Washington':{"wa_con":2991+9585,"wa_dem":29686+75357+78601+38029+74571+73164+104613,"wa_peace":1105+1974,"wa_rep":120747+44727+40946+77929+57310+48041+60065},
'West Virginia':{"wv_dem":36242+51235+60073+71751+42722,"wv_rep":88364+33676+37416+48396+24470},
'Wisconsin':{"wi_dem":62398+70311+32849+77690+52332+61761+40093+47926+47674+39863,"wi_ind":235,"wi_rep":65041+50850+72586+26863+22167+67941+74942+75817+85297+79282,"wi_scatter":1+1+1+3+4+4+1+6+2},
'Wyoming':{"wy_dem":56442,"wy_rep":62984},}

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