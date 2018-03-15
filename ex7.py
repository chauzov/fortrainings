# task: generate dates and time of your work shift via
# python datetime module
# print list of tuples in format (2018-01-20 10:40, 2018-01-20 21:30)

import datetime

startNightShift = datetime.time(21,30)
endNightShift = datetime.time(7,30)

startDayShift = datetime.time(11,40)
endDayShift = datetime.time(21,30)

nightShifts = (0,6)
dayShifts = (2,3)

now = datetime.date.today()
nextMonth = now.month + 1

# get last day of the current month
eom = datetime.date(now.year, nextMonth, 1) - datetime.timedelta(days = 1)
schedList = []


dayIter = now.day
while dayIter <= eom.day:
    iterDate = datetime.date(now.year, now.month, dayIter)

    if dayIter == eom.day:
        nextDate = datetime.date(now.year, now.month + 1, 1)
    else:
        nextDate = datetime.date(now.year, now.month, dayIter+ 1)

    iterDayOfWeek = iterDate.weekday()
    if iterDayOfWeek in nightShifts:
        sBegin = datetime.datetime.combine(iterDate, startNightShift)
        sEnd = datetime.datetime.combine(nextDate, endNightShift)
        sBeginStr = sBegin.isoformat(sep=' ')
        sEndStr = sEnd.isoformat(sep=' ')
        shift = (sBeginStr[:-3], sEndStr[:-3])
        schedList.append(shift)


    if iterDayOfWeek in dayShifts:
        sBegin = datetime.datetime.combine(iterDate, startDayShift)
        sEnd = datetime.datetime.combine(iterDate, endDayShift)
        sBeginStr = sBegin.isoformat(sep=' ')
        sEndStr = sEnd.isoformat(sep=' ')
        shift = (sBeginStr[:-3], sEndStr[:-3])
        schedList.append(shift)

    dayIter += 1

print "Shift schedule for this month:"

for d in schedList:
    print d
