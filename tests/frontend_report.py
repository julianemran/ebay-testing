import os
import pytest
import allure
import conftest


class FrontendReport:

    @pytest.fixture(scope="function", autouse=True)
    def log_report(self, page, request, pytestconfig):
        tests_failed_before_module = request.session.testsfailed
        yield "test"
        tests_failed_during_module = request.session.testsfailed - tests_failed_before_module
        console_log_path = conftest.get_console_logs(page.browser, request)
        if tests_failed_during_module > 0:
            if conftest.is_browser_open(page.browser):
                test_name = request.node.name.replace("/", "_").replace("[", "_").replace("]", "_").replace(".", "_")
                test_name = test_name[:50]  # to take only the first 50 character for long test names
                file_name = f"screenshots/{test_name}.png"
                if not os.path.exists(file_name):
                    page.browser.save_screenshot(file_name)
                if pytestconfig.option.allure_report_dir:
                    allure.attach.file(file_name,
                                       f"{test_name}_screenshot.png", attachment_type=allure.attachment_type.PNG)
                    if console_log_path:
                        allure.attach.file(console_log_path,
                                           f"{test_name}_Console", attachment_type=allure.attachment_type.TEXT)

