BiSLoop<-function(MateriaFrame,Food,GearSet){
  MateriaFrame$DPS<-NA

  Temp = 1
  GearDPS = 0

  while(Temp>GearDPS){
      GearDPS<-as.numeric(Food.Apply(MateriaFrame,GearSet,Food)['DPS'])

        for(i in 1:nrow(MateriaFrame)){
        MateriaFrame$DPS[i]<-Gear_Replace_DPS(MateriaFrame,Food,GearSet,i)
        }
      Temp = max(MateriaFrame$DPS)
      print(Temp)

      NewPiece<-which(MateriaFrame$DPS==Temp)
      NewPiece<-NewPiece[sample(length(NewPiece),1)]
      GearSet<-Gear_Replace(MateriaFrame,Food,GearSet,NewPiece)
  }
  return(GearSet)
}
