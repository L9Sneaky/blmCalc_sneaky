MateriaFrameGenerate<-function(GearSetFilePath=file.choose()){
  print('Warning: You should see this message exactly ONCE')
  GearFrame<-Gearframe_Generate(GearSetFilePath)

  MateriaFrame<-data.frame()

  for(i in 1:nrow(GearFrame)){
    ItemToAdd<-MateriaAddFrame(GearFrame[i,])
    MateriaFrame<-rbind.data.frame(MateriaFrame,ItemToAdd)
  }

  MateriaFrame$Prune<-NA

  for(i in 1:nrow(MateriaFrame)){
    MateriaFrame$Prune[i]<-length(
      intersect(
        intersect(
          intersect(
            intersect(which(MateriaFrame$WD>=MateriaFrame$WD[i]),
                      which(MateriaFrame$Int>=MateriaFrame$Int[i])),
            intersect(which(MateriaFrame$Crit>=MateriaFrame$Crit[i]),
                      which(MateriaFrame$DH>=MateriaFrame$DH[i]))),
          intersect(which(MateriaFrame$Det>=MateriaFrame$Det[i]),
                    which(MateriaFrame$SS>=MateriaFrame$SS[i]))),
        which(MateriaFrame$Slot==MateriaFrame$Slot[i]))
      )
  }

  MateriaFrame<-MateriaFrame[MateriaFrame$Prune==1,]
  MateriaFrame$Prune<-NULL
  rownames(MateriaFrame)<-1:nrow(MateriaFrame)
  return(MateriaFrame)
}
