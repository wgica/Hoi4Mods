outdirT=r"C:\Users\wgic\Documents\Paradox Interactive\Hearts of Iron IV\mod\Universal Unlock Units\uuu_core_tech.txt"
##在上面输入目标文件路径  Enter the target file path above👆


namelist=[

    ##原版名称

    "light_tank_recon",
    "infantry",
    "medium_flame_tank",
    "military_police",
    "camelry",
    "winter_logistics_support",
    "pioneer_support",
    "armored_car_recon",
    "rangers_support",
    "militia",
    "long_range_patrol_support",
    "motorized_rocket_brigade",
    "mot_recon",
    "light_flame_tank",
    "penal_battalion",
    "blackshirt_assault_battalion",
    "recon",
    "bus",
    "marine",
    "logistics_company",
    "irregular_infantry",
    "maintenance_company",
    "jungle_pioneers_support",
    "mountaineers",
    "motorized",
    "field_hospital",
    "engineer",
    "signal_company",
    "airborne_light_armor",
    "bicycle_battalion",
    "paratrooper",
    "fake_intel_unit",
    "heavy_flame_tank",

    ##56之路
    "mot_shocktroop",
    "militia",
    "mech_shocktroop",
    "infantry",
    "desertinfantry",
    "motorized",
    "marine",
    "camelry",
    "shocktroop",
    "jaeger",
    "fake_intel_unit",
    "penal_battalion",
    "mountaineers",
    "jungletroop",
    "bicycle_battalion",
    "paratrooper",
    "motorized_rocket_brigade",
    "irregular_infantry",

    #TNO
    "anti_tank",
    "air_assault",
    "light_infantry",
    "alt_MBT",
    "cavalry",
    "mot_recon",
    "experimental_helicopter_company",
    "maintenance_company",
    "infantry",
    "pony_ontreads",
    "recon",
    "pony_onhooves",
    "experimental_infantry_rifles",
    "scout_helicopter_company",
    "AC_recon",
    "anti_tank_brigade",
    "egghead",
    "elite_infantry",
    "military_police",
    "IFV_recon",
    "IFV_flame_tank",
    "alt_motorized",
    "signal_company",
    "militia",
    "motorized",
    "fake_intel_unit",
    "irregular_infantry",
    "marine",
    "attack_helicopter_company",
    "alt_light_infantry",
    "logistics_company",
    "alt_marine",
    "MBT_recon",
    "alt_APC",
    "field_hospital",
    "MBT_flame_tank",
    "mountaineers",
    "engineer",
    "alt_infantry",
    "mbt_engineer",
    "mot_anti_tank_brigade",
    "pegasi",
    "transport_helicopter_company",
    "transport_helicopter_supply_company",
    "garrison",

]



import codecs
import time

start = time.time()
namelistone = list(set(namelist))
print(len(namelist),len(namelistone))
with codecs.open(outdirT,"w","utf-8") as file:
    file.write("""technologies = { uuu_tech_1 = { allow = { always = no } enable_subunits = { """)
    for name in namelistone:
        file.write(name+" ")  
    file.write(" } } }")

end = time.time()
print("Using time: "+str(end - start)+"s")