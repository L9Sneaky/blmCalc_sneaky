Gear_Replace<-function(MateriaFrame,Food,GearSet,NewPiece){
  Slot<-MateriaFrame$Slot[NewPiece]
  if(Slot=="Finger"){
    Set1<-Set2<-GearSet

    Set1['Finger1']<-NewPiece
    Set1<-as.numeric(Food.Apply(MateriaFrame,Set1,Food)['DPS'])

    Set2['Finger2']<-NewPiece
    Set2<-as.numeric(Food.Apply(MateriaFrame,Set2,Food)['DPS'])

        if(Set1>Set2){
          GearSet['Finger1']<-NewPiece
          return(GearSet)
        } else {
          GearSet['Finger2']<-NewPiece
          return(GearSet)
        }

  } else {
      GearSet[Slot]<-NewPiece
      return(GearSet)
    }

}

Gear_Replace_DPS<-function(MateriaFrame,Food,GearSet,NewPiece){
  Slot<-MateriaFrame$Slot[NewPiece]
  if(Slot=="Finger"){
    Set1<-Set2<-GearSet

    Set1['Finger1']<-NewPiece
    Set1<-as.numeric(Food.Apply(MateriaFrame,Set1,Food)['DPS'])

    Set2['Finger2']<-NewPiece
    Set2<-as.numeric(Food.Apply(MateriaFrame,Set2,Food)['DPS'])

    if(Set1>Set2){
      GearSet['Finger1']<-NewPiece
    } else {
      GearSet['Finger2']<-NewPiece
    }

  } else {
    GearSet[Slot]<-NewPiece
  }
  return(as.numeric(Food.Apply(MateriaFrame,GearSet,Food)['DPS']))
}
