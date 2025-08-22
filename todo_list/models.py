from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.Users", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
