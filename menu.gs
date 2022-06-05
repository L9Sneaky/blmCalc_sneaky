function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Gear Calculator')
      //.addItem('Run Calculations', 'sheetCalc')
      .addItem('Create Statistics', 'sheetStats')
      .addItem('Reset Calculations', 'sheetReset')
      .addItem('Clear Gear Sheet', 'clearData')
      .addItem('Clear Stat Sheet', 'clearStatsData')
      .addToUi();
}

/**
* Clears out data and resets sheet
*/
function clearData() {

  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  if (sheet =! ss.getSheetByName("Readme")) {
    sheet.getRange("A3:H30").clearContent()
  }
}

/**
* Clears out data and resets sheet
*/
function clearStatsData() {

  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("Statistics");

  sheet.getRange("A3:G30").clearContent();
}

//reseting calculations
function sheetReset() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  var inputRange = sheet.getRange("S3:U30");
  var formulas = inputRange.getFormulas();
  var values = inputRange.getValues();
  inputRange.clearContent();
  inputRange.setValues(values)
  SpreadsheetApp.flush();
  inputRange.setValues(formulas)
}
/*
//Grab the data and run the calculation
function sheetCalc() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();

  //skips, ticks, cuts config
  var configValues = sheet.getRange("W2:Y2").getValues();
  var probSheet = ss.getSheetByName("prob");

  //give the config stuff a name
  var ticks = configValues[0][0]
  var skips = configValues[0][1]
  var cuts = configValues[0][2]

  // [WD, INT, DH, Crit, Det, SS]
  var inputValues = sheet.getRange("C3:H30").getValues();

  //avg Reshreshs for sharp Any
  var avgRefresh = probSheet.getRange("T2").getValues();

  var outputRange = sheet.getRange("Q3:R30");
  var outputValues = []
  //loop over all
  try {
    for (var n = 0; n < sheet.getRange("C3:H30").getHeight(); n++) {
      var SpS = inputValues[n][5]
      if (isNaN(parseInt(SpS))) {
        outputValues.push(['','']);
        continue;
      }
      //sharp Thunder
      var sharpF = (70 + 390 * 1.32 + 40 * SpsScalar(SpS) * (8 - 3/10 * Math.pow((9/10),5)-ticks)*2.32 +(newHRCTimeThunder(newR(avgThunderCycle(SpS,0.1),true))-(0.1+(GcdCalc(2500,SpS,true)+2*GcdCalc(2500,SpS,false))/3)*2.32)*ThunderP(SpS, 0.1))/(newHRCTimeThunder(newR(avgThunderCycle(SpS,0.1),true)))
      //sharp Any
      var sharpT = ((70 + 390 * avgRefresh[0][0] + 40 * SpsScalar(SpS) * ((8 - 3/10*Math.pow((9/10),5)-ticks)*2.32+(6.76-ticks)*(avgRefresh[0][0] + 1 - 2.32))) + (newHRCTimeAny(newR(avgAnyCycle(SpS,0.1,skips, cuts),false))-(0.1+(GcdCalc(2500,SpS,true)+2*GcdCalc(2500,SpS,false))/3)*(avgRefresh+1))*AnyP(SpS, 0.1, skips, cuts))/(newHRCTimeAny(newR(avgAnyCycle(SpS,0.1,skips, cuts),false)))
      outputValues.push([sharpF,sharpT])
    }
    outputRange.setValues(outputValues);
  }
  catch(e) {
    Browser.msgBox("error")
  }
}*/

function sheetStats() {

  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  var statsSheet = ss.getSheetByName("Statistics");
  var probSheet = ss.getSheetByName("prob");

  //grab all the data
  var gearDesc = sheet.getRange("A3:A").getValues();
  var gearStats = sheet.getRange("C3:H30").getValues();
  var configValues = sheet.getRange("Z2:Z10").getValues();
  var sharpFireMeanDps = sheet.getRange("U3:U").getValues();
  var sharpThunderMeanDps = sheet.getRange("V3:V").getValues();
  var sharpFireMeanPps = sheet.getRange("S3:S").getValues();
  var sharpThunderMeanPps = sheet.getRange("T3:T").getValues();

  //give the config stuff a name
  var hasBrd = configValues[2][0]
  var hasDrg = configValues[3][0]
  var hasSch = configValues[4][0]
  var hasDnc = configValues[5][0]
  var classNum = configValues[8][0]

  //parse into stats sheet
  statsSheet.getRange("A3:A").setValues(gearDesc);
  statsSheet.getRange("B3:B").setValues(sharpFireMeanDps);
  statsSheet.getRange("C3:C").setValues(sharpThunderMeanDps);
  //variance
  var sigmaRange = statsSheet.getRange("D3:E30");
  var sigmaValues = [];
  //total spread
  var errorRange = statsSheet.getRange("F3:G30");
  var errorValues = [];
  //loop over all
  try {
    for (var n = 0; n < sheet.getRange("C3:H30").getHeight(); n++) {
      var WD = gearStats[n][0]
      var INT = gearStats[n][1]
      var DH = gearStats[n][2]
      var Crit = gearStats[n][3]
      Logger.log(Crit)
      var Det = gearStats[n][4]
      var SpS = gearStats[n][5]
      if (isNaN(parseInt(SpS))) {
        sigmaValues.push(['','']);
        errorValues.push(['','']);
        continue;
      }
      //sharp Fire
      var sharpFvar = DamageVariance(sharpFireMeanPps[n][0], WD, 115, INT,Det, Crit, DH, 400, 400, hasBrd, hasDrg, hasSch, hasDnc, classNum)-(sharpFireMeanDps[n]*sharpFireMeanDps[n])

      //sharp Thunder
      var sharpTvar = DamageVariance(sharpThunderMeanPps[n][0], WD, 115, INT,Det, Crit, DH, 400, 400, hasBrd, hasDrg, hasSch, hasDnc, classNum)-(sharpThunderMeanDps[n]*sharpThunderMeanDps[n])
      sigmaValues.push([
        Math.sqrt(sharpFvar/59),
        Math.sqrt(sharpTvar/59),
      ])
      //~59 casts over 120s
      //Var(XY) = Var(X)Var(Y) + (E(X)^2)Var(Y) + (E(Y)^2)Var(X)
      var FireSpread = Math.round(Math.sqrt(((Math.pow(0.1,2))/12*sharpFvar+sharpFvar+(Math.pow(0.1,2))/12*(sharpFireMeanDps[n]*sharpFireMeanDps[n]))/59))
      var ThunderSpread = Math.round(Math.sqrt(((Math.pow(0.1+1,2)-1)/12*sharpTvar+sharpTvar+(Math.pow(0.1,2))/12*(sharpThunderMeanDps[n]*sharpThunderMeanDps[n]))/59))

      errorValues.push([
        FireSpread,
        ThunderSpread,
      ])
    }
    sigmaRange.setValues(sigmaValues);
    errorRange.setValues(errorValues);
  }
  catch(e) {
    Browser.msgBox("error")
  }
}  
