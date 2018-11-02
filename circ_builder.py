import organelles


#  Artery Info
#  missing arms


def build_network():
    vessel_dict = {"Heart": organelles.Heart([(265, 265)]),
                   "Aortic arch": organelles.BloodVessel(0.03, [(265, 215)]),
                   "Brachiocephalic": organelles.BloodVessel(0.012, [(245, 205)]),
                   "R common carotid": organelles.BloodVessel(0.006, [(225, 160)]),
                   "R Internal carotid": organelles.BloodVessel(0.001, [(221, 98)]),
                   "R External carotid": organelles.BloodVessel(0.001, [(208, 85)]),
                   "R subclavian": organelles.BloodVessel(0.025, [(185, 205)]),
                   "L common carotid": organelles.BloodVessel(0.006, []),
                   "L Internal carotid": organelles.BloodVessel(0.001, []),
                   "L External carotid": organelles.BloodVessel(0.001, []),
                   "L subclavian": organelles.BloodVessel(0.025, []),
                   "Vertebral artery": organelles.BloodVessel(0.004, [(250, 160)]),
                   "R Int. thoracic": organelles.BloodVessel(0.03, [(225, 235)]),
                   "L Int. thoracic": organelles.BloodVessel(0.03, []),
                   "R Thyrocervical trunk": organelles.BloodVessel(0.001, [(220, 178)]),
                   "R Costocervical trunk": organelles.BloodVessel(0.006, [(205, 180)]),
                   "L Thyrocervical trunk": organelles.BloodVessel(0.001, []),
                   "L Costocervical trunk": organelles.BloodVessel(0.006, []),
                   "R Dorsal scapular artery": organelles.BloodVessel(0.002, [(197, 187)]),
                   "L Dorsal scapular artery": organelles.BloodVessel(0.002, []),
                   "Descending Aorta": organelles.BloodVessel(0.015, [(262, 320)]),
                   "R Bronchial": organelles.BloodVessel(0.0015, [(225, 250)]),
                   "L Bronchial": organelles.BloodVessel(0.0015, []),
                   "Abdominal aorta": organelles.BloodVessel(0.02, [(262, 385)]),
                   "Celiac": organelles.BloodVessel(0.0078, [(261, 338)]),
                   "L Gastric": organelles.BloodVessel(0.0038, [(239, 343)]),
                   "Common hepatic": organelles.BloodVessel(0.004, [(239, 339)]),
                   "Splenic": organelles.BloodVessel(0.0061, [(289, 334)]),
                   "SMA": organelles.BloodVessel(0.08, [(281, 381)]),
                   "Renal": organelles.BloodVessel(0.0055, [(241, 368)]),
                   "IMA": organelles.BloodVessel(0.04, [(251, 410)]),
                   "L common iliac": organelles.BloodVessel(0.012, []),
                   "R common iliac": organelles.BloodVessel(0.013, [(235, 445)]),
                   "L external iliac": organelles.BloodVessel(0.01, []),
                   "L internal iliac": organelles.BloodVessel(0.006, []),
                   "L femoral": organelles.BloodVessel(0.01, []),
                   "L profunda femoris": organelles.BloodVessel(0.006, []),
                   "L popliteal": organelles.BloodVessel(0.009, []),
                   "L peroneal": organelles.BloodVessel(0.0015, []),
                   "L anterior tibial": organelles.BloodVessel(0.0028, []),
                   "L posterior tibial": organelles.BloodVessel(0.0019, []),
                   "L dorsalis pedis": organelles.BloodVessel(0.0033, []),
                   "R external iliac": organelles.BloodVessel(0.01, [(206, 502)]),
                   "R internal iliac": organelles.BloodVessel(0.006, [(239, 461)]),
                   "R femoral": organelles.BloodVessel(0.01, [(201, 636)]),
                   "R profunda femoris": organelles.BloodVessel(0.006, [(206, 503)]),
                   "R popliteal": organelles.BloodVessel(0.009, [(189, 694)]),
                   "R peroneal": organelles.BloodVessel(0.0015, [(176, 813)]),
                   "R anterior tibial": organelles.BloodVessel(0.0028, [(183, 826)]),
                   "R posterior tibial": organelles.BloodVessel(0.0019, [(166, 822)]),
                   "R dorsalis pedis": organelles.BloodVessel(0.0033, [(155, 961)])}
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
    vessel_dict["L subclavian"].add_recipient(vessel_dict["Vertebral artery"])
    vessel_dict["L subclavian"].add_recipient(vessel_dict["L Int. thoracic"])
    vessel_dict["R subclavian"].add_recipient(vessel_dict["R Int. thoracic"])
    vessel_dict["L subclavian"].add_recipient(vessel_dict["L Thyrocervical trunk"])
    vessel_dict["L subclavian"].add_recipient(vessel_dict["L Costocervical trunk"])
    vessel_dict["L subclavian"].add_recipient(vessel_dict["L Dorsal scapular artery"])
    vessel_dict["R subclavian"].add_recipient(vessel_dict["R Thyrocervical trunk"])
    vessel_dict["R subclavian"].add_recipient(vessel_dict["R Costocervical trunk"])
    vessel_dict["R subclavian"].add_recipient(vessel_dict["R Dorsal scapular artery"])
    vessel_dict["Descending Aorta"].add_recipient(vessel_dict["R Bronchial"])
    vessel_dict["Descending Aorta"].add_recipient(vessel_dict["L Bronchial"])
    vessel_dict["Descending Aorta"].add_recipient(vessel_dict["Abdominal aorta"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["Celiac"])
    vessel_dict["Abdominal aorta"].add_recipient(vessel_dict["Renal"])
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
