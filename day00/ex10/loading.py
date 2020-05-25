import sys
import time


def ft_progress(lst):
    s = time.time()
    estimateTime = 0
    elapsedTime = 0
    size = 50
    file = sys.stdout
    count = len(lst)

    def show(j):
        x = int(size * j / count)
        p = int(j / count * 100)
        file.write("ETA: {:.1f}s \x1b[6;30;42m{}\x1b[6;30;47m{}\x1b[0m {}/{} [{:0>2d}%] | Elapsed time {:.1f}s\r".format(estimateTime / (j if j > 0 else 1) * (count - j), " " * x, " " * (size - x - 1), j, count, p, elapsedTime))
        file.flush()

    show(0)
    for i, item in enumerate(lst):
        yield item
        show(i + 1)
        e = time.time()
        estimateTime = e - s
        c = time.time()
        elapsedTime = c - s
