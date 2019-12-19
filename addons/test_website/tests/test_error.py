import coffice.tests
from coffice.tools import mute_logger


@coffice.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(coffice.tests.HttpCase):

    @mute_logger('coffice.addons.http_routing.models.ir_http', 'coffice.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
