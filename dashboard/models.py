
from django.db import models
from django.contrib.auth import get_user_model

class OrderQueue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=128)
    description = models.TextField()
    status = models.CharField(max_length=32, choices=[
        ('new', 'Новый'),
        ('design', 'Проектирование'),
        ('production', 'Производство'),
        ('ready', 'Готово'),
        ('shipped', 'Отгружено'),
    ], default='new')

    def __str__(self):
        return f"Заказ #{self.id} — {self.client}"

class KPIRecord(models.Model):
    timestamp = models.DateTimeField()
    metric = models.CharField(max_length=64)
    value = models.FloatField()

    class Meta:
        unique_together = ('timestamp', 'metric')

    def __str__(self):
        return f"{self.metric}: {self.value}"

class ShiftSchedule(models.Model):
    date = models.DateField()
    shift = models.CharField(max_length=16, choices=[('A','A'),('B','B'),('C','C')])
    planned = models.PositiveIntegerField()
    completed = models.PositiveIntegerField()

    class Meta:
        unique_together = ('date','shift')
        ordering = ['-date','shift']

    def __str__(self):
        return f"{self.date} — смена {self.shift}"

class AlertLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=16, choices=[('info','Info'),('warning','Warning'),('critical','Critical')])
    message = models.CharField(max_length=255)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.level}] {self.message[:50]}"

class Report(models.Model):
    generated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    file = models.FileField(upload_to='reports/')

    def __str__(self):
        return self.title
