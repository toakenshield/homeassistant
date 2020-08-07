today = datetime.datetime.now().date()

name = data.get('name')
type = data.get('type')
sensorName = "sensor.{}_{}".format(type , name.replace(" " , "_"))

dateStr = data.get('date')
dateSplit = dateStr.split("-")

dateDay = int(dateSplit[2])
dateMonth = int(dateSplit[1])
dateYear =  int(dateSplit[0])
date = datetime.date(dateYear,dateMonth,dateDay)

thisYear = today.year
nextOccur = datetime.date(dateYear , dateMonth , dateDay)

numberOfDays = 0
years = int(thisYear) - dateYear


if today < nextOccur:
  numberOfDays = (nextOccur - today).days

elif today > nextOccur:
  nextOccur = datetime.date(dateYear , dateMonth , dateDay)
  numberOfDays = int((nextOccur - today).days)
  years = years+1


hass.states.set(sensorName , numberOfDays ,
  {
    "icon" : "mdi:calendar-star" ,
    "unit_of_measurement" : "dager" ,
    "friendly_name" : "Frist EU-kontroll {}".format(name) ,
#    "years" : years
  }
)
