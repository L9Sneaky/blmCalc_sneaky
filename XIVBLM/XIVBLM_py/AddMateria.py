import pandas as pd
import numpy as np

# def materia_add_frame(gear_piece):
#     columns = gear_piece.columns
#     materia_id_cols = [i for i, col in enumerate(columns) if 'Materia' in col]
#     m_value = gear_piece.iloc[:, materia_id_cols].astype('float').values.squeeze()

#     gear_piece = gear_piece.drop(columns=columns[materia_id_cols])
#     stats = [col for col in columns if col not in ['Slot', 'Idx', 'Ilvl', 'StatCap', 'Name', 'Unique', 'WD', 'Int', 'Materia']]

#     materia_base = pd.DataFrame(np.zeros((len(stats), len(stats))), columns=stats)
#     materia_base.index = pd.Index(stats, name='Materia')
#     materia_base.index.name = None

#     # Generate Materia Combinations. TECH DEBT, ASSUMES DPS ROLE
#     for materia_value in m_value:
#         if materia_value > 0:
#             temp = pd.DataFrame(np.diag(materia_value * np.ones(4)), columns=stats)
#             temp['Materia'] = stats
#             temp = temp.merge(materia_base.reset_index(), how='inner', on=None)

#             materia_base = pd.DataFrame({
#                 'Materia': [f'+{r["Materia_x"]}_{r["Materia_y"]}' for _, r in temp.iterrows()],
#                 'DH': temp['DH_x'] + temp['DH_y'],
#                 'Crit': temp['Crit_x'] + temp['Crit_y'],
#                 'Det': temp['Det_x'] + temp['Det_y'],
#                 'SS': temp['SS_x'] + temp['SS_y']
#             })

#     materia_base = materia_base.drop_duplicates(subset=stats).reset_index(drop=True)
#     materia_base['Materia'] = materia_base['Materia'].str.slice(1)
#     gear_piece_with_materia = gear_piece.merge(materia_base, how='inner', on=None)
#     stat_cap = gear_piece_with_materia['StatCap']

#     for stat in stats:
#         partial_stat_columns = [i for i, col in enumerate(gear_piece_with_materia.columns) if stat in col]
#         x = min(partial_stat_columns)
#         y = max(partial_stat_columns)
#         gear_piece_with_materia.iloc[:, x] = gear_piece_with_materia.iloc[:, partial_stat_columns].sum(axis=1)
#         gear_piece_with_materia.iloc[:, x] = np.minimum(stat_cap, gear_piece_with_materia.iloc[:, x])
#         gear_piece_with_materia = gear_piece_with_materia.drop(columns=gear_piece_with_materia.columns[partial_stat_columns[1:]])
#         gear_piece_with_materia = gear_piece_with_materia.rename(columns={gear_piece_with_materia.columns[x]: stat})

#     return_vector_order = ['Slot', 'Name', 'Materia', 'Unique', 'WD', 'Int'] + stats
#     return gear_piece_with_materia[return_vector_order]


def MateriaAddFrame(GearPiece):
    Columns = GearPiece.columns.tolist()
    MateriaIDCols = [col for col in Columns if 'Materia' in col]
    MValue = GearPiece[MateriaIDCols].values.astype(np.float).flatten()

    GearPiece = GearPiece.drop(columns=MateriaIDCols)
    stats = [col for col in Columns if col not in ['Slot', 'Idx', 'Ilvl', 'StatCap', 'Name', 'Unique', 'WD', 'Int', *MateriaIDCols]]
    numstats = len(stats)

    MateriaBase = pd.DataFrame({'Materia': stats})
    MateriaBase[stats] = np.diag(np.zeros(numstats))
    MateriaBase['Materia'] = ""

    # Generate Materia Combinations. TECH DEBT, ASSUMES DPS ROLE
    for MateriaValue in MValue:
        if MateriaValue > 0:
            TEMP = pd.DataFrame({'Materia': stats})
            TEMP[stats] = np.diag(np.ones(4) * MateriaValue)
            TEMP.loc[:, 'Materia'] = stats
            TEMP = pd.merge(TEMP.assign(key=1), MateriaBase.assign(key=1), on='key', how='outer').drop('key', axis=1)
            # TEMP = TEMP+MateriaBase
            MateriaBase = pd.DataFrame({
                'Materia': [s1+'+'+s2 for s1, s2 in zip(TEMP['Materia_y'], TEMP['Materia_x'])],
                'DH': TEMP['DH_x']+TEMP['DH_y'],
                'Crit': TEMP['Crit_x']+TEMP['Crit_y'],
                'Det': TEMP['Det_x']+TEMP['Det_y'],
                'SS': TEMP['SS_x']+TEMP['SS_y']
            })

    MateriaBase = MateriaBase.loc[~MateriaBase.iloc[:, 1:].duplicated(), :]
    MateriaBase.index = np.arange(1, len(MateriaBase)+1)
    MateriaBase['Materia'] = MateriaBase['Materia'].str[1:]

    GearPieceWithMateria = pd.merge(GearPiece.assign(key=1), MateriaBase.assign(key=1), on='key', how='outer').drop('key', axis=1)
    StatCap = GearPieceWithMateria['StatCap']

    for stat in stats:
        PartialStatColumns = [col for col in GearPieceWithMateria.columns if stat in col]
        X, Y = PartialStatColumns[0], PartialStatColumns[-1]
        GearPieceWithMateria[X] = GearPieceWithMateria[PartialStatColumns].sum(axis=1)
        GearPieceWithMateria[X] = np.minimum(StatCap, GearPieceWithMateria[X])
        GearPieceWithMateria = GearPieceWithMateria.drop(PartialStatColumns[1:-1], axis=1)
        GearPieceWithMateria = GearPieceWithMateria.rename(columns={X: stat})

    ReturnVectorOrder = ['Slot', 'Name', 'Materia', 'Unique', 'WD', 'Int', *stats]
    GearPieceWithMateria = GearPieceWithMateria.loc[:, ReturnVectorOrder]

    return GearPieceWithMateria
