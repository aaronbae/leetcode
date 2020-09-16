DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

import datetime
def find_day_of_week(date):
  [day, month, year] = map(lambda x: int(x), date.split("/"))
  return datetime.datetime(year, month, day)

def recurringTask(firstDate, k, daysOfTheWeek, n):
  ref_day = find_day_of_week(firstDate)
  ref_day_weekday = ref_day.weekday()
  days_to_add = [DAYS.index(x)-ref_day_weekday if DAYS.index(x)>=ref_day_weekday else 7-ref_day_weekday+DAYS.index(x) for x in daysOfTheWeek]
  days_to_add = sorted(days_to_add)
  result = []
  day_index = 0
  while len(result) < n:
    result.append((ref_day+datetime.timedelta(days=days_to_add[day_index])).strftime("%d/%m/%Y"))
    day_index += 1
    if day_index >= len(days_to_add):
      day_index = 0
      ref_day += datetime.timedelta(weeks=k)
  return result

print(recurringTask("01/01/2015", 2, ["Monday", "Thursday"], 4))