from func_new_post import *


def test_step_1():
    assert new_posts() == (200, 'First post from API'), 'TEST new_post FAIL'
