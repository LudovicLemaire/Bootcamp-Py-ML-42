def ft_filter(function_to_apply, list_of_inputs):
    return [x for x in list_of_inputs if function_to_apply(x)]
