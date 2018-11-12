class TestLogin():

    def setup(self):
        print("前")
        assert 1

    def teardown(self):
        print("后")
        assert 0

    def test_a(self):
        print("你好")
        assert 1

    def test_b(self):
        print("世界")
        assert 0
