from django.db import models


CONTENT_LEN = 2**16
PREVIEW_LEN = 2**6
HEAD_LEN = 2**8
TAIL_LEN = 2**8


class Thing(models.Model):
    sha256 = models.CharField(max_length=64, primary_key=True)
    length = models.BigIntegerField(null=True, blank=True)
    full = models.BooleanField(default=False)

    content = models.BinaryField(max_length=CONTENT_LEN, null=True, blank=True)
    head = models.BinaryField(max_length=HEAD_LEN, null=True, blank=True)
    tail = models.BinaryField(max_length=TAIL_LEN, null=True, blank=True)
    preview = models.CharField(max_length=PREVIEW_LEN, blank=True)

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sha256[:8]

    @classmethod
    def add(cls, content):
        from hashlib import sha256
        digest = sha256(content).hexdigest()
        obj, _ = cls.objects.get_or_create(sha256=digest)

        obj.length = len(content)
        obj.full = len(content) <= CONTENT_LEN
        obj.content = content[:CONTENT_LEN]
        obj.head = content[:HEAD_LEN]
        obj.tail = content[-TAIL_LEN:]

        head_text = obj.head.decode(errors='replace')
        if len(head_text) > PREVIEW_LEN:
            obj.preview = head_text[:PREVIEW_LEN-1] + '…'
        else:
            obj.preview = head_text

        obj.save()

        return obj
