from convert_hex_to_dec import convert_hex_to_dec
def compute_time_interval(myhex):
    """
    Input - myhex - string
    Output - time_interval in ns- float
    each hex represents number of ticks
    each tick is about 80 ns
    """
    number_of_ticks = convert_hex_to_dec(myhex)
    time_interval = number_of_ticks * 80.
    return time_interval


if __name__ == "__main__":
    test_hex = '03'
    print("Time interval for {}: {} ns"
          .format(test_hex, compute_time_interval(test_hex)))
