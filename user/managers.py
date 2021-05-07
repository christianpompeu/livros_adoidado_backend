from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email = self.normalize_email(email),
            name=name,
            surname=surname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, surname, email, password=None):
        user = self.create_user(
            name,
            surname,
            email, 
            password = password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user