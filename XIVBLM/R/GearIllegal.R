Gear_Illegal<-function(MateriaFrame,Gearset){
  Judge<-MateriaFrame[Gearset,c('Name','Unique')]
  Jury<-which(duplicated(Judge))
  return(any(Judge[Jury,"Unique"]))
}
