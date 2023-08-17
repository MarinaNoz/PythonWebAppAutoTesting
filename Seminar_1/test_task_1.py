from func_task_1 import *


def test_step_1(incorrect_word, correct_word):
    assert correct_word in check_text(incorrect_word), 'TEST 1 FAIL'
