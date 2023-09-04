import pytest
import yaml

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)
    login = testdata['username']



@pytest.fixture()
def sel_1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def btn_selector():
    return 'button'


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def result():
    return '401'


@pytest.fixture()
def auth():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def result2():
    return f'Hello, {login}'


@pytest.fixture()
def create_btn_selector():
    return '#create-btn'


@pytest.fixture()
def title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def create():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""


@pytest.fixture()
def get_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""