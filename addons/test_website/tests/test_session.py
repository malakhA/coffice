import coffice.tests
from coffice.tools import mute_logger


@coffice.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(coffice.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
