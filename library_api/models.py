from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.TextField(max_length=275)
    author = models.TextField(max_length=275)
    publication_date = models.DateTimeField()
    genre = models.TextField()
    featured = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book')
        ]


class BookTracker(BaseModel):
    WANT = 1
    READING = 2
    READ = 3
    STATUS = (
        (WANT,  ('Want to read')),
        (READING, ('Reading')),
        (READ, ('Read')),
        )
    user = models.ForeignKey('auth.User', related_name='book_tracker', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=WANT)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book', 'user'], name='unique_book_tracker')
        ]


class Note(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.TextField(max_length=300)
    public_status = models.BooleanField()
    page = models.IntegerField(null=True)
