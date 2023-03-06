GearSetFrameGen<-function(MateriaFrame,GearSet){
  GearSetFrame<-MateriaFrame[GearSet,]
  BaseRow<-c(NA,'Base',NA,NA,0,447,400,400,390,400)
  GearSetFrame<-rbind.data.frame(GearSetFrame,BaseRow)
  rownames(GearSetFrame)<-1:nrow(GearSetFrame)
  return(GearSetFrame)
}
