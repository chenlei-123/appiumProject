from hamcrest import assert_that, equal_to, close_to, contains_string


class TestHamcrest:
    def test_hamcrest(self):
        assert_that(10, equal_to(10), '这是一个提示')
        assert_that(12, close_to(10, 2), '这是一个提示')
        assert_that('contains some string', contains_string("string"))
