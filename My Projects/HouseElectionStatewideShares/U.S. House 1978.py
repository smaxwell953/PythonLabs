file_handle = open('C:\\Users\\saraa\\Desktop\\1978 House.txt', 'w')

state_name_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

state_dict_dict = {
'Alabama':{"al_con":3285,"al_dem":40450+49341+74895+87380+68985+40771+77742,"al_libert":2250,"al_rep":71711+57924+65700+1841,"al_writein":2+1+1},
'Alaska':{"ak_dem":55176,"ak_rep":68811,"ak_writein":200},
'Arizona':{"az_dem":33178+67878+111850+48661,"az_libert":1402+19813+4407,"az_rep":81108+58697+90768,"az_socwork":1220},
'Arkansas':{"ar_dem":62140+35748,"ar_rep":65285+130086},
'California':{"ca_amindep":4452+4857+5961+5609+7163+6363+4410+6544,"ca_dem":125122+99712+105537+87764+106046+81801+109676+94824+88179+84488+92882+34472+100809+76602+75212+104550+67885+58900+41672+65695+73869+54442+117498+85075+45881+85880+97592+65214+66241+55667+74004+62540+73608+80388+80448+60463+75471+63891+76358+77540+85126+76308,"ca_peace":6097+5562+3022+5246+6887+5750+6453,"ca_rep":85690+114451+91966+70733+52603+3515+58332+70481+41138+41374+54621+116982+69306+95962+49914+65808+81296+85663+123192+129714+44519+99502+61496+44243+22205+113059+89392+11512+26511+26490+23242+79533+90554+68442+47417+106581+53298+112160+147882+107685+30319+167150},
'Colorado':{"co_dem":82742+98889+69669+65421+52914,"co_indep":2470+8933,"co_rep":49845+88072+69303+103121+91933,"co_socwork":2043},
'Connecticut':{"ct_communist":3068,"ct_dem":102749+116624+96830+59918+96738+119537,"ct_labor":1965,"ct_rep":67828+50167+66663+83990+88162+66664,"ct_scatter":22+23+26+11+13+23},
'Delaware':{"de_amindep":1014,"de_dem":64863,"de_rep":91689},
'Florida':{"fl_dem":85608+112649+113302+101867+40654+89543+123346+107037+65202+108837,"fl_rep":49715+25148+41647+106319+150694+56074+99757+66610+38081+37897},
'Georgia':{"ga_dem":36961+42234+54881+60284+52739+39451+47090+41184+47264+50122,"ga_rep":14221+17132+47078+23698+14172,"ga_scatter":1+2+1+8+4+11+38+9+1+8},
'Hawaii':{"hi_dem":84552+118272,"hi_inddem":2095,"hi_libert":4205+3988,"hi_rep":24470+15697},
'Idaho':{"id_dem":57972+60040,"id_rep":86680+80591},
'Illinois':{"il_dem":47581+80906+95701+46788+98702+44543+64716+81457+87543+89479+112365+28424+40675+39438+48756+40471+39260+44527+48426+27054+73331+74247+110298,"il_indep":2064,"il_rep":33540+11104+51098+94435+18802+87193+10273+13302+28673+88829+40044+110503+64060+118741+80856+76752+94375+85973+89770+111054+97473+86051+25858+57763,"il_writein":158+3+1+6+2+1+3+1+1+3+8+3+86+14+20+1},
'Indiana':{"in_amindep":1166+2352+1400,"in_dem":72367+82402+64336+42238+45479+66421+67469+76654+99727+73343+61504,"in_indep":9368,"in_labor":384,"in_libert":1381+231,"in_rep":17419+52842+50145+80527+94950+60630+86955+83019+52218+55999+45809,"in_socwork":128},
'Iowa':{"ia_dem":45037+65450+34880+88526+82333+87139,"ia_indep":884,"ia_rep":79940+72644+103659+48308+57377+44320,"ia_socialist":978},
'Kansas':{"ks_dem":70460+100139+62402,"ks_prohib":2353,"ks_rep":131037+76419+103265+43854+86011},
'Kentucky':{"ky_amindep":3323,"ky_dem":44090+36441+37346+32212+15714+47436+51559,"ky_indep":1312,"ky_rep":17785+62087+59743+52092+15861,"ky_socwork":428,"ky_writein":7+18+1+6},
'Louisiana':{"la_dem":65583,"la_rep":65317},
'Maine':{"me_dem":70348+70691,"me_indep":5346+8035+1923+1653+1573+1223,"me_rep":120791+87939},
'Maryland':{"md_dem":46093+98601+91189+43663+64868+126196+51996+81851,"md_indep":6626,"md_rep":80202+49886+71374+19160+14545+77807},
'Massachusetts':{"ma_communist":6193,"ma_dem":101570+119337+111353+90156+97099+145615+102160+106805+64868+133644+176704,"ma_indep":33835+26017,"ma_labor":12044,"ma_others":145+28+134+138+5+35+14+9+30+9+34+155,"ma_rep":131773+37881+39259+48685+83511+28566+102080,"ma_socwork":6794,"ma_workers":2709},
'Michigan':{"mi_amindep":1191+1460+3028+2179+1230+1889+5341+1848,"mi_dem":89646+45631+83932+38204+80622+97971+105402+103346+53450+94913+79081+82892+44771+84032+95137+93387+106303+113037+47165,"mi_rep":6878+97503+79572+95440+81794+74718+29958+51900+122363+89451+96351+68063+11749+40716+23177+26827+36913+117122,"mi_scatter":2+1+6+4+2+17+1+2+6+25+3+1+23+8+1+8+10+11},
'Minnesota':{"mn_american":2540+6555+25015,"mn_dem":83271+61173+67120+95989+91673+115880+93055+171125,"mn_rep":110090+145415+128759+69396+55412+93742+106573,"mn_writein":28+2+10+9+154},
'Mississippi':{"ms_dem":57358+57678+101605+34847,"ms_indep":2059+25134+2500+1436,"ms_rep":26734+35730+8408+68225+97177},
'Missouri':{"mo_dem":65950+102911+121565+120748+82140+76061+66351+96509+135170+99148,"mo_labor":712,"mo_rep":30995+79495+26881+45116+30360+96574+104566+63109+45795+52687,"mo_socwork":1353+1631},
'Montana':{"mt_dem":86016+57480,"mt_rep":64093+75766},
'Nebraska':{"ne_dem":71311+77135+35371,"ne_rep":99013+70309+141597},
'Nevada':{"nv_dem":132513,"nv_libert":6029,"nv_rep":44425},
'New Hampshire':{"nh_dem":82697+39546,"nh_libert":2407,"nh_rep":49131+84535},
'New Jersey':{"nj_betsyross":1145+484,"nj_dem":106096+112768+83349+69259+38108+56874+78358+69496+56888+55074+88294+34423+71808+67008+55944,"nj_indcoalition":5396,"nj_indep":827+318+19126+15015+1962,"nj_labor":243+663+290,"nj_libert":876+643+974+1238+1438,"nj_rep":26853+56997+64730+41833+100739+89446+69543+23842+73478+8066+35642+94850+77301+21355+53108,"nj_soclabor":671+737,"nj_socwork":347},
'New Mexico':{"nm_dem":70761+95710,"nm_rep":118075},
'New York':{"ny_con":14529+9531+11949+14445+10585+9503+3935+5165+10012+4082+4219+3878+1330+6626+3782+8003+1648+499+2550+10384+8588+10708+5703+2905+8946+5976+9376+6384+4972+18127+6046+3233+1501+13896+4053,"ny_dem":67180+64807+70526+46508+56497+74741+55985+74872+68971+51350+51682+55880+21406+64514+29040+42646+52855+54228+48196+49344+57452+23950+20769+54110+66354+75397+31213+39062+83413+139575+84705+80512+52455+76251+58286+60708+36428+95613+70911+67475+79385,"ny_indep":192,"ny_indneigh":3129,"ny_labor":274,"ny_liberal":2909+1686+2083+4022+6058+4073+5901+1329+2866+3117+4291+4323+2299+2551+6848+12662+5238+4630+6823+1526+4617+2763+1423+2808+7353+4193+3330+2149+1695+3884+3436+6204,"ny_rep":75586+43791+66458+54509+80266+74279+44304+13008+15165+32096+23431+16206+11987+3580+12524+7516+20508+9033+25068+57738+5757+11661+1655+8560+49071+48863+114641+87059+60474+33112+99518+90572+79502+98415+60687+82501+62081+96119+30964+17585+100032+52378,"ny_soclabor":679,"ny_socwork":560+612,"ny_taxpayer":563+372},
'North Carolina':{"nc_dem":67716+61851+54452+74249+68778+58193+53696+63168+29761+75460,"nc_libert":1214+4436+906,"nc_rep":16814+15988+22150+58161+26882+23146+43942+66157+67004+65832},
'North Dakota':{"nd_dem":68016,"nd_indep":3197,"nd_natstate":1389,"nd_rep":147712},
'Ohio':{"oh_dem":38669+64522+62849+39360+51071+46318+32493+71709+35039+37131+61698+80875+82356+37000+29640+42117+71894+69977+76973+58934+87551+99975,"oh_indep":1907+2122+3+4530+2563+4723+7125+6966,"oh_rep":73593+58716+51833+85575+85547+85592+92507+81156+34326+99329+89327+81573+43269+31311+91023+105152+87010+48931+71890+9533+30930+33732},
'Oklahoma':{"ok_dem":73886+72583+62993+17978+103512,"ok_rep":49404+59853+41421+71451+36031},
'Oregon':{"or_dem":158706+152099+151895+124745,"or_labor":27120,"or_rep":93640+67547+96953,"or_writein":32+373+445+68},
'Pennsylvania':{"pa_amindep":1206,"pa_dem":104412+132594+86015+87555+36704+106431+79771+89276+33882+35721+61433+104216+47151+68004+58077+27386+79234+88299+28577+97745+73712+99559+61657+48894+68293,"pa_indep":10588+5907,"pa_labor":1059+540+1284,"pa_libert":2837,"pa_rep":37913+25785+33750+110445+110565+37746+78403+56776+101151+116003+45335+47442+112711+49992+65986+91910+53613+65088+105424+37745+65622+39518+73194+87041+62160,"pa_socwork":2321},
'Rhode Island':{"ri_dem":86768+87397,"ri_rep":54912+78725},
'South Carolina':{"sc_dem":65621+52598+80968+45357+63013+69220,"sc_indep":1691+13207,"sc_rep":42994+71032+17924+51483},
'South Dakota':{"sd_dem":64683+55516,"sd_rep":64544+70780},
'Tennessee':{"tn_dem":50694+27745+108282+108695+68608+38954+96863+80776,"tn_indep":13535+17674+1460,"tn_rep":92143+125082+47288+114630+36003+33679,"tn_writein":4+6+21+6+38+7+2},
'Texas':{"tx_dem":73708+66986+58336+35524+66025+22415+39429+50792+94529+53354+46456+75271+63953+54560+53090+69030+36783+54729+51584+63501+53443+62649+39201,"tx_laraza":7185,"tx_rep":20700+28584+96406+36582+34672+35393+128214+24673+29473+29328+49965+21364+25275+24325+27853+22743+32302+48070+84336+54643+33314,"tx_socwork":397+1235},
'Utah':{"ut_amindep":4180+1940,"ut_dem":93892+68899,"ut_indep":894+1512+1323,"ut_rep":85028+121492},
'Vermont':{"vt_dem":23228,"vt_libunion":6505,"vt_rep":90688,"vt_scatter":81},
'Virginia':{"va_dem":34578+104550+83575+46950+56137+47637+70892,"va_indep":14453+52396,"va_rep":89158+63512+77827+88647+84517+2632+76877+61981,"va_writein":5+18+214+46+44+156+9+5+10+9},
'Washington':{"wa_dem":52706+70620+82616+85602+77201+71057+67450,"wa_indep":14887,"wa_libert":3545,"wa_rep":99942+66793+58270+54389+68761+43640+59052,"wa_socwork":2043},
'West Virginia':{"wv_dem":76372+69683+74837+70035,"wv_rep":44062+56272+51584},
'Wisconsin':{"wi_con":1287+1678,"wi_dem":77146+99631+96326+101575+85067+48785+110874+73925+75207,"wi_indep":1697+779+386,"wi_rep":64437+71412+57060+52125+30185+114742+65750+101856+118386,"wi_scatter":2+22+26+3+3+3+2+10+95},
'Wyoming':{"wy_dem":53522,"wy_rep":75855}
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
