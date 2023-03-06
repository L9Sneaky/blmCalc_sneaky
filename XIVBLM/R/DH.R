DHRate<-function(DirectHit=400)
{
  return (floor(550*(DirectHit-400)/1900)/1000)
}

DH_DPS<-function(DirectHit=400){
  return(1+DHRate(DirectHit)/4)
}
