import uuid
import bcrypt

from django.db import models

from .choices import (
    CATEGORY_CHOICES,
    MEDIA_TYPE_CHOICES,
    PLATFORM_CHOICES,
    STATUS_CHOICES
)


class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    password = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("-created_at",)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt())
        self.password = self.password.decode("utf-8")
        super().save(*args, **kwargs)


class LoanerModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=25, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "loaner"
        verbose_name_plural = "loaners"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
    

class ItemImageModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.URLField(max_length=250, blank=True, null=True)
    label = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        ordering = ("-created_at",)


class ItemModel(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    image = models.ForeignKey(ItemImageModel, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    main_actor = models.CharField(max_length=150, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    platform = models.CharField(max_length=150, choices=PLATFORM_CHOICES, blank=True, null=True, default=None)
    category = models.CharField(max_length=150, choices=CATEGORY_CHOICES, blank=True, null=True, default=None)
    media_type = models.CharField(max_length=150, choices=MEDIA_TYPE_CHOICES, blank=True, null=True, default=None)
    launch_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, blank=True, null=True, default="available")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class LoanModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    loaner = models.ForeignKey(LoanerModel, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "loan"
        verbose_name_plural = "loans"

    def __str__(self):
        return self.item

    def save(self, *args, **kwargs):
        if self.item.status != "not_available":
            self.item.status = "not_available"
            self.item.save()
        super().save(*args, **kwargs)
    

class LoanHistoryModel(models.Model):
    loan = models.ForeignKey(LoanModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "history"
        ordering = ("-loan",)
