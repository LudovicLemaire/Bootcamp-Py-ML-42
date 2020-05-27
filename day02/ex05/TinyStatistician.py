class TinyStatistician:
    @staticmethod
    def mean(arr):
        return float(sum(e for e in arr) / len(arr))

    @staticmethod
    def median(arr):
        if len(arr) % 2 == 0:
            return TinyStatistician.mean([sorted(arr)[int(len(arr) / 2) - 1], sorted(arr)[int(len(arr) / 2)]])
        else:
            return float(sorted(arr)[int(len(arr) / 2)])

    @staticmethod
    def quartile(arr, quartile):
        arr = sorted(arr)
        percent = 100 / (len(arr) - 1.0)
        for i, v in enumerate(arr):
            if percent * (i + 1) == quartile:
                return float(arr[i + 1])
            if percent * (i + 1) > quartile:
                return TinyStatistician.median([arr[i], arr[i + 1]])

    @staticmethod
    def var(arr):
        return float(sum((e - TinyStatistician.mean(arr))**2 for e in arr) / len(arr))

    @staticmethod
    def std(arr):
        return float(TinyStatistician.var(arr)**(1/2))
