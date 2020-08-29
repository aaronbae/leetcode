class Solution(object):
  def dayOfYear(self, date):
    import datetime
    x, y, z = [ int(x) for x in date.split("-")]
    a = datetime.datetime(x, y, z)
    b = datetime.datetime(x, 1, 1)
    return (a-b).days + 1

a = Solution()
print(a.dayOfYear("2019-01-09"))