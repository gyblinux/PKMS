from typing import List
from django.db import models
from django.conf import settings
from users.models import CustomUser

# Create your models here.
class Para(models.Model):
    para_id = models.AutoField(primary_key=True)
    content = models.TextField()
    previous = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, default=None, related_name="next")

    def is_end(self) -> bool:
        """checking if this paragraph is the last para in the linkedlist"""
        return not hasattr(self, "next")

    def is_linked(self) -> bool:
        """checking if this paragraph is appended to the linkedlist"""
        return self.previous is not None

    def link_to(self, predecessor: "Para" = None, post: "Post" = None) -> None:
        """append OR insert this para to another para, its predecessor"""
        # early return: must name either predecessor para or header post
        if (predecessor is None) and (post is None):
            raise Exception("Must name either a para or a post to complete the insertion")
        if (predecessor is not None) and (post is not None):
            raise Exception("Insertion Error: cannot insert the para to two different position")

        # to a paragraph
        if (predecessor is not None) and (post is None):
            # append to SLL
            if predecessor.is_end():
                self.previous = predecessor
                self.save()
            # insert to SLL
            else:
                predecessor.next.previous = self
                predecessor.next.save()
                self.previous = predecessor
                self.save()
        # to a post header
        elif (predecessor is None) and (post is not None):
            if post.index_para is not None:
                post.index_para.previous = self
                post.index_para.save()
            post.set_index_para(self)
    
    def delete_myself(self) -> None:
        """destruct this para and repair the SLL connections if there are any"""
        # delete from tail
        if self.is_end():
            self.delete()
        # delete with successor
        else:
            if hasattr(self, "of_post"):
                self.of_post.set_index_para(self.next)
            else:
                prev = self.previous
                temp = self.next
                self.delete()
                temp.previous = prev
                temp.save()

    def __str__(self) -> str:
        return self.content

class Post(models.Model):
    # PK
    post_id = models.AutoField(primary_key=True)
    # props
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    is_shared = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    post_title = models.CharField(max_length=50, default="Untitled")
    # header of SLL(single linked list)
    index_para = models.OneToOneField(Para, on_delete=models.SET_DEFAULT, null=True, default=None, related_name="of_post")

    def set_index_para(self, para: "Para") -> None:
        self.index_para = para
        self.save()

    def render_post(self) -> str:
        """render the entire post with linked-list paragraphs if there exsits any"""
        probe = self.index_para

        # early return with empty post
        if (probe is None): return "There are no contents in this post yet"
        
        # render all paragraphs with non-empty post
        content = ""
        while True:
            content += "%s\n" % probe
            if not probe.is_end(): probe = probe.next
            else: break
        return content

    def _render_paras_id(self) -> List[int]:
        probe = self.index_para
        para_ids: List[int] = []
        while (probe is not None) and (not probe.is_end()):
            para_ids.append(probe.para_id)
            probe = probe.next
        return para_ids

    @property
    def render_paras(self) -> List["Para"]:
        para_ids: List[int] = self._render_paras_id()
        paras: List["Para"] = []
        for id in para_ids:
            paras.append(Para.objects.get(pk=id))
        return paras

