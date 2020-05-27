from TinyStatistician import TinyStatistician
tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
b = [10, 20, 30, 40]

print("\x1b[1;35;40ma: \x1b[0m{}".format(a))
print("\x1b[1;35;40mb: \x1b[0m{}".format(b))

print("\n\x1b[1;34;40mMean\x1b[0m")
print("\x1b[1;36;40ma: \x1b[0m{}".format(tstat.mean(a)))
print("\x1b[1;36;40mb: \x1b[0m{}".format(tstat.mean(b)))

print("\n\x1b[1;34;40mMedian\x1b[0m")
print("\x1b[1;36;40ma: \x1b[0m{}".format(tstat.median(a)))
print("\x1b[1;36;40mb: \x1b[0m{}".format(tstat.median(b)))

print("\n\x1b[1;34;40mQuartile\x1b[0m")
p = 25
print("\x1b[1;36;40ma[{}%]: \x1b[0m{}".format(p, tstat.quartile(a, p)))
print("\x1b[1;36;40mb[{}%]: \x1b[0m{}".format(p, tstat.quartile(b, p)))
p = 75
print("\n\x1b[1;36;40ma[{}%]: \x1b[0m{}".format(p, tstat.quartile(a, p)))
print("\x1b[1;36;40mb[{}%]: \x1b[0m{}".format(p, tstat.quartile(b, p)))
p = 34
print("\n\x1b[1;36;40ma[{}%]: \x1b[0m{}".format(p, tstat.quartile(a, p)))
print("\x1b[1;36;40mb[{}%]: \x1b[0m{}".format(p, tstat.quartile(b, p)))

print("\n\x1b[1;34;40mPopulation Variance\x1b[0m")
print("\x1b[1;36;40ma: \x1b[0m{}".format(tstat.var(a)))
print("\x1b[1;36;40mb: \x1b[0m{}".format(tstat.var(b)))

print("\n\x1b[1;34;40mSample Standard Deviation\x1b[0m")
print("\x1b[1;36;40ma: \x1b[0m{}".format(tstat.std(a)))
print("\x1b[1;36;40mb: \x1b[0m{}".format(tstat.std(b)))