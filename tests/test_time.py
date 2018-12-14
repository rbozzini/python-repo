import utils.time


def test_print_time_hh_mm_ss():
    assert utils.time.print_time_hh_mm_ss(60788660) == "16:53:08"


