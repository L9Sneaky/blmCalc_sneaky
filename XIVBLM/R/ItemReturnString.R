ItemReturnString<-function(MateriaFrame,EquipmentIndex){
  return(paste(sep='',
               MateriaFrame$Name[EquipmentIndex],' (',MateriaFrame$Materia[EquipmentIndex],')'))
}
