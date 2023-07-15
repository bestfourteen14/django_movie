from django.db import models

# Create your models here.
class Movie(models.Model):
    title_kor = models.CharField(max_length=30)
    title_eng = models.TextField(default='')
    poster_url = models.URLField(max_length=1024)
    rating_aud = models.CharField(max_length=10)
    rating_cri = models.CharField(max_length=10)
    rating_net = models.CharField(max_length=10)
    genre = models.CharField(max_length=20)
    showtimes = models.CharField(max_length=30)
    release_date = models.TextField(default='')
    rate = models.CharField(max_length=20)
    summary = models.TextField(default='')

    def __str__(self):
        return self.title_kor

class Staff(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='staff')
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image_url = models.URLField(max_length=1024)

    def __str__(self):
        return self.name

# class Comment(models.Model):
#     post = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comments')
#     created_at = models.DateField(auto_now_add=True)
#     comment = models.TextField()

#     def __str__(self):
#         return self.comment