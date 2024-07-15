namelist=[
    ##原版名称

    ##兼容mod————《人名和部队名称汉化 （只限原版）》[2067895531]
    "马其顿革命军",#BUL
    "尼德兰国土风暴国民卫队",#DEN
    "赤卫队",#ETH
    "黑狮组织师",
    "海岸兵团",#FIN
    "叙利亚干预部队",#FRA
    "叙利亚防卫军",
    "印度支那干涉部队",
    "印度支那防卫军",
    "中部非洲干预部队",
    "中非武装防卫军",
    "西非干预部队",
    "西非国防军",
    "殖民地骑警师",#ITA
    "非正规骆驼骑兵师",
    "殖民地骑兵队",
    "托米斯拉夫皇家卫队",
    "黑山切特尼克师",
    "救赎军",#MAN
    "八旗师",
    "民兵师",#POL
    "国际马克思主义旅"#SOV
    "苏联特种旅"
    "银衫军团",#USA
    "苏联志愿军",#baltic
    "森林兄弟游击队",
    "外籍军团",#BRA
    "囚犯营",
    "智利祖国警卫队",#CHL
    "阿根廷志愿军",
    "共和国卫队",
    "骑兵师",#ETH
    "骆驼骑兵师",
    "刚果雇佣军",
    "阿拉伯雇佣军",
    "赤卫队",
    "黑狮组织师",
    "警卫",
    "厄立特里亚战士师",
    "苏丹雇佣军",
    "芬兰黑衫军",#FIN
    "工人赤卫队",
    "苏联军团",
    "惩戒步兵师",
    "FFI半旅团",#FFR
    "东非民兵师",#HOA
    "殖民地骑兵队",#ITA
    "殖民地骑警师",
    "非正规骆驼骑兵师",
    "游击队",
    "赤军",#JAP
    "保皇党师团",
    "火十字团",#LAT
    "女王陛下的德国军团",#HOL
    "美洲驻军",
    "毛利人志愿军",#NZL
    "莫尔日师",#POL
    "惩戒营",#SOV
    "托洛茨基主义革命民兵",
    "第五纵队",#SPR
    "无政府主义民兵师",
    "警卫团",
    "可移动总部",#SWE
    "家园卫队",
    "冲锋队",
    "南斯拉夫防卫军",#YUG
    "反剥削惩戒旅",#00
    "祖国阵线民兵师",#BUL
    "祖国阵线游击队",
    "抵抗军民兵",#DEN
    "抵抗战士",#ETH
    "红衫军",#ITA
    "国王军",
    "防卫民兵",
    "秘密军队",
    "党属民兵卫队",
    "武装部队",
    "挪威人民军",
    "国际马克思主义旅",
    "统工党特战旅",
    "统工党青年旅",
    "托洛茨基主义工人民兵",
    "托洛茨基主义农民民兵",
    "布哈林工人民兵",
    "布哈林农民民兵",
    "日本远征军",
    "反对派游击队",
    "Swiss Citizen Militia",
    "流亡者",
    "公民民兵",
    "疑兵师",
    "殖民地骑兵队",
    "非正规骆驼骑兵师"
    "丹麦旅",
    "卡累利阿森林游击队",
    "工人民兵",
    "切特师",
    "警卫",
    "抵抗军",
    "国际旅",
    "Resistance",
    "国民警卫队",
    "共和警卫队",
    "卡洛斯呼啸兵",
    "突击卫队师",
    "国民卫队旅",
    "突击卫队师",
    "联合青年旅",
    "人民旅",
    "无政府主义旅",
    "西班牙卡洛斯保皇师",
    "忠良旅",
    "黑衫军旅",
    "巴基斯坦解放军",
    "印度民兵师",
    "孟加拉国解放军",
    "本土志愿军",
    "Citizen Militia",
    "国际马克思主义旅",
    "苏联特种旅",
    "国际旅",
    "德国培训师",
    "卡累利阿森林游击队",
    "抵抗军",
    "咒缚军团",
    "自由印度军团",
    "苏联志愿军",
    "荣誉卫队",
    "切特师",
    "党卫军突击旅",
    "民兵团",
    "黑衫军",
    "土著民兵师",
    "殖民地骑警师",
    "利比亚班队",
    "厄立特里亚班队",
    "索马里班队",
    "内务人民委员部边境卫队",
    "步兵旅",
    "国际旅",
    "轻装旅",



]
import codecs
namelistone = list(set(namelist))
with codecs.open("nuu_core_ses.txt", "w","utf-8") as file:
    file.write("""nuu_core_eff = {
	country_lock_all_division_template = no\n""")
    for name in namelistone:
        file.write("""	if = {
		limit = {
			has_template = """+"\""+name+"\""+"""
		}
		set_division_template_lock = {
			division_template = """+"\""+name+"\""+"""
			is_locked = no
        }
	}
  """)  
    file.write("}")