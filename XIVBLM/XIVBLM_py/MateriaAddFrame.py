import pandas as pd
import numpy as np

def MateriaAddFrame(GearPiece):
    Columns = GearPiece.tolist()
    MateriaIDCols = [i for i in range(len(Columns)) if isinstance(Columns[i], str) and 'Materia' in Columns[i]]

    MValue = GearPiece.iloc[:, MateriaIDCols].values.astype(int)

    GearPiece = GearPiece.drop(columns=Columns[MateriaIDCols])
    stats = [s for s in Columns if s not in ['Slot', 'Idx', 'Ilvl', 'StatCap', 'Name', 'Unique', 'WD', 'Int']]
    numstats = len(stats)

    MateriaBase = pd.DataFrame(data=np.zeros((numstats, numstats)), columns=stats)
    MateriaBase['Materia'] = ''

    for MateriaValue in MValue.flatten():
        if MateriaValue > 0:
            TEMP = pd.DataFrame(data=MateriaValue * np.identity(4), columns=stats)
            TEMP['Materia'] = '+'.join(stats)
            TEMP = pd.merge(TEMP, MateriaBase, on=None)
            MateriaBase = pd.concat([MateriaBase, pd.DataFrame({
                'Materia': [s[1:] for s in TEMP['Materia_x']],
                'DH': TEMP['DH_x'] + TEMP['DH_y'],
                'Crit': TEMP['Crit_x'] + TEMP['Crit_y'],
                'Det': TEMP['Det_x'] + TEMP['Det_y'],
                'SS': TEMP['SS_x'] + TEMP['SS_y']
            })], ignore_index=True)

    MateriaBase.drop_duplicates(subset=stats, inplace=True)
    MateriaBase.index = range(1, len(MateriaBase)+1)
    MateriaBase['Materia'] = MateriaBase['Materia'].str[1:]

    GearPieceWithMateria = pd.merge(GearPiece, MateriaBase, on=None)
    StatCap = GearPieceWithMateria['StatCap']

    for stat in stats:
        PartialStatColumns = [i for i in range(len(GearPieceWithMateria.columns)) if stat in GearPieceWithMateria.columns[i]]
        X, Y = min(PartialStatColumns), max(PartialStatColumns)
        GearPieceWithMateria.iloc[:, X] = GearPieceWithMateria.iloc[:, PartialStatColumns].sum(axis=1)
        GearPieceWithMateria.iloc[:, X] = np.minimum(StatCap, GearPieceWithMateria.iloc[:, X])
        GearPieceWithMateria.drop(GearPieceWithMateria.columns[PartialStatColumns[1:]], axis=1, inplace=True)
        GearPieceWithMateria.rename(columns={GearPieceWithMateria.columns[X]: stat}, inplace=True)

    ReturnVectorOrder = ['Slot', 'Name', 'Materia', 'Unique', 'WD', 'Int'] + stats
    GearPieceWithMateria = GearPieceWithMateria[ReturnVectorOrder]
    return GearPieceWithMateria
