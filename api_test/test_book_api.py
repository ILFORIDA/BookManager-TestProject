import requests
import allure

@allure.feature("图书管理接口测试")
class TestBook:

    @allure.story("获取图书列表")
    def test_get_book_list(self, base_url):
        res = requests.get(f"{base_url}/posts")
        assert res.status_code == 200
        assert len(res.json()) > 0

    @allure.story("新增图书")
    def test_add_book(self, base_url):
        data = {
            "title": "Python软件测试实战",
            "body": "接口自动化项目",
            "userId": 1
        }
        res = requests.post(f"{base_url}/posts", json=data)
        assert res.status_code == 201
        assert res.json()["title"] == "Python软件测试实战"

    @allure.story("获取单本图书详情")
    def test_get_book_detail(self, base_url):
        res = requests.get(f"{base_url}/posts/2")
        assert res.status_code == 200

    @allure.story("修改图书信息")
    def test_update_book(self, base_url):
        data = {"title": "测试修改图书名称"}
        res = requests.put(f"{base_url}/posts/2", json=data)
        assert res.status_code == 200

    @allure.story("删除图书")
    def test_delete_book(self, base_url):
        res = requests.delete(f"{base_url}/posts/2")
        assert res.status_code == 200
