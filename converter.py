import xml.etree.ElementTree as ET
import os
import ctypes

tree = ET.parse("types.xml")
root = tree.getroot()



end ="""}\n]\n}"""	

head = """{
    "m_Version": 12,
    "DisplayName": "",
    "Icon": "Trader",
    "Color": "EB3736FF",
    "InitStockPercent": 100,
    "Items": [\n"""

precursor1 ="""		{\n			"ClassName": """

precursor ="""
			"MaxPriceThreshold": 500,
			"MinPriceThreshold": 500,
			"SellPricePercent": -1,
			"MaxStockThreshold": 1,
			"MinStockThreshold": 1,
			"QuantityPercent": -1,
			"SpawnAttachments": [],
			"Variants": []"""

categories = {}

traders = {
	"Consume Trader": ["Food", "Canteens", "Seeds"], # 0
	"Misc Trader": ["Containers", "Tools", "Kits", "Viking", "Bbp", "Msp", "Mass", "Cp", "Mung", "Mmg", "Imp","Clothes"], # 1
	"Weapon Trader": ["Weapons", "Explosives"], # 2
	"Clothing Trader": ["Shirts", "Pants", "Coats", "Jackets", "Vests", "Bags", "Shoes", "Gear", "Boots", "Belts", "Helmet", "Masks", "Glasses", "Armbands", "Ghillie", "OtherClothes"], # 3
	"Weapon Supplies Trader": ["Mags", "Ammo", "Attachments", "Optics"], # 4
	"Vehicles Trader": ["Vehiclesparts", "Vehicles"] # 5
}

banned_prefixes = [
	"animal",
	"christmastree",
	"land_wreck",
	"wreck",
	"zmb",
	"slottedwood",
	"BusPsychoWheel_offroad_Ruined",

]

IsFirstEntry = True;
precursor_end = ""

for child in root:
	name = ('"') + child.attrib["name"] + ('"')
	category = ""
	quantity = ""

	for childs_child in child:
		if childs_child.tag == "category":
			category = childs_child.attrib["name"]

	shouldContinue = True
	for prefix in banned_prefixes:
		if len(prefix) <= len(name):
			if name[:len(prefix)].lower() == prefix.lower():
				shouldContinue = False

	if shouldContinue == False:
		continue

	elif ("shirt" in name.lower()):
		category = "Shirts"

	elif ("pant" in name.lower()):
		category = "Pants"

	elif ("coat" in name.lower()):
		category = "Coats"

	elif ("mmg" in name.lower()):
		category = "Mmg"

	elif ("clothes" in name.lower()):
		category = "Clothes"

	elif ("imp" in name.lower()):
		category = "Imp"

	elif ("jacket" in name.lower()):
		category = "Jackets"

	elif ("vest" in name.lower() or "platecarrier" in name.lower()):
		category = "Vests"

	elif ("pouch" in name.lower() or "holster" in name.lower() or "sheath" in name.lower()):
		category = "Gear"

	elif ("shoe" in name.lower()):
		category = "Shoes"

	elif ("tool" in name.lower()):
		category = "Tools"

	elif ("boot" in name.lower()):
		category = "Boots"

	elif ("belt" in name.lower()):
		category = "Belts"

	elif ("helmet" in name.lower()):
		category = "Helmets"

	elif ("glasses" in name.lower()):
		category = "Glasses"

	elif ("armband" in name.lower() or "patch" in name.lower()):
		category = "Armbands"

	elif ("ghillie" in name.lower()):
		category = "Ghillie"

	elif ("mask" in name.lower() or "respirator" in name.lower() or "shemagh" in name.lower()):
		category = "Masks"

	elif name[:3].lower() == "bbp":
		category = "Bbp"

	elif name[:3].lower() == "viking":
		category = "Viking"
	
	elif name[:3].lower() == "msp":
		category = "Msp"
	
	elif name[:4].lower() == "mass":
		category = "Mass"

	elif name[:2].lower() == "cp":
		category = "Cp"

	elif name[-4:].lower() == "mung":
		category = "Mung"

	elif name[:11].lower() == "rag_hummer_":
		category = "Vehiclesparts"

	elif name[-4:].lower() == "_kit":
		category = "Kits"

	elif ("bag" in name.lower()):
			category = "Bags"

	elif ("fridge" in name.lower()):
		category = "Containers"

	elif ("canteen" in name.lower()):
		category = "Canteens"

	elif ("seed" in name.lower()):
		category = "Seeds"

	elif ("ammo" in name.lower()):
		category = "Ammo"

	elif ("mag" in name.lower()):
		category = "Mags"
		

	elif ("bttstck" in name.lower() or "compensator" in name.lower() or "hndgrd" in name.lower() or "hndguard" in name.lower() or "buttstock" in name.lower() or "suppressor" in name.lower() or "mount" in name.lower()):
		category = "Attachments"

	elif ("optic" in name.lower() or "acog" in name.lower() or "sight" in name.lower() or "scope" in name.lower()):
		category = "Optics"

	elif name[-9:].lower() == "destroyed":
		continue

	elif name[-9:].lower() == "_deployed":
		continue

	elif category == "":
		category = "Vehicles"
		quantity = ""

	if not (category.capitalize() in categories):
		categories[category.capitalize()] = []

	categories[category.capitalize()].append({"name": name, "quantity": quantity})

f = open("TraderConfig.json", "w")
f.write(head)

typeNames = []

for trader in traders:	
	for category in categories:
		if category in traders[trader]:
			f.write("")
			for item in categories[category]:
				if (item["name"] in typeNames):
					continue
				
				precursor_end = "		},\n"
				precursor_end2 = "\n" +"		}"+"\n	]"+"\n}"

				if IsFirstEntry == True:
					precursor_end = ""
					IsFirstEntry = False

					 

				writeString ="{:<70}".format(precursor_end + precursor1 + item["name"] + "," + precursor)
				f.write(writeString + item["quantity"] + "			 			\n")
f.write(precursor_end2)
f.close()
ctypes.windll.user32.MessageBoxW(0, "made by Ninjin~ ", "Information",1)
9
