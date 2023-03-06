import pandas as pd
import numpy as np

def materia_add_frame(gear_piece):
    columns = gear_piece.columns
    materia_id_cols = [i for i, col in enumerate(columns) if 'Materia' in col]
    m_value = gear_piece.iloc[:, materia_id_cols].astype('float').values.squeeze()

    gear_piece = gear_piece.drop(columns=columns[materia_id_cols])
    stats = [col for col in columns if col not in ['Slot', 'Idx', 'Ilvl', 'StatCap', 'Name', 'Unique', 'WD', 'Int', 'Materia']]

    materia_base = pd.DataFrame(np.zeros((len(stats), len(stats))), columns=stats)
    materia_base.index = pd.Index(stats, name='Materia')
    materia_base.index.name = None

    # Generate Materia Combinations. TECH DEBT, ASSUMES DPS ROLE
    for materia_value in m_value:
        if materia_value > 0:
            temp = pd.DataFrame(np.diag(materia_value * np.ones(4)), columns=stats)
            temp['Materia'] = stats
            temp = temp.merge(materia_base.reset_index(), how='inner', on=None)

            materia_base = pd.DataFrame({
                'Materia': [f'+{r["Materia_x"]}_{r["Materia_y"]}' for _, r in temp.iterrows()],
                'DH': temp['DH_x'] + temp['DH_y'],
                'Crit': temp['Crit_x'] + temp['Crit_y'],
                'Det': temp['Det_x'] + temp['Det_y'],
                'SS': temp['SS_x'] + temp['SS_y']
            })

    materia_base = materia_base.drop_duplicates(subset=stats).reset_index(drop=True)
    materia_base['Materia'] = materia_base['Materia'].str.slice(1)
    gear_piece_with_materia = gear_piece.merge(materia_base, how='inner', on=None)
    stat_cap = gear_piece_with_materia['StatCap']

    for stat in stats:
        partial_stat_columns = [i for i, col in enumerate(gear_piece_with_materia.columns) if stat in col]
        x = min(partial_stat_columns)
        y = max(partial_stat_columns)
        gear_piece_with_materia.iloc[:, x] = gear_piece_with_materia.iloc[:, partial_stat_columns].sum(axis=1)
        gear_piece_with_materia.iloc[:, x] = np.minimum(stat_cap, gear_piece_with_materia.iloc[:, x])
        gear_piece_with_materia = gear_piece_with_materia.drop(columns=gear_piece_with_materia.columns[partial_stat_columns[1:]])
        gear_piece_with_materia = gear_piece_with_materia.rename(columns={gear_piece_with_materia.columns[x]: stat})

    return_vector_order = ['Slot', 'Name', 'Materia', 'Unique', 'WD', 'Int'] + stats
    return gear_piece_with_materia[return_vector_order]
