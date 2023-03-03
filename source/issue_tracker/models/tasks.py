from django.db import models


class Task(models.Model):
    summary = models.CharField(
        max_length=100,
        verbose_name='Краткое описание'
    )

    description = models.TextField(
        null=True, blank=True,
        verbose_name='Полное описание'
    )

    status = models.ForeignKey(
        to='issue_tracker.Status',
        on_delete=models.RESTRICT,
        related_name='statuses',
        verbose_name='Статус'
    )

    type = models.ForeignKey(
        to='issue_tracker.Type',
        on_delete=models.RESTRICT,
        verbose_name='Тип'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время и дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время и дата обновления'
    )

    def __str__(self):
        return self.summary
