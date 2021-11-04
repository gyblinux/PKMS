from django.test import TestCase
from app.models import Para
# Create your tests here.
class ModelTest(TestCase):
    def test_linkedlist(self):
        p1 = Para.objects.create(content="I'm the first paragraph");
        p2 = Para.objects.create(content="This is the second paragraph");
        p2.previous = p1;
        p2.save();
        self.assertEqual(p1.next, p2);
        self.assertEqual(p2.previous, p1);
        
        