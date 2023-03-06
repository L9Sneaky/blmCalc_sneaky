import pandas as pd

def gearframe_generate(input_set, major_materia_value=36, minor_materia_value=12):
    input_table = pd.read_csv(input_set)
    input_table['StatCap'] = 0
    input_table['WD'] = 0
    input_table['Int'] = 0
    input_table['DH'] = 0
    input_table['Crit'] = 0
    input_table['Det'] = 0
    input_table['SS'] = 0
    input_table['MateriaId1'] = 0
    input_table['MateriaId2'] = 0
    input_table['MateriaId3'] = 0
    input_table['MateriaId4'] = 0
    input_table['MateriaId5'] = 0
    
    materia_rows = [col for col in input_table.columns if 'Materia' in col]
    
    gear_frame = pd.DataFrame()
    slots = ["Weapon", "Head", "Chest", "Hands", "Legs", "Feet", "Ear", "Neck", "Wrist", "Finger"]
    
    for slot in slots:
        stat_type = gear_type[gear_type["Slot"] == slot]["Type"].iloc[0]
        insert = input_table[input_table["Slot"] == slot]
        n = len(insert.index)
        insert["Idx"] = range(1, n + 1)
        
        for i in insert.index:
            ilvl = str(insert.loc[i, "Ilvl"])
            cap_value = secondary_stat_cap_values.loc[ilvl, stat_type]
            insert.loc[i, "StatCap"] = cap_value
            insert.loc[i, "WD"] = wd_values.loc[ilvl, stat_type]
            insert.loc[i, "Int"] = main_stat_values.loc[ilvl, stat_type]
            insert.loc[i, insert.loc[i, "Primary"]] = cap_value
            insert.loc[i, insert.loc[i, "Secondary"]] = secondary_minor_values.loc[ilvl, stat_type]
            
            if insert.loc[i, "Overmeld"]:
                major_meld_rows = materia_rows[: insert.loc[i, "Meld.Slots"] + 1]
                insert.loc[i, major_meld_rows] = major_materia_value
                insert.loc[i, materia_rows[insert.loc[i, "Meld.Slots"] + 2 : 5]] = minor_materia_value
            else:
                major_meld_rows = materia_rows[: insert.loc[i, "Meld.Slots"]]
                insert.loc[i, major_meld_rows] = major_materia_value
        
        insert = insert[
            [
                "Slot",
                "Idx",
                "Ilvl",
                "StatCap",
                "Name",
                "Unique",
                "WD",
                "Int",
                "DH",
                "Crit",
                "Det",
                "SS",
                "MateriaId1",
                "MateriaId2",
                "MateriaId3",
                "MateriaId4",
                "MateriaId5",
            ]
        ]
        
        gear_frame = pd.concat([gear_frame, insert])
        
    gear_frame.index = range(1, len(gear_frame.index) + 1)
    return gear_frame
