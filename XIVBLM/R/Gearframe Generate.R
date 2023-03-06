Gearframe_Generate<-function(InputSet,MajorMateriaValue=36,MinorMateriaValue=12){
  InputTable<-read.csv(InputSet)
  InputTable$StatCap<-0
  InputTable$WD<-0
  InputTable$Int<-0
  InputTable$DH<-0
  InputTable$Crit<-0
  InputTable$Det<-0
  InputTable$SS<-0
  InputTable$MateriaId1<-0
  InputTable$MateriaId2<-0
  InputTable$MateriaId3<-0
  InputTable$MateriaId4<-0
  InputTable$MateriaId5<-0

  MateriaRows<-grep('Materia',colnames(InputTable))

  GearFrame<-data.frame()
  Slots<-c("Weapon","Head","Chest","Hands","Legs","Feet","Ear","Neck","Wrist","Finger")

  for(Slot in Slots){
    StatType=GearType$Type[which(GearType$Slot==Slot)]

    Insert<-InputTable[which(InputTable$Slot==Slot),]

    N<-length(rownames(Insert))
    Insert$Idx<-1:N


    for(i in Insert$Idx){
      ilvl<-as.character(Insert$Ilvl[i])
      CapValue<-SecondaryStatCapValues[ilvl,StatType]
      Insert$StatCap[i]<-CapValue
      Insert$WD[i]<-WDValues[ilvl,StatType]
      Insert$Int[i]<-MainStatValues[ilvl,StatType]
      Insert[i,Insert$Primary[i]]<-CapValue
      Insert[i,Insert$Secondary[i]]<-SecondaryMinorValues[ilvl,StatType]

      if(Insert$Overmeld[i]){
          MajorMeldRows<-MateriaRows[1:(Insert$Meld.Slots[i]+1)]
          Insert[i,MajorMeldRows]<-MajorMateriaValue
          Insert[i,MateriaRows[(Insert$Meld.Slots[i]+2):5]]<-MinorMateriaValue
        } else {
          MajorMeldRows<-MateriaRows[1:Insert$Meld.Slots[i]]
          Insert[i,MajorMeldRows]<-MajorMateriaValue
        }
    }
    Insert<-Insert[,c('Slot','Idx','Ilvl','StatCap','Name','Unique',
                      'WD','Int','DH','Crit','Det','SS',
                      'MateriaId1','MateriaId2','MateriaId3','MateriaId4','MateriaId5')]
    GearFrame<-rbind.data.frame(GearFrame,Insert)
  }
rownames(GearFrame)<-1:length(GearFrame$Name)
return(GearFrame)
}
