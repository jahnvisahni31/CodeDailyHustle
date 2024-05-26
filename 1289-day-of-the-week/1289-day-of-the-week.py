class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dat = datetime.date(year, month, day)
        da_ind = dat.weekday()
        return d[da_ind]