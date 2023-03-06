PPSTable<-read.csv('Tables\\PPSTable.csv')
save(PPSTable,file='data\\PPSTable.rda')

MainStatValues<-as.matrix(read.csv('Tables\\MainStatValues.csv',row.names = 1))
save(MainStatValues,file='data\\MainStatValues.rda')

SecondaryMinorValues<-as.matrix(read.csv('Tables\\SecondaryMinorValues.csv',row.names = 1))
save(SecondaryMinorValues,file='data\\SecondaryMinorValues.rda')

SecondaryStatCapValues<-as.matrix(read.csv('Tables\\SecondaryStatCapValues.csv',row.names = 1))
save(SecondaryStatCapValues,file='data\\SecondaryStatCapValues.rda')

WDValues<-as.matrix(read.csv('Tables\\WDValues.csv',row.names = 1))
save(WDValues,file='data\\WDValues.rda')

GearType<-read.csv('Tables\\GearType.csv')
save(GearType,file='data\\GearType.rda')

Menu<-read.csv('Tables\\Menu.csv')
save(Menu,file='data\\Menu.rda')
