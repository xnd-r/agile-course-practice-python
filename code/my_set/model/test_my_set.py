import unittest

from my_set.model.my_set import MySet


class TestSetClass(unittest.TestCase):
    def test_can_init_with_default_constructor(self):
        test_set = MySet()
        self.assertTrue(isinstance(test_set, MySet))

    def test_can_get_size_of_set(self):
        test_set = MySet([1, 2, 5])
        size = test_set.get_size()
        self.assertEqual(size, 3)

    def test_can_init_with_init_constructor(self):
        test_list_of_elements = [1, 2, 3, 5, 7]
        test_set = MySet(test_list_of_elements)
        self.assertEqual(test_set.get_size(), 5)

    def test_set_with_size_0_is_empty(self):
        test_set = MySet()
        result = test_set.is_empty()
        self.assertTrue(result)

    def test_set_with_some_elements_is_not_empty(self):
        test_set = MySet([1, 2, 4, 5])
        result = test_set.is_empty()
        self.assertFalse(result)

    def test_can_check_element_contain(self):
        test_set = MySet([1, 2, 4, 5])
        element = 4
        result = element in test_set
        self.assertTrue(result)

    def test_can_check_element_not_contain(self):
        test_set = MySet([1, 2, 4, 5])
        element = 7
        result = element in test_set
        self.assertFalse(result)

    def test_can_add_new_element(self):
        test_set = MySet([1, 2, 4, 5])
        element = 7
        test_set.add(element)
        self.assertTrue(element in test_set)

    def test_dont_add_ununic_element(self):
        test_set = MySet([1, 2, 4, 5])
        element = 2
        test_set.add(element)
        self.assertEqual(test_set.get_size(), 4)

    def test_can_delete_element(self):
        test_set = MySet([1, 2, 4, 5])
        element = 1
        test_set.delete(element)
        self.assertFalse(element in test_set)

    def test_after_delete_size_became_less_on_one(self):
        test_set = MySet([1, 2, 4, 5])
        element = 2
        test_set.delete(element)
        self.assertEqual(test_set.get_size(), 3)
