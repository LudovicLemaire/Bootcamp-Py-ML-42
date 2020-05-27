from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce


def forMapFunc(arr):
    return arr[0] + arr[1] + arr[2]

def forFilterFunc(string):
    if len(string) > 13:
        return True
    else:
        return False

def do_mult(x1, x2): 
    return x1 * x2

print("\n\x1b[1;34;40mft_map\x1b[0m")
x = ft_map(forMapFunc, [('Ich', ' liebe', ' dich'), ('Ich', ' brauche', ' dich'), ('Gib', ' mir', ' mehr')])
print(list(x))

print("\n\x1b[1;34;40mft_filter\x1b[0m")
x = ft_filter(forFilterFunc, ("Komm, fütter' mich", "Allesfresser", "Ich liebe dich", "Gib mir mehr", "Ich brauch' dich sehr"))
print(list(x))

print("\n\x1b[1;34;40mft_reduce\x1b[0m")
x = ft_reduce(do_mult, [4, 2, 3, 4])
print(x)
