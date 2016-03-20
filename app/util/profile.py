#coding=utf-8

ChandiSettingDictionary = {}
JiaogeSettingDictionary = {}

SettingDictionary = {
	u'产地': ChandiSettingDictionary,
	u'交割地': JiaogeSettingDictionary
}

IdList = []
SettingList = []

class Setting(object):

	def __init__(self, id, name, category, group = -1):
		self.id = id
		self.name = name
		self.group = group
		self.category = category
		global SettingDictionary
		SettingDictionary[category][id] = self
		global SettingList
		SettingList.append(self)
		global IdList
		if id not in IdList:
			IdList.append(id)
	
	def getName(self):
		return self.name


Setting(id=20, name=u'内蒙古', category=u'产地')
Setting(id=21, name=u'山西', category=u'产地')
Setting(id=22, name=u'陕西', category=u'产地')
Setting(id=56, name=u'河北', category=u'产地')
Setting(id=68, name=u'山东', category=u'产地')
Setting(id=74, name=u'朝鲜', category=u'产地')
Setting(id=76, name=u'安徽', category=u'产地')
Setting(id=77, name=u'河南', category=u'产地')
Setting(id=109, name=u'俄罗斯', category=u'产地')
Setting(id=110, name=u'黑龙江', category=u'产地')
Setting(id=130, name=u'吉林', category=u'产地')
Setting(id=148, name=u'辽宁', category=u'产地')
Setting(id=192, name=u'湖南', category=u'产地')
Setting(id=251, name=u'甘肃', category=u'产地')
Setting(id=288, name=u'宁夏', category=u'产地')
Setting(id=301, name=u'贵州', category=u'产地')
Setting(id=339, name=u'四川', category=u'产地')
Setting(id=372, name=u'云南', category=u'产地')
Setting(id=471, name=u'越南', category=u'产地')
Setting(id=476, name=u'南非', category=u'产地')
Setting(id=479, name=u'澳大利亚', category=u'产地')
Setting(id=482, name=u'印度尼西亚', category=u'产地')
Setting(id=488, name=u'美国', category=u'产地')
Setting(id=492, name=u'蒙古国', category=u'产地')

#交割地category的group标识:
#1--华东，2--华北，3--西北，4--西南，5--华中，6--东北，7--华南，8--外国地，-1--未分组

#group 1
Setting(id=437, name=u'镇海港', category=u'交割地', group=1)
Setting(id=436, name=u'北仑港', category=u'交割地', group=1)
Setting(id=435, name=u'乍浦港', category=u'交割地', group=1)
Setting(id=428, name=u'江阴港', category=u'交割地', group=1)
Setting(id=431, name=u'扬子江港', category=u'交割地', group=1)
Setting(id=463, name=u'九江港', category=u'交割地', group=1)
Setting(id=462, name=u'丰城港', category=u'交割地', group=1)
Setting(id=446, name=u'泉州港', category=u'交割地', group=1)
Setting(id=445, name=u'莆田八方港', category=u'交割地', group=1)
Setting(id=444, name=u'漳州港', category=u'交割地', group=1)
Setting(id=443, name=u'福州港', category=u'交割地', group=1)
Setting(id=442, name=u'厦门港', category=u'交割地', group=1)
Setting(id=441, name=u'海沧港', category=u'交割地', group=1)
Setting(id=440, name=u'温州港', category=u'交割地', group=1)
Setting(id=439, name=u'玉环港', category=u'交割地', group=1)
Setting(id=438, name=u'舟山港', category=u'交割地', group=1)
Setting(id=432, name=u'大港', category=u'交割地', group=1)
Setting(id=430, name=u'南京港惠宁', category=u'交割地', group=1)
Setting(id=429, name=u'南京港西坝', category=u'交割地', group=1)
Setting(id=427, name=u'如皋港', category=u'交割地', group=1)
Setting(id=426, name=u'泰州港', category=u'交割地', group=1)
Setting(id=425, name=u'南通港', category=u'交割地', group=1)
Setting(id=424, name=u'邳州港', category=u'交割地', group=1)
Setting(id=423, name=u'万寨港', category=u'交割地', group=1)
Setting(id=422, name=u'张家港', category=u'交割地', group=1)
Setting(id=421, name=u'江都港', category=u'交割地', group=1)
Setting(id=420, name=u'扬州港', category=u'交割地', group=1)
Setting(id=419, name=u'连云港', category=u'交割地', group=1)
Setting(id=418, name=u'日照港', category=u'交割地', group=1)
Setting(id=417, name=u'青岛港', category=u'交割地', group=1)
Setting(id=416, name=u'威海港', category=u'交割地', group=1)
Setting(id=415, name=u'蓬莱港', category=u'交割地', group=1)
Setting(id=414, name=u'烟台港', category=u'交割地', group=1)
Setting(id=413, name=u'龙口港', category=u'交割地', group=1)
Setting(id=412, name=u'东营港', category=u'交割地', group=1)
Setting(id=491, name=u'常州港', category=u'交割地', group=1)
Setting(id=493, name=u'靖江码头', category=u'交割地', group=1)
Setting(id=494, name=u'泰富港', category=u'交割地', group=1)
Setting(id=498, name=u'泰州民生港', category=u'交割地', group=1)
Setting(id=499, name=u'江阴长宏国际码头', category=u'交割地', group=1)
Setting(id=500, name=u'青岛前港', category=u'交割地', group=1)
Setting(id=502, name=u'新长江港', category=u'交割地', group=1)
Setting(id=504, name=u'博联港', category=u'交割地', group=1)
Setting(id=506, name=u'中林如皋港', category=u'交割地', group=1)
Setting(id=507, name=u'靖江港', category=u'交割地', group=1)
Setting(id=508, name=u'镇江港', category=u'交割地', group=1)
Setting(id=509, name=u'台州港', category=u'交割地', group=1)

#group 2
Setting(id=409, name=u'黄骅港', category=u'交割地', group=2)
Setting(id=408, name=u'曹妃甸', category=u'交割地', group=2)
Setting(id=407, name=u'秦皇岛港', category=u'交割地', group=2)
Setting(id=505, name=u'河北钢铁码头', category=u'交割地', group=2)

#group 3
Setting(id=484, name=u'二连浩特口岸', category=u'交割地', group=3)
Setting(id=485, name=u'甘其毛都口岸', category=u'交割地', group=3)
Setting(id=486, name=u'策克口岸', category=u'交割地', group=3)

#group 4 empty for now

#group 5
Setting(id=467, name=u'城陵矶', category=u'交割地', group=5)
Setting(id=466, name=u'黄石', category=u'交割地', group=5)
Setting(id=465, name=u'平鄂港', category=u'交割地', group=5)
Setting(id=464, name=u'枝城港', category=u'交割地', group=5)
Setting(id=461, name=u'芜湖港', category=u'交割地', group=5)

#group 6
Setting(id=406, name=u'葫芦岛港', category=u'交割地', group=6)
Setting(id=405, name=u'锦州港', category=u'交割地', group=6)
Setting(id=404, name=u'鲅鱼圈港', category=u'交割地', group=6)
Setting(id=403, name=u'大连港', category=u'交割地', group=6)
Setting(id=402, name=u'丹东港', category=u'交割地', group=6)

#group 7
Setting(id=460, name=u'防城港', category=u'交割地', group=7)
Setting(id=459, name=u'钦州港', category=u'交割地', group=7)
Setting(id=458, name=u'铁山港', category=u'交割地', group=7)
Setting(id=457, name=u'北海港', category=u'交割地', group=7)
Setting(id=456, name=u'茂名港', category=u'交割地', group=7)
Setting(id=455, name=u'东莞明盛码头', category=u'交割地', group=7)
Setting(id=454, name=u'汕头港', category=u'交割地', group=7)
Setting(id=453, name=u'广州港西基码头', category=u'交割地', group=7)
Setting(id=452, name=u'黄埔新港', category=u'交割地', group=7)
Setting(id=451, name=u'黄埔老港', category=u'交割地', group=7)
Setting(id=450, name=u'广州港新沙码头', category=u'交割地', group=7)
Setting(id=449, name=u'珠海港', category=u'交割地', group=7)
Setting(id=448, name=u'高栏港', category=u'交割地', group=7)
Setting(id=447, name=u'湛江港', category=u'交割地', group=7)
Setting(id=497, name=u'东莞海昌码头', category=u'交割地', group=7)
Setting(id=503, name=u'珠电码头', category=u'交割地', group=7)
Setting(id=510, name=u'广州港', category=u'交割地', group=7)

#group 8
Setting(id=74, name=u'朝鲜', category=u'交割地', group=8)
Setting(id=109, name=u'俄罗斯', category=u'交割地', group=8)
Setting(id=471, name=u'越南', category=u'交割地', group=8)
Setting(id=476, name=u'南非', category=u'交割地', group=8)
Setting(id=479, name=u'澳大利亚', category=u'交割地', group=8)
Setting(id=482, name=u'印度尼西亚', category=u'交割地', group=8)
Setting(id=488, name=u'美国', category=u'交割地', group=8)

def generate_unique_serial_number():
	import random
	return "{0}".format(random.random()).replace('.', '')

def get_jiaogedi_name_by_id(id):
	if id in JiaogeSettingDictionary:
		return JiaogeSettingDictionary[id].getName()
	return ''

