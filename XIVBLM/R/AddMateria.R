MateriaAddFrame<-function(GearPiece){
  Columns<-colnames(GearPiece)
  MateriaIDCols<-grep('Materia',Columns)
  MValue<-as.numeric(GearPiece[MateriaIDCols])

  GearPiece<-GearPiece[,-MateriaIDCols]
  stats<-Columns[-c(MateriaIDCols)]

  stats<-stats[!stats %in% c('Slot','Idx','Ilvl','StatCap','Name','Unique','WD','Int')]
  numstats<-length(stats)
  rm(Columns,MateriaIDCols)

  MateriaBase<-cbind.data.frame(Materia=stats,diag(0,numstats,numstats))
  colnames(MateriaBase)<-c("Materia",stats)
  MateriaBase$Materia<-""

  #Generate Materia Combinations. TECH DEBT, ASSUMES DPS ROLE
  for(MateriaValue in MValue){
    if(MateriaValue>0){
      TEMP<-cbind.data.frame(Materia=stats,diag(MateriaValue,4,4))
      colnames(TEMP)<-c("Materia",stats)
      TEMP<-merge(x=TEMP,y=MateriaBase,by=NULL)
      MateriaBase<-cbind.data.frame(Materia=paste(TEMP$Materia.y,TEMP$Materia.x,sep='+'),
                                    DH=TEMP$DH.x+TEMP$DH.y,
                                    Crit=TEMP$Crit.x+TEMP$Crit.y,
                                    Det=TEMP$Det.x+TEMP$Det.y,
                                    SS=TEMP$SS.x+TEMP$SS.y,
                                    stringsAsFactors = FALSE)

      rm(TEMP)
    }
  }
  MateriaBase<-MateriaBase[!duplicated(MateriaBase[,2:(1+numstats)]),]
  rownames(MateriaBase)<-1:nrow(MateriaBase)
  MateriaBase$Materia<-substr(MateriaBase$Materia,2,nchar(MateriaBase$Materia))
  rm(MateriaValue)

  GearPieceWithMateria<-merge(x=GearPiece,y=MateriaBase,by=NULL)
  StatCap<-GearPieceWithMateria$StatCap

  for (stat in stats){
    PartialStatColumns<-grep(stat,colnames(GearPieceWithMateria))
      X<-min(PartialStatColumns)
      Y<-max(PartialStatColumns)
    GearPieceWithMateria[,X]<-rowSums(GearPieceWithMateria[PartialStatColumns])
    GearPieceWithMateria[,X]<-pmin(StatCap,GearPieceWithMateria[,X])
    GearPieceWithMateria[,Y]<-NULL
    colnames(GearPieceWithMateria)[X]<-stat
  }
ReturnVectorOrder<-c('Slot','Name','Materia','Unique','WD','Int',stats)
GearPieceWithMateria<-GearPieceWithMateria[,ReturnVectorOrder]
return(GearPieceWithMateria)
}



