from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "check_pangram"
    FUNCTION_NAMES = {
        "python_3": "check_pangram",
        "js_node": "checkPangram"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''def cover(f, data):
    return f(str(data))
'''
    }