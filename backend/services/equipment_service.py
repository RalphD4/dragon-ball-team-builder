from data.database import EQUIPMENTS

# ---------- SORT by rarity
def sorted_by_eqRarity(equips, rarity):
    return sorted(equips, key=lambda e: e.rarity_rank, reverse=True)



# --------- ADD / REMOVE
def add_equip(equip):
    if equip.name not in EQUIPMENTS_BY_NAME:
        EQUIPMENTS.append(equip)
        EQUIPMENTS_BY_NAME[equip.name] = equip
    else:
        raise Exception("Equip already exists")


def del_equip(name):
    if name not in EQUIPMENTS_BY_NAME:
        raise Exception("Equip does not exist")
    else:
        equip = EQUIPMENTS_BY_NAME.get(name)
        del EQUIPMENTS_BY_NAME[name]
        EQUIPMENTS.remove(equip)


EQUIPMENTS_BY_NAME = {equip.name: equip for equip in EQUIPMENTS}
