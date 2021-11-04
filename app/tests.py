from django.test import TestCase
from app.models import Para
from app.models import Post
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self) -> None:
        Para.objects.create(content="I'm the first paragraph");
        Para.objects.create(content="This is the SECOND para");
        Para.objects.create(content="The third paragraph");
        Post.objects.create();

    def test_append_to_paragraph(self):
        p1 = Para.objects.get(pk=1);
        p2 = Para.objects.get(pk=2);
        p2.link_to(p1);
        self.assertEqual(p2.previous, p1);
        self.assertTrue(hasattr(p1, "next"));
        self.assertEqual(p1.next, p2);
    
    def test_insert_to_paragraph(self):
        p1 = Para.objects.get(pk=1);
        p2 = Para.objects.get(pk=2);
        p3 = Para.objects.get(pk=3);
        p3.link_to(predecessor=p1);
        p2.link_to(predecessor=p1);
        self.assertTrue(hasattr(p1, "next"));
        self.assertEqual(p1.next, p2);
        self.assertEqual(p2.previous, p1);
        self.assertEqual(p2.next, p3);
        self.assertEqual(p3.previous, p2);

    def test_append_to_post_header(self):
        post = Post.objects.get(pk=1);
        p1 = Para.objects.get(pk=1);
        p1.link_to(post=post);
        self.assertTrue(hasattr(p1, "of_post"));
        self.assertIsNotNone(post.index_para);
        self.assertTrue(post.index_para, p1);
        self.assertTrue(p1.of_post, post);
    
    def test_insert_to_post_header(self):
        post = Post.objects.get(pk=1);
        p1 = Para.objects.get(pk=1);
        p2 = Para.objects.get(pk=2);
        p1.link_to(post=post);
        p2.link_to(post=post); # should result in post-p1-p2;
        self.assertEqual(post.index_para, p2);
        self.assertEqual(p2.next, p1);
        self.assertTrue(p1.is_end());
    
    def test_delete_para(self):
        post = Post.objects.get(pk=1);
        p1 = Para.objects.get(pk=1);
        p1.link_to(post=post);
        self.assertTrue(p1.is_end());
        p1.delete();
        post = Post.objects.get(pk=1); # must re-query to get the right reference of object
        self.assertIsNone(post.index_para);
        
    def test_delete_para_after_header(self):
        post = Post.objects.get(pk=1);
        p1 = Para.objects.get(pk=1);
        p1.link_to(post=post);
        p2 = Para.objects.get(pk=2);
        p2.link_to(predecessor=p1);
        p1.delete_myself();
        post = Post.objects.get(pk=1);
        self.assertEqual(post.index_para, p2);
    
    def test_delete_middle_para(self):
        post = Post.objects.get(pk=1);
        p1 = Para.objects.get(pk=1);
        p1.link_to(post=post);
        p2 = Para.objects.get(pk=2);
        p2.link_to(predecessor=p1);
        p3 = Para.objects.get(pk=3);
        p3.link_to(predecessor=p2);
        p2.delete_myself();
        p1 = Para.objects.get(pk=1);
        p3 = Para.objects.get(pk=3);
        self.assertEqual(p1.next, p3);
        self.assertEqual(p3.previous, p1);