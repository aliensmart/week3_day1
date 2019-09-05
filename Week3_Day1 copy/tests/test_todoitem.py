
# Write tests using the unittest module to test that our TodoItem class 
from unittest import TestCase
from app import TodoItem

class testApp(TestCase):

    def testTodoItem(self):
        item1 = TodoItem(title = "Do Hackerrank Problems", description = "Gotta keep up with these...", complete = 0)
        self.assertEqual(item1.title, "Do Hackerrank Problems")
        self.assertEqual(item1.description, "Gotta keep up with these...")
        self.assertEqual(item1.complete, 0)
        self.assertIsInstance(item1, TodoItem)

    def testSave(self):
        item2 = TodoItem(pk=1, title = "Do Hackerrank Problems", description = "Gotta keep up with these...", complete = 1)
        item2.save()
        self.assertEqual(item2.complete, 1)

    def testDelete(self):
        item2 = TodoItem(pk=1)
        item2.delete()
        self.assertEqual(item2.one_from_pk(1), None)
        self.assertNotEqual(item2.one_from_pk(3), None)

    def testOneFromPk(self):
         
        item = TodoItem().one_from_pk(3)
        self.assertEqual(item.title, "Get Lunch")
        self.assertEqual(item.pk, 3)
        self.assertEqual(item.description, "Why is everything so expensive around here?")
        self.assertEqual(item.complete, 1)

    def testAll(self):
        items = TodoItem().all()
        self.assertEqual(items[0].title, "Complete Homework")
        self.assertEqual(items[1].title, "Get Lunch")
        self.assertEqual(items[0].description, None)
        self.assertEqual(items[1].description, "Why is everything so expensive around here?")
        self.assertEqual(items[0].complete, 0)
        self.assertEqual(items[1].complete, 1)

        items = TodoItem().all(True)
        self.assertEqual(items[0].title, "Get Lunch")
        self.assertEqual(items[0].description, "Why is everything so expensive around here?")
        self.assertEqual(items[0].complete, 1)

        items = TodoItem().all(False)
        self.assertEqual(items[0].title, "Complete Homework")
        self.assertEqual(items[0].description, None)
        self.assertEqual(items[0].complete, 0)








    



