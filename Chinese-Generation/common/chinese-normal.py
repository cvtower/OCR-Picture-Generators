#coding:utf-8
import Image, ImageDraw, ImageFont
import random
import os
import codecs

index = 0
fonts = 0

fontDir = "/alter/fonts"
font_dir = os.walk(fontDir)

for root, dirs, files in font_dir:
    for f in files:
        fonts = fonts + 1

print fonts


letters = ['亍','兀','丐','廿','卅','丕','亘','丞','鬲','孬','噩','禺','匕','乇','夭','爻','卮','氐','囟','胤','馗','毓','睾','亟','鼐','乜','乩','亓','芈','孛','啬','嘏','仄','厍','厝','厥','厮','靥','赝','叵','匮','匾','赜','卦','刈','刎','刭','刳','刿','剀','剌','剡','剜','剽','劂','劁','劐','劓','罔','仃','仉','仂','仨','仡','仞','伛','仳','伢','佤','仵','伥','伧','伉','伫','佞','佧','攸','佚','佝','佟','佗','伲','伽','佶','佴','侑','侉','侃','侏','佾','佻','侪','佼','侬','侔','俦','俨','俪','俅','俚','俣','俜','俑','俟','俸','倩','偌','俳','倬','倏','倮','倭','俾','倜','倌','倥','倨','偾','偃','偕','偈','偎','偬','偻','傥','傧','傩','傺','僖','儆','僭','僬','僦','僮','儇','儋','仝','氽','佘','佥','俎','龠','汆','籴','兮','巽','黉','馘','夔','匍','訇','匐','凫','夙','兕','兖','亳','衮','袤','亵','脔','禀','嬴','蠃','羸','冽','冼','凇','冢','冥','讦','讧','讪','讴','讵','讷','诂','诃','诋','诏','诎','诒','诓','诔','诖','诘','诙','诜','诟','诠','诤','诨','诩','诮','诰','诳','诶','诹','诼','诿','谀','谂','谄','谇','谌','谏','谑','谒','谔','谕','谖','谙','谛','谘','谝','谟','谠','谡','谥','谧','谪','谮','谯','谲','谳','谵','谶','阢','阡','阱','阪','阽','阼','陂','陉','陔','陟','陧','陬','陲','陴','隈','隍','隗','隰','邗','邛','邝','邙','邬','邡','邴','邳','邶','邺','邸','邰','郏','郅','邾','郐','郄','郇','郓','郦','郢','郜','郗','郛','郫','郯','郾','鄄','鄞','鄣','鄱','鄯','鄹','酆','刍','奂','劢','劬','劭','劾','哿','勐','勖','勰','叟','燮','矍','凼','鬯','弁','畚','巯','坌','垩','垡','塾','壅','壑','圩','圬','圪','圳','圹','圮','圯','坜','圻','坂','坩','垅','坫','垆','坼','坻','坨','坶','坳','垭','垤','垌','垲','垧','垓','垠','埕','埘','埚','埙','埒','垸','埴','埯','埸','埤','埝','堋','埭','堀','堞','堙','塄','堠','塥','塬','墁','墚','墀','馨','鼙','懿','艽','艿','芏','芊','芨','芄','芎','芑','芗','芙','芫','芸','芾','芰','苈','苊','苣','芘','芷','芮','苋','苌','苁','芩','芴','芡','芪','芟','苄','苎','苡','茉','苷','苤','茏','茇','苜','苴','苒','苘','茌','苻','苓','茑','茚','茆','茔','茕','苠','苕','茜','荑','荛','荜','茈','莒','茼','茴','茱','莛','荞','茯','荏','荇','荃','荟','荀','茗','荠','茭','茺','茳','荦','荥','荨','茛','荩','荬','荪','荭','荮','莰','荸','莳','莴','莠','莪','莓','莜','莅','荼','莶','莩','荽','莸','荻','莘','莞','莨','莺','莼','菁','萁','菥','菘','堇','萘','萋','菝','菽','菖','萜','萸','萑','萆','菔','菟','萏','萃','菸','菪','菅','菀','萦','菰','菡','葜','葑','葚','葙','葳','蒈','葺','蒉','葸','萼','葆','葩','葶','蒌','蒎','萱','葭','蓁','蓍','蓐','蓦','蒽','蓓','蓊','蒿','蒺','蓠','蒡','蒹','蒴','蒗','蓥','蓣','蔌','甍','蔸','蓰','蔹','蔟','蔺','蕖','蔻','蓿','蓼','蕙','蕈','蕨','蕤','蕞','蕺','瞢','蕃','蕲','薨','薇','薏','薜','薅','薹','薰','藓','藁','藜','藿','蘅','蘩','蘼','弈','夼','奁','耷','奕','奚','奘','匏','尢','尥','尬','尴','扪','抟','抻','拊','拚','拗','拮','挢','拶','挹','捋','捃','掭','揶','捱','捺','掎','掴','捭','掬','掊','捩','掮','掼','揲','揸','揠','揿','揄','揞','揎','摒','揆','掾','摅','摁','搋','搛','搠','搌','搦','搡','摞','撄','摭','撖','摺','撷','撸','撙','撺','擀','擗','擤','擢','攉','攥','弋','忒','甙','弑','卟','叱','叽','叩','叨','叻','吒','吖','吆','呋','呒','呓','呔','呖','呃','吡','呗','呙','吣','吲','咂','咔','呷','呱','呤','咚','咛','咄','呶','呦','咝','哐','咭','哂','咴','哒','咧','咦','哓','哔','呲','咣','哕','咻','咿','哙','哚','哜','咩','咪','咤','哝','哏','哞','唛','哧','唠','哽','唔','哳','唢','唣','唏','唑','唧','啧','喏','喵','啉','啭','啁','啕','唿','啐','唷','啖','啵','啶','啷','唳','唰','啜','喋','嗒','喃','喱','喹','喈','喁','喟','啾','嗖','喑','啻','嗟','喽','喔','喙','嗷','嗉','嘟','嗑','嗫','嗬','嗔','嗦','嗝','嗄','嗯','嗥','嗲','嗳','嗌','嗨','嗵','嗤','嘞','嘈','嘌','嘁','嘤','嘀','嘧','嘭','噘','嘹','噗','嘬','噍','噢','噙','噜','噌','噔','噤','噱','噫','噻','噼','嚅','嚓','嚯','囔','囗','囝','囡','囵','囫','囹','囿','圄','圊','圉','圜','帏','帙','帑','帱','帻','帼','帷','幄','幔','幛','幡','岌','屺','岐','岖','岘','岑','岚','岜','岵','岢','岬','岫','岱','岣','峁','峤','峋','峥','崂','崃','崧','崮','崤','崆','崛','嵘','崾','崴','崽','嵬','嵛','嵯','嵝','嵋','嵩','嶂','嶙','豳','嶷','巅','彳','彷','徂','徇','徉','後','徕','徙','徜','徨','徭','徵','徼','衢','犰','犴','犷','犸','狃','狁','狎','狍','狒','狨','狯','狩','狲','狷','猁','狳','猗','猓','猡','猝','猕','猢','猹','猥','猬','猱','獐','獗','獠','獾','舛','夥','飧','饧','饨','饪','饫','饬','饴','饷','饽','馀','馄','馇','馊','馍','馐','馑','馔','馕','庀','庑','庖','庥','庠','庵','庾','庳','赓','廒','廑','廛','廪','膺','忉','忖','忏','怃','怄','忡','忤','忾','怅','怆','忪','忸','怙','怵','怛','怏','怍','怩','怿','怡','恸','恹','恻','恺','恂','恪','悖','悚','悭','悛','惬','悱','惝','惘','惆','惚','悴','愠','愦','愕','愣','惴','愀','愎','愫','慵','憬','憔','憧','懔','懵','忝','闩','闫','闵','闾','阏','阖','阙','爿','戕','沐','沌','汨','汩','汴','汶','沆','泷','泱','泗','泠','泫','泮','沱','泓','泯','浒','浣','渎','涿','渑','淝','淙','涮','湮','滟','溏','滂','潇','潋','漪','漩','澍','潸','潲','潼','潺','濉','澧','濡','濮','濠','濯','瀚','瀣','瀛','灏','宕','宸','甯','骞','寤','寰','蹇','謇','遐','遢','遛','暹','遴','邈','邃','邋','彗','彖','咫','屐','孱','屣','羼','弪','弩','弼','鬻','妃','妍','妪','姊','妞','妤','妲','姗','妾','姝','娈','姘','娌','娉','娲','娑','婀','婊','婕','娼','婢','婵','胬','媛','婷','媾','嫔','嫣','嫱','嫖','嫦','嬉','嬲','嬷','孀','尕','孚','孥','孑','孓','孢','驷','驸','驿','驽','骈','骊','骒','骓','骛','骜','骠','骢','骥','骧','纣','纥','纨','纾','绮','绯','绺','缟','缢','缤','缥','缭','缰','缱','畿','甾','邕','珏','珂','玳','珈','玺','琦','瑁','瑜','瑕','瑙','瑷','瑾','璎','璀','璁','璇','璋','璞','璨','璐','璧','韪','韫','韬','杞','枭','枋','杷','柚','枳','栀','枸','桢','桦','桀','栾','梵','楠','楂','榄','槌','榈','楣','楹','榭','榕','槿','樯','槲','橛','樵','橹','樽','樨','橘','檐','檩','檗','檫','猷','獒','殁','殂','殇','殄','殒','殓','殚','殡','轶','辄','辇','辍','辘','戋','戛','戟','戢','戡','戬','臧','攴','旮','昊','昙','杲','昕','昀','炅','昝','昱','昶','昵','耆','晟','晔','晁','晏','晖','晗','晷','暄','暌','暧','暝','暾','曛','曜','曦','贻','贽','赅','赈','觇','觊','觋','觌','觎','觐','觑','犟','牦','牯','犄','犒','挈','挲','掰','擘','耄','毳','毽','氕','氘','氙','氚','氡','氩','氤','氪','氲','牍','爰','肓','肴','胧','胄','胴','胭','脍','朕','腓','腴','腚','腱','腩','腼','媵','膈','膑','滕','朦','臊','膻','膦','欷','欹','歆','飒','飓','飕','飙','殳','彀','毂','斐','斓','於','旃','旌','旎','旖','焖','焯','焱','煜','煨','煅','煲','煸','熵','熨','熠','燧','焘','煦','熹','戾','扈','扉','祉','祛','祠','祯','祺','禅','禧','禳','忑','忐','怼','恁','恙','恣','愆','憩','懋','懑','戆','聿','沓','泶','淼','砥','硎','砦','碥','磬','礓','礞','礴','龛','眈','眦','眵','眸','睑','睇','睨','睢','睥','睿','睽','瞌','瞑','瞟','瞠','瞰','町','畀','畈','罘','罡','罟','罹','羁','盍','盥','钊','钏','钗','钚','钛','钰','铊','铐','铢','铯','铿','锂','锕','锱','锲','镂','锵','镗','镢','镤','镫','镬','镯','镲','矬','雉','秣','稆','稞','稔','稹','稷','穑','黏','馥','皈','皎','皓','皙','甬','鸠','鸢','鸨','鸩','鸪','鸫','鸬','鸸','鸷','鸾','鹂','鹈','鹋','鹌','鹎','鹑','鹗','鹚','鹜','鹞','鹦','鹧','鹩','鹫','鹬','鹭','鹳','疖','疣','疱','痂','痣','痦','瘌','瘢','瘠','瘾','瘳','癍','癞','癔','癜','癖','癫','翊','竦','穹','窈','窕','窦','窠','窨','衩','衽','衿','袂','裆','袷','裱','裨','裾','褓','褛','褊','褴','褶','襁','襦','胥','皲','矜','耒','耜','耦','耧','耩','耋','耵','聃','聆','聍','聒','聩','覃','颀','颌','颏','颔','颚','颦','虔','虬','虿','蚝','蚣','蚓','蚩','蛄','蛎','蚱','蚯','蛭','蛐','蛟','蜃','蜇','蜈','蜊','蜍','蜉','蜣','蜻','蜥','蜚','蝈','蜴','蜱','蝾','蝠','蝌','蝼','蝙','蝥','螨','蟒','螈','螅','螃','螳','蟋','螽','蟑','蟀','蟊','蟠','蟮','蠖','蠓','蟾','蠛','蠡','蠹','蠼','缶','罂','罄','罅','舐','竺','笈','笃','笸','笪','笙','笠','笳','筠','筱','箧','箸','箪','箜','箢','箫','篁','篌','篝','篚','篦','簌','篾','簏','簋','簪','簸','籁','臾','舁','舂','舄','臬','舫','舸','舴','艄','艟','艨','衾','袅','袈','裘','裟','襞','羝','羟','羧','羯','羲','籼','粑','粝','粜','粞','粲','粼','粽','糁','糇','糌','糍','糅','糗','糨','艮','暨','羿','翎','翕','翡','翦','翩','翳','糸','繇','麸','麴','赳','趄','趔','赧','赭','豉','酊','酐','酰','醅','醐','醍','醪','醭','醴','醺','豕','趸','蹙','蹩','跄','跚','跛','跬','跹','跻','跤','踉','踝','踟','踮','踯','蹀','踹','踵','踽','踱','蹑','蹒','蹊','蹰','蹶','蹼','蹴','躅','躏','豸','貂','貅','貘','貔','斛','觞','觚','觥','訾','謦','靓','雳','雯','霆','霁','霈','霏','霪','霭','霰','霾','龃','龅','龇','龈','龉','龊','龌','黾','鼋','隹','隼','隽','雎','雒','瞿','雠','銮','錾','鎏','鐾','鑫','鱿','鲅','鲆','鲇','鲈','鲎','鲑','鲛','鲞','鲟','鲠','鲢','鲦','鲨','鲫','鲱','鲲','鲵','鲶','鲷','鲽','鳄','鳅','鳊','鳌','鳍','鳏','鳐','鳔','鳕','鳗','鳙','鳜','鳝','鳟','鳢','靼','鞑','鞫','鞲','鞴','骰','骷','鹘','骼','髁','髀','髅','髋','髌','魅','魃','魇','魉','魈','魍','魑','飨','餍','餮','饕','饔','髦','髫','髻','鬈','鬟','鬣','麽','麾','麇','麈','麋','麒','鏖','麝','麟','黛','黜','黝','黠','黟','黢','黩','黧','黥','黯','鼬','鼹','鼷','鼾','啊','阿','埃','挨','哎','唉','哀','皑','癌','蔼','矮','艾','碍','爱','隘','鞍','氨','安','俺','按','暗','岸','胺','案','肮','昂','盎','凹','敖','熬','翱','袄','傲','奥','懊','澳','芭','捌','扒','叭','吧','笆','八','疤','巴','拔','跋','靶','把','耙','坝','霸','罢','爸','白','柏','百','摆','佰','败','拜','稗','斑','班','搬','扳','般','颁','板','版','扮','拌','伴','瓣','半','办','绊','邦','帮','梆','榜','膀','绑','棒','磅','蚌','镑','傍','谤','苞','胞','包','褒','剥','薄','雹','保','堡','饱','宝','抱','报','暴','豹','鲍','爆','杯','碑','悲','卑','北','辈','背','贝','钡','倍','狈','备','惫','焙','被','奔','苯','本','笨','崩','绷','甭','泵','蹦','迸','逼','鼻','比','鄙','笔','彼','碧','蓖','蔽','毕','毙','毖','币','庇','痹','闭','敝','弊','必','辟','壁','臂','避','陛','鞭','边','编','贬','扁','便','变','卞','辨','辩','辫','遍','标','彪','膘','表','鳖','憋','别','瘪','彬','斌','濒','滨','宾','摈','兵','冰','柄','丙','秉','饼','炳','病','并','玻','菠','播','拨','钵','波','博','勃','搏','铂','箔','伯','帛','舶','脖','膊','渤','泊','驳','捕','卜','哺','补','埠','不','布','步','簿','部','怖','擦','猜','裁','材','才','财','睬','踩','采','彩','菜','蔡','餐','参','蚕','残','惭','惨','灿','苍','舱','仓','沧','藏','操','糙','槽','曹','草','厕','策','侧','册','测','层','蹭','插','叉','茬','茶','查','碴','搽','察','岔','差','诧','拆','柴','豺','搀','掺','蝉','馋','谗','缠','铲','产','阐','颤','昌','猖','场','尝','常','长','偿','肠','厂','敞','畅','唱','倡','超','抄','钞','朝','嘲','潮','巢','吵','炒','车','扯','撤','掣','彻','澈','郴','臣','辰','尘','晨','忱','沉','陈','趁','衬','撑','称','城','橙','成','呈','乘','程','惩','澄','诚','承','逞','骋','秤','吃','痴','持','匙','池','迟','弛','驰','耻','齿','侈','尺','赤','翅','斥','炽','充','冲','虫','崇','宠','抽','酬','畴','踌','稠','愁','筹','仇','绸','瞅','丑','臭','初','出','橱','厨','躇','锄','雏','滁','除','楚','础','储','矗','搐','触','处','揣','川','穿','椽','传','船','喘','串','疮','窗','幢','床','闯','创','吹','炊','捶','锤','垂','春','椿','醇','唇','淳','纯','蠢','戳','绰','疵','茨','磁','雌','辞','慈','瓷','词','此','刺','赐','次','聪','葱','囱','匆','从','丛','凑','粗','醋','簇','促','蹿','篡','窜','摧','崔','催','脆','瘁','粹','淬','翠','村','存','寸','磋','撮','搓','措','挫','错','搭','达','答','瘩','打','大','呆','歹','傣','戴','带','殆','代','贷','袋','待','逮','怠','耽','担','丹','单','郸','掸','胆','旦','氮','但','惮','淡','诞','弹','蛋','当','挡','党','荡','档','刀','捣','蹈','倒','岛','祷','导','到','稻','悼','道','盗','德','得','的','蹬','灯','登','等','瞪','凳','邓','堤','低','滴','迪','敌','笛','狄','涤','翟','嫡','抵','底','地','蒂','第','帝','弟','递','缔','颠','掂','滇','碘','点','典','靛','垫','电','佃','甸','店','惦','奠','淀','殿','碉','叼','雕','凋','刁','掉','吊','钓','调','跌','爹','碟','蝶','迭','谍','叠','丁','盯','叮','钉','顶','鼎','锭','定','订','丢','东','冬','董','懂','动','栋','侗','恫','冻','洞','兜','抖','斗','陡','豆','逗','痘','都','督','毒','犊','独','读','堵','睹','赌','杜','镀','肚','度','渡','妒','端','短','锻','段','断','缎','堆','兑','队','对','墩','吨','蹲','敦','顿','囤','钝','盾','遁','掇','哆','多','夺','垛','躲','朵','跺','舵','剁','惰','堕','蛾','峨','鹅','俄','额','讹','娥','恶','厄','扼','遏','鄂','饿','恩','而','儿','耳','尔','饵','洱','二','贰','发','罚','筏','伐','乏','阀','法','珐','藩','帆','番','翻','樊','矾','钒','繁','凡','烦','反','返','范','贩','犯','饭','泛','坊','芳','方','肪','房','防','妨','仿','访','纺','放','菲','非','啡','飞','肥','匪','诽','吠','肺','废','沸','费','芬','酚','吩','氛','分','纷','坟','焚','汾','粉','奋','份','忿','愤','粪','丰','封','枫','蜂','峰','锋','风','疯','烽','逢','冯','缝','讽','奉','凤','佛','否','夫','敷','肤','孵','扶','拂','辐','幅','氟','符','伏','俘','服','浮','涪','福','袱','弗','甫','抚','辅','俯','釜','斧','脯','腑','府','腐','赴','副','覆','赋','复','傅','付','阜','父','腹','负','富','讣','附','妇','缚','咐','噶','嘎','该','改','概','钙','盖','溉','干','甘','杆','柑','竿','肝','赶','感','秆','敢','赣','冈','刚','钢','缸','肛','纲','岗','港','杠','篙','皋','高','膏','羔','糕','搞','镐','稿','告','哥','歌','搁','戈','鸽','胳','疙','割','革','葛','格','蛤','阁','隔','铬','个','各','给','根','跟','耕','更','庚','羹','埂','耿','梗','工','攻','功','恭','龚','供','躬','公','宫','弓','巩','汞','拱','贡','共','钩','勾','沟','苟','狗','垢','构','购','够','辜','菇','咕','箍','估','沽','孤','姑','鼓','古','蛊','骨','谷','股','故','顾','固','雇','刮','瓜','剐','寡','挂','褂','乖','拐','怪','棺','关','官','冠','观','管','馆','罐','惯','灌','贯','光','广','逛','瑰','规','圭','硅','归','龟','闺','轨','鬼','诡','癸','桂','柜','跪','贵','刽','辊','滚','棍','锅','郭','国','果','裹','过','哈','骸','孩','海','氦','亥','害','骇','酣','憨','邯','韩','含','涵','寒','函','喊','罕','翰','撼','捍','旱','憾','悍','焊','汗','汉','夯','杭','航','壕','嚎','豪','毫','郝','好','耗','号','浩','呵','喝','荷','菏','核','禾','和','何','合','盒','貉','阂','河','涸','赫','褐','鹤','贺','嘿','黑','痕','很','狠','恨','哼','亨','横','衡','恒','轰','哄','烘','虹','鸿','洪','宏','弘','红','喉','侯','猴','吼','厚','候','后','呼','乎','忽','瑚','壶','葫','胡','蝴','狐','糊','湖','弧','虎','唬','护','互','沪','户','花','哗','华','猾','滑','画','划','化','话','槐','徊','怀','淮','坏','欢','环','桓','还','缓','换','患','唤','痪','豢','焕','涣','宦','幻','荒','慌','黄','磺','蝗','簧','皇','凰','惶','煌','晃','幌','恍','谎','灰','挥','辉','徽','恢','蛔','回','毁','悔','慧','卉','惠','晦','贿','秽','会','烩','汇','讳','诲','绘','荤','昏','婚','魂','浑','混','豁','活','伙','火','获','或','惑','霍','货','祸','击','圾','基','机','畸','稽','积','箕','肌','饥','迹','激','讥','鸡','姬','绩','缉','吉','极','棘','辑','籍','集','及','急','疾','汲','即','嫉','级','挤','几','脊','己','蓟','技','冀','季','伎','祭','剂','悸','济','寄','寂','计','记','既','忌','际','妓','继','纪','嘉','枷','夹','佳','家','加','荚','颊','贾','甲','钾','假','稼','价','架','驾','嫁','歼','监','坚','尖','笺','间','煎','兼','肩','艰','奸','缄','茧','检','柬','碱','硷','拣','捡','简','俭','剪','减','荐','槛','鉴','践','贱','见','键','箭','件','健','舰','剑','饯','渐','溅','涧','建','僵','姜','将','浆','江','疆','蒋','桨','奖','讲','匠','酱','降','蕉','椒','礁','焦','胶','交','郊','浇','骄','娇','嚼','搅','铰','矫','侥','脚','狡','角','饺','缴','绞','剿','教','酵','轿','较','叫','窖','揭','接','皆','秸','街','阶','截','劫','节','桔','杰','捷','睫','竭','洁','结','解','姐','戒','藉','芥','界','借','介','疥','诫','届','巾','筋','斤','金','今','津','襟','紧','锦','仅','谨','进','靳','晋','禁','近','烬','浸','尽','劲','荆','兢','茎','睛','晶','鲸','京','惊','精','粳','经','井','警','景','颈','静','境','敬','镜','径','痉','靖','竟','竞','净','炯','窘','揪','究','纠','玖','韭','久','灸','九','酒','厩','救','旧','臼','舅','咎','就','疚','鞠','拘','狙','疽','居','驹','菊','局','咀','矩','举','沮','聚','拒','据','巨','具','距','踞','锯','俱','句','惧','炬','剧','捐','鹃','娟','倦','眷','卷','绢','撅','攫','抉','掘','倔','爵','觉','决','诀','绝','均','菌','钧','军','君','峻','俊','竣','浚','郡','骏','喀','咖','卡','咯','开','揩','楷','凯','慨','刊','堪','勘','坎','砍','看','康','慷','糠','扛','抗','亢','炕','考','拷','烤','靠','坷','苛','柯','棵','磕','颗','科','壳','咳','可','渴','克','刻','客','课','肯','啃','垦','恳','坑','吭','空','恐','孔','控','抠','口','扣','寇','枯','哭','窟','苦','酷','库','裤','夸','垮','挎','跨','胯','块','筷','侩','快','宽','款','匡','筐','狂','框','矿','眶','旷','况','亏','盔','岿','窥','葵','奎','魁','傀','馈','愧','溃','坤','昆','捆','困','括','扩','廓','阔','垃','拉','喇','蜡','腊','辣','啦','莱','来','赖','蓝','婪','栏','拦','篮','阑','兰','澜','谰','揽','览','懒','缆','烂','滥','琅','榔','狼','廊','郎','朗','浪','捞','劳','牢','老','佬','姥','酪','烙','涝','勒','乐','雷','镭','蕾','磊','累','儡','垒','擂','肋','类','泪','棱','楞','冷','厘','梨','犁','黎','篱','狸','离','漓','理','李','里','鲤','礼','莉','荔','吏','栗','丽','厉','励','砾','历','利','傈','例','俐','痢','立','粒','沥','隶','力','璃','哩','俩','联','莲','连','镰','廉','怜','涟','帘','敛','脸','链','恋','炼','练','粮','凉','梁','粱','良','两','辆','量','晾','亮','谅','撩','聊','僚','疗','燎','寥','辽','潦','了','撂','镣','廖','料','列','裂','烈','劣','猎','琳','林','磷','霖','临','邻','鳞','淋','凛','赁','吝','拎','玲','菱','零','龄','铃','伶','羚','凌','灵','陵','岭','领','另','令','溜','琉','榴','硫','馏','留','刘','瘤','流','柳','六','龙','聋','咙','笼','窿','隆','垄','拢','陇','楼','娄','搂','篓','漏','陋','芦','卢','颅','庐','炉','掳','卤','虏','鲁','麓','碌','露','路','赂','鹿','潞','禄','录','陆','戮','驴','吕','铝','侣','旅','履','屡','缕','虑','氯','律','率','滤','绿','峦','挛','孪','滦','卵','乱','掠','略','抡','轮','伦','仑','沦','纶','论','萝','螺','罗','逻','锣','箩','骡','裸','落','洛','骆','络','妈','麻','玛','码','蚂','马','骂','嘛','吗','埋','买','麦','卖','迈','脉','瞒','馒','蛮','满','蔓','曼','慢','漫','谩','芒','茫','盲','氓','忙','莽','猫','茅','锚','毛','矛','铆','卯','茂','冒','帽','貌','贸','么','玫','枚','梅','酶','霉','煤','没','眉','媒','镁','每','美','昧','寐','妹','媚','门','闷','们','萌','蒙','檬','盟','锰','猛','梦','孟','眯','醚','靡','糜','迷','谜','弥','米','秘','觅','泌','蜜','密','幂','棉','眠','绵','冕','免','勉','娩','缅','面','苗','描','瞄','藐','秒','渺','庙','妙','蔑','灭','民','抿','皿','敏','悯','闽','明','螟','鸣','铭','名','命','谬','摸','摹','蘑','模','膜','磨','摩','魔','抹','末','莫','墨','默','沫','漠','寞','陌','谋','牟','某','拇','牡','亩','姆','母','墓','暮','幕','募','慕','木','目','睦','牧','穆','拿','哪','呐','钠','那','娜','纳','氖','乃','奶','耐','奈','南','男','难','囊','挠','脑','恼','闹','淖','呢','馁','内','嫩','能','妮','霓','倪','泥','尼','拟','你','匿','腻','逆','溺','蔫','拈','年','碾','撵','捻','念','娘','酿','鸟','尿','捏','聂','孽','啮','镊','镍','涅','您','柠','狞','凝','宁','拧','泞','牛','扭','钮','纽','脓','浓','农','弄','奴','努','怒','女','暖','虐','疟','挪','懦','糯','诺','哦','欧','鸥','殴','藕','呕','偶','沤','啪','趴','爬','帕','怕','琶','拍','排','牌','徘','湃','派','攀','潘','盘','磐','盼','畔','判','叛','乓','庞','旁','耪','胖','抛','咆','刨','炮','袍','跑','泡','呸','胚','培','裴','赔','陪','配','佩','沛','喷','盆','砰','抨','烹','澎','彭','蓬','棚','硼','篷','膨','朋','鹏','捧','碰','坯','砒','霹','批','披','劈','琵','毗','啤','脾','疲','皮','匹','痞','僻','屁','譬','篇','偏','片','骗','飘','漂','瓢','票','撇','瞥','拼','频','贫','品','聘','乒','坪','苹','萍','平','凭','瓶','评','屏','坡','泼','颇','婆','破','魄','迫','粕','剖','扑','铺','仆','莆','葡','菩','蒲','埔','朴','圃','普','浦','谱','曝','瀑','期','欺','栖','戚','妻','七','凄','漆','柒','沏','其','棋','奇','歧','畦','崎','脐','齐','旗','祈','祁','骑','起','岂','乞','企','启','契','砌','器','气','迄','弃','汽','泣','讫','掐','恰','洽','牵','扦','钎','铅','千','迁','签','仟','谦','乾','黔','钱','钳','前','潜','遣','浅','谴','堑','嵌','欠','歉','枪','呛','腔','羌','墙','蔷','强','抢','橇','锹','敲','悄','桥','瞧','乔','侨','巧','鞘','撬','翘','峭','俏','窍','切','茄','且','怯','窃','钦','侵','亲','秦','琴','勤','芹','擒','禽','寝','沁','青','轻','氢','倾','卿','清','擎','晴','氰','情','顷','请','庆','琼','穷','秋','丘','邱','球','求','囚','酋','泅','趋','区','蛆','曲','躯','屈','驱','渠','取','娶','龋','趣','去','圈','颧','权','醛','泉','全','痊','拳','犬','券','劝','缺','炔','瘸','却','鹊','榷','确','雀','裙','群','然','燃','冉','染','瓤','壤','攘','嚷','让','饶','扰','绕','惹','热','壬','仁','人','忍','韧','任','认','刃','妊','纫','扔','仍','日','戎','茸','蓉','荣','融','熔','溶','容','绒','冗','揉','柔','肉','茹','蠕','儒','孺','如','辱','乳','汝','入','褥','软','阮','蕊','瑞','锐','闰','润','若','弱','撒','洒','萨','腮','鳃','塞','赛','三','叁','伞','散','桑','嗓','丧','搔','骚','扫','嫂','瑟','色','涩','森','僧','莎','砂','杀','刹','沙','纱','傻','啥','煞','筛','晒','珊','苫','杉','山','删','煽','衫','闪','陕','擅','赡','膳','善','汕','扇','缮','墒','伤','商','赏','晌','上','尚','裳','梢','捎','稍','烧','芍','勺','韶','少','哨','邵','绍','奢','赊','蛇','舌','舍','赦','摄','射','慑','涉','社','设','砷','申','呻','伸','身','深','娠','绅','神','沈','审','婶','甚','肾','慎','渗','声','生','甥','牲','升','绳','省','盛','剩','胜','圣','师','失','狮','施','湿','诗','尸','虱','十','石','拾','时','什','食','蚀','实','识','史','矢','使','屎','驶','始','式','示','士','世','柿','事','拭','誓','逝','势','是','嗜','噬','适','仕','侍','释','饰','氏','市','恃','室','视','试','收','手','首','守','寿','授','售','受','瘦','兽','蔬','枢','梳','殊','抒','输','叔','舒','淑','疏','书','赎','孰','熟','薯','暑','曙','署','蜀','黍','鼠','属','术','述','树','束','戍','竖','墅','庶','数','漱','恕','刷','耍','摔','衰','甩','帅','栓','拴','霜','双','爽','谁','水','睡','税','吮','瞬','顺','舜','说','硕','朔','烁','斯','撕','嘶','思','私','司','丝','死','肆','寺','嗣','四','伺','似','饲','巳','松','耸','怂','颂','送','宋','讼','诵','搜','艘','擞','嗽','苏','酥','俗','素','速','粟','僳','塑','溯','宿','诉','肃','酸','蒜','算','虽','隋','随','绥','髓','碎','岁','穗','遂','隧','祟','孙','损','笋','蓑','梭','唆','缩','琐','索','锁','所','塌','他','它','她','塔','獭','挞','蹋','踏','胎','苔','抬','台','泰','酞','太','态','汰','坍','摊','贪','瘫','滩','坛','檀','痰','潭','谭','谈','坦','毯','袒','碳','探','叹','炭','汤','塘','搪','堂','棠','膛','唐','糖','倘','躺','淌','趟','烫','掏','涛','滔','绦','萄','桃','逃','淘','陶','讨','套','特','藤','腾','疼','誊','梯','剔','踢','锑','提','题','蹄','啼','体','替','嚏','惕','涕','剃','屉','天','添','填','田','甜','恬','舔','腆','挑','条','迢','眺','跳','贴','铁','帖','厅','听','烃','汀','廷','停','亭','庭','挺','艇','通','桐','酮','瞳','同','铜','彤','童','桶','捅','筒','统','痛','偷','投','头','透','凸','秃','突','图','徒','途','涂','屠','土','吐','兔','湍','团','推','颓','腿','蜕','褪','退','吞','屯','臀','拖','托','脱','鸵','陀','驮','驼','椭','妥','拓','唾','挖','哇','蛙','洼','娃','瓦','袜','歪','外','豌','弯','湾','玩','顽','丸','烷','完','碗','挽','晚','皖','惋','宛','婉','万','腕','汪','王','亡','枉','网','往','旺','望','忘','妄','威','巍','微','危','韦','违','桅','围','唯','惟','为','潍','维','苇','萎','委','伟','伪','尾','纬','未','蔚','味','畏','胃','喂','魏','位','渭','谓','尉','慰','卫','瘟','温','蚊','文','闻','纹','吻','稳','紊','问','嗡','翁','瓮','挝','蜗','涡','窝','我','斡','卧','握','沃','巫','呜','钨','乌','污','诬','屋','无','芜','梧','吾','吴','毋','武','五','捂','午','舞','伍','侮','坞','戊','雾','晤','物','勿','务','悟','误','昔','熙','析','西','硒','矽','晰','嘻','吸','锡','牺','稀','息','希','悉','膝','夕','惜','熄','烯','溪','汐','犀','檄','袭','席','习','媳','喜','铣','洗','系','隙','戏','细','瞎','虾','匣','霞','辖','暇','峡','侠','狭','下','厦','夏','吓','掀','锨','先','仙','鲜','纤','咸','贤','衔','舷','闲','涎','弦','嫌','显','险','现','献','县','腺','馅','羡','宪','陷','限','线','相','厢','镶','香','箱','襄','湘','乡','翔','祥','详','想','响','享','项','巷','橡','像','向','象','萧','硝','霄','削','哮','嚣','销','消','宵','淆','晓','小','孝','校','肖','啸','笑','效','楔','些','歇','蝎','鞋','协','挟','携','邪','斜','胁','谐','写','械','卸','蟹','懈','泄','泻','谢','屑','薪','芯','锌','欣','辛','新','忻','心','信','衅','星','腥','猩','惺','兴','刑','型','形','邢','行','醒','幸','杏','性','姓','兄','凶','胸','匈','汹','雄','熊','休','修','羞','朽','嗅','锈','秀','袖','绣','墟','戌','需','虚','嘘','须','徐','许','蓄','酗','叙','旭','序','畜','恤','絮','婿','绪','续','轩','喧','宣','悬','旋','玄','选','癣','眩','绚','靴','薛','学','穴','雪','血','勋','熏','循','旬','询','寻','驯','巡','殉','汛','训','讯','逊','迅','压','押','鸦','鸭','呀','丫','芽','牙','蚜','崖','衙','涯','雅','哑','亚','讶','焉','咽','阉','烟','淹','盐','严','研','蜒','岩','延','言','颜','阎','炎','沿','奄','掩','眼','衍','演','艳','堰','燕','厌','砚','雁','唁','彦','焰','宴','谚','验','殃','央','鸯','秧','杨','扬','佯','疡','羊','洋','阳','氧','仰','痒','养','样','漾','邀','腰','妖','瑶','摇','尧','遥','窑','谣','姚','咬','舀','药','要','耀','椰','噎','耶','爷','野','冶','也','页','掖','业','叶','曳','腋','夜','液','一','壹','医','揖','铱','依','伊','衣','颐','夷','遗','移','仪','胰','疑','沂','宜','姨','彝','椅','蚁','倚','已','乙','矣','以','艺','抑','易','邑','屹','亿','役','臆','逸','肄','疫','亦','裔','意','毅','忆','义','益','溢','诣','议','谊','译','异','翼','翌','绎','茵','荫','因','殷','音','阴','姻','吟','银','淫','寅','饮','尹','引','隐','印','英','樱','婴','鹰','应','缨','莹','萤','营','荧','蝇','迎','赢','盈','影','颖','硬','映','哟','拥','佣','臃','痈','庸','雍','踊','蛹','咏','泳','涌','永','恿','勇','用','幽','优','悠','忧','尤','由','邮','铀','犹','油','游','酉','有','友','右','佑','釉','诱','又','幼','迂','淤','于','盂','榆','虞','愚','舆','余','俞','逾','鱼','愉','渝','渔','隅','予','娱','雨','与','屿','禹','宇','语','羽','玉','域','芋','郁','吁','遇','喻','峪','御','愈','欲','狱','育','誉','浴','寓','裕','预','豫','驭','鸳','渊','冤','元','垣','袁','原','援','辕','园','员','圆','猿','源','缘','远','苑','愿','怨','院','曰','约','越','跃','钥','岳','粤','月','悦','阅','耘','云','郧','匀','陨','允','运','蕴','酝','晕','韵','孕','匝','砸','杂','栽','哉','灾','宰','载','再','在','咱','攒','暂','赞','赃','脏','葬','遭','糟','凿','藻','枣','早','澡','蚤','躁','噪','造','皂','灶','燥','责','择','则','泽','贼','怎','增','憎','曾','赠','扎','喳','渣','札','轧','铡','闸','眨','栅','榨','咋','乍','炸','诈','摘','斋','宅','窄','债','寨','瞻','毡','詹','粘','沾','盏','斩','辗','崭','展','蘸','栈','占','战','站','湛','绽','樟','章','彰','漳','张','掌','涨','杖','丈','帐','账','仗','胀','瘴','障','招','昭','找','沼','赵','照','罩','兆','肇','召','遮','折','哲','蛰','辙','者','锗','蔗','这','浙','珍','斟','真','甄','砧','臻','贞','针','侦','枕','疹','诊','震','振','镇','阵','蒸','挣','睁','征','狰','争','怔','整','拯','正','政','帧','症','郑','证','芝','枝','支','吱','蜘','知','肢','脂','汁','之','织','职','直','植','殖','执','值','侄','址','指','止','趾','只','旨','纸','志','挚','掷','至','致','置','帜','峙','制','智','秩','稚','质','炙','痔','滞','治','窒','中','盅','忠','钟','衷','终','种','肿','重','仲','众','舟','周','州','洲','诌','粥','轴','肘','帚','咒','皱','宙','昼','骤','珠','株','蛛','朱','猪','诸','诛','逐','竹','烛','煮','拄','瞩','嘱','主','著','柱','助','蛀','贮','铸','筑','住','注','祝','驻','抓','爪','拽','专','砖','转','撰','赚','篆','桩','庄','装','妆','撞','壮','状','椎','锥','追','赘','坠','缀','谆','准','捉','拙','卓','桌','琢','茁','酌','啄','着','灼','浊','兹','咨','资','姿','滋','淄','孜','紫','仔','籽','滓','子','自','渍','字','鬃','棕','踪','宗','综','总','纵','邹','走','奏','揍','租','足','卒','族','祖','诅','阻','组','钻','纂','嘴','醉','最','罪','尊','遵','昨','左','佐','柞','做','作','坐','座']

seed = len(letters)

print seed

with codecs.open('10w.csv', 'w', encoding='utf-8') as csvfile:
    csvfile.write('%s %s\n' % ('filename', 'string'))

    hh = 0
    while (hh < 100):
        hh = hh + 1

        rootDir = '/home/sensetime/deepir_test/test_images/class0_normal'
        list_dir = os.walk(rootDir)

        for root, d, fs in list_dir:
            for file in fs:
                image_path = os.path.join(root, file)
                print(image_path)
                im = Image.open(image_path)
                width, height = im.size
                print im.size
                print width
                print height
                print im.mode
                draw = ImageDraw.Draw(im)

                length = random.randint(1, 30)

                ll = length;

                string = ''
                font = random.randint(1, fonts)
                font_select = 1
                print font

                fontDir = "/alter/fonts"
                font_dir = os.walk(fontDir)

                path = ""

                for roo, dirs, files in font_dir:
                    print 1
                    for f in files:
                        if(font_select == font):
                            print font
                            path = os.path.join(roo, f)
                            print path
                            break
                        font_select = font_select + 1

                ttfont = ImageFont.truetype(path, 30)

                print path

                while (length > 0):
                    choice = random.randint(0, seed - 1)
                    print letters[choice]
                    string = string + letters[choice]
                    length = length - len(letters[choice])

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                # watermark = Image.new("RGBA", im.size)
                # waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")

                draw.text((12, 14), string.decode('utf-8'), fill=(r, g, b), font=ttfont)
                t_width, t_height = draw.textsize(unicode(string, 'UTF-8'), font = ttfont)
                print r
                print g
                print b

                print string

                #box = (0, 0, 20 + t_width, 30 + t_height)

                rX = 16 + t_width
                rY = 24 + t_height

                box = (8, 12, rX, rY)

                alpha = random.randint(20, 160)

                # watermask = watermark.convert("L").point(lambda x: min(x, alpha))
                #
                # watermark.putalpha(watermask)
                #
                # im.paste(watermark, None, watermark)

                region = im.crop(box)

                index = index + 1

                filename = '10w/' + str(index) + '.jpg'

                fname = str(index) + '.jpg'

                region.save(filename)

                csvfile.write('%s %s\n' % (fname, string.decode('utf-8')))
