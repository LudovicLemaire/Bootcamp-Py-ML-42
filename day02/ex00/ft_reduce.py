def ft_reduce(function_to_apply, list_of_inputs):
    r = list_of_inputs[0]
    for x in list_of_inputs[1:]:
        r = function_to_apply(r, x)
    return r
