import organelles


#  Artery Info
#  TODO: missing arms
#  TODO: Stretch - minor vessels, veins?


def build_network():
    vessel_dict = {"Heart": organelles.Heart("Heart", [(265, 265)]),
                   "Aortic arch": organelles.BloodVessel("Aortic arch", 0.03, 0.276, [(265, 215)]),
                   "Brachiocephalic": organelles.BloodVessel("Brachiocephalic", 0.012, 0.0865, [(245, 205)]),
                   "R common carotid": organelles.BloodVessel("R common carotid", 0.006, 0.233, [(225, 160)]),
                   "R Internal carotid": organelles.BloodVessel("R Internal carotid", 0.001, 0.283, [(221, 98)]),
                   "R External carotid": organelles.BloodVessel("R External carotid", 0.001, 0.204, [(208, 85)]),
                   "R subclavian": organelles.BloodVessel("R subclavian", 0.025, 0.467, [(185, 205)]),
                   "L common carotid": organelles.BloodVessel("L common carotid", 0.006, 0.232, []),
                   "L Internal carotid": organelles.BloodVessel("L Internal carotid", 0.001, 0.283, []),
                   "L External carotid": organelles.BloodVessel("L External carotid", 0.001, 0.204, []),
                   "L subclavian": organelles.BloodVessel("L subclavian", 0.025, 0.467, []),
                   "R Vertebral artery": organelles.BloodVessel("R Vertebral artery", 0.004, 0.41, [(250, 160)]),
                   "L Vertebral artery": organelles.BloodVessel("L Vertebral artery", 0.004, 0.41, []),
                   "Descending Aorta": organelles.BloodVessel("Descending Aorta", 0.015, 0.412, [(262, 320)]),
                   "Abdominal aorta": organelles.BloodVessel("Abdominal aorta", 0.02, 0.403, [(262, 385)]),
                   "Celiac": organelles.BloodVessel("Celiac", 0.0078, 0.037, [(261, 338)]),
                   "L Gastric": organelles.BloodVessel("L Gastric", 0.0038, 0.067, [(239, 343)]),
                   "Common hepatic": organelles.BloodVessel("Common hepatic", 0.004, 0.044, [(239, 339)]),
                   "Splenic": organelles.BloodVessel("Splenic", 0.0061, 0.07912, [(289, 334)]),
                   "SMA": organelles.BloodVessel("SMA", 0.08, 0.552, [(281, 381)]),
                   "Renal": organelles.BloodVessel("Renal", 0.0055, 0.0662, [(241, 368)]),
                   "IMA": organelles.BloodVessel("IMA", 0.04, 0.138, [(251, 410)]),
                   "L common iliac": organelles.BloodVessel("L common iliac", 0.012, 0.046, []),
                   "R common iliac": organelles.BloodVessel("R common iliac", 0.013, 0.1472, [(235, 445)]),
                   "L external iliac": organelles.BloodVessel("L external iliac", 0.01, 0.368, []),
                   "L internal iliac": organelles.BloodVessel("L internal iliac", 0.006, 0.1656, []),
                   "L femoral": organelles.BloodVessel("L femoral", 0.01, 1.135, []),
                   "L profunda femoris": organelles.BloodVessel("L profunda femoris", 0.006, 0.6054, []),
                   "L popliteal": organelles.BloodVessel("L popliteal", 0.009, 0.1518, []),
                   "L peroneal": organelles.BloodVessel("L peroneal", 0.0015, 0.4453, []),
                   "L anterior tibial": organelles.BloodVessel("L anterior tibial", 0.0028, 1.046, []),
                   "L posterior tibial": organelles.BloodVessel("L posterior tibial", 0.0019, 0.605, []),
                   "L dorsalis pedis": organelles.BloodVessel("L dorsalis pedis", 0.0033, 0.152, []),
                   "R external iliac": organelles.BloodVessel("R external iliac", 0.01, 0.3128, [(206, 502)]),
                   "R internal iliac": organelles.BloodVessel("R internal iliac", 0.006, .166, [(239, 461)]),
                   "R femoral": organelles.BloodVessel("R femoral", 0.01, 1.135, [(201, 636)]),
                   "R profunda femoris": organelles.BloodVessel("R profunda femoris", 0.006, 0.65, [(206, 503)]),
                   "R popliteal": organelles.BloodVessel("R popliteal", 0.009, 0.477, [(189, 694)]),
                   "R peroneal": organelles.BloodVessel("R peroneal", 0.0015, 0.445, [(176, 813)]),
                   "R anterior tibial": organelles.BloodVessel("R anterior tibial", 1.046, 0.0028, [(183, 826)]),
                   "R posterior tibial": organelles.BloodVessel("R posterior tibial", 0.0019, 0.605, [(166, 822)]),
                   "R dorsalis pedis": organelles.BloodVessel("R dorsalis pedis", 0.0033, 0.152, [(155, 961)])}
    vessel_dict["Heart"].add_recipient(vessel_dict["Aortic arch"])
    vessel_dict["Aortic arch"].add_recipient(vessel_dict["Brachiocephalic"])
    vessel_dict["Aortic arch"].add_recipient(vessel_dict["L common carotid"])
    vessel_dict["Aortic arch"].add_recipient(vessel_dict["L subclavian"])
    vessel_dict["Aortic arch"].add_recipient(vessel_dict["R subclavian"])
    vessel_dict["Aortic arch"].add_recipient(vessel_dict["Descending Aorta"])
    vessel_dict["Brachiocephalic"].add_recipient(vessel_dict["R common carotid"])
    vessel_dict["Brachiocephalic"].add_recipient(vessel_dict["R subclavian"])
    vessel_dict["L common carotid"].add_recipient(vessel_dict["L Internal carotid"])
    vessel_dict["L common carotid"].add_recipient(vessel_dict["L External carotid"])
    vessel_dict["R common carotid"].add_recipient(vessel_dict["R Internal carotid"])
    vessel_dict["R common carotid"].add_recipient(vessel_dict["R External carotid"])
    vessel_dict["L subclavian"].add_recipient(vessel_dict["L Vertebral artery"])
    vessel_dict["R subclavian"].add_recipient(vessel_dict["R Vertebral artery"])
    vessel_dict["Descending Aorta"].add_recipient(vessel_dict["Abdominal aorta"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["Celiac"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["Renal"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["SMA"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["IMA"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["L common iliac"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["R common iliac"])
    vessel_dict["Celiac"].add_recipient(vessel_dict["L Gastric"])
    vessel_dict["Celiac"].add_recipient(vessel_dict["Common hepatic"])
    vessel_dict["Celiac"].add_recipient(vessel_dict["Splenic"])
    vessel_dict["L common iliac"].add_recipient(vessel_dict["L external iliac"])
    vessel_dict["L common iliac"].add_recipient(vessel_dict["L internal iliac"])
    vessel_dict["R common iliac"].add_recipient(vessel_dict["R external iliac"])
    vessel_dict["R common iliac"].add_recipient(vessel_dict["R internal iliac"])
    vessel_dict["L external iliac"].add_recipient(vessel_dict["L femoral"])
    vessel_dict["R external iliac"].add_recipient(vessel_dict["R femoral"])
    vessel_dict["L femoral"].add_recipient(vessel_dict["L profunda femoris"])
    vessel_dict["L femoral"].add_recipient(vessel_dict["L popliteal"])
    vessel_dict["R femoral"].add_recipient(vessel_dict["R profunda femoris"])
    vessel_dict["R femoral"].add_recipient(vessel_dict["R popliteal"])
    vessel_dict["L popliteal"].add_recipient(vessel_dict["L peroneal"])
    vessel_dict["R popliteal"].add_recipient(vessel_dict["R peroneal"])
    vessel_dict["L popliteal"].add_recipient(vessel_dict["L posterior tibial"])
    vessel_dict["R popliteal"].add_recipient(vessel_dict["R posterior tibial"])
    vessel_dict["L popliteal"].add_recipient(vessel_dict["L anterior tibial"])
    vessel_dict["R popliteal"].add_recipient(vessel_dict["R anterior tibial"])
    vessel_dict["L anterior tibial"].add_recipient(vessel_dict["L dorsalis pedis"])
    vessel_dict["R anterior tibial"].add_recipient(vessel_dict["R dorsalis pedis"])
    return vessel_dict
