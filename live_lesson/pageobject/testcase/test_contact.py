import pytest
import yaml

from live_lesson.pageobject.page.app import App


def get_data():
    with open('../data/data.yaml', encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        add_data = data['add']
        return add_data


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_data())
    def test_add_contact(self, name, gender, phonenum):
        toast = self.main.click_addresslist().add_member().addcontact_menual(). \
            edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save().get_toast()
        assert toast == '添加成功'
