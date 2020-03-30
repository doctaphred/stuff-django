from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Empty user model, for ease of future customization.

    According to the Django docs, "If you're starting a new project,
    it's highly recommended to set up a custom user model, even if the
    default User model is sufficient for you."

    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
    #using-a-custom-user-model-when-starting-a-project
    """
    pass

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.get_username()
