import pandas as pd
import numpy as np

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
