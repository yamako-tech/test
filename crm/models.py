from django.db import models

# Show Messages on HomePage
class HomeMessage(models.Model):
    message = models.CharField(
        max_length=250, 
        null=False, 
        blank=False
    )
    is_published =  models.BooleanField('Published', default=True)
    start_date = models.DateField('From', blank=True, null=True)
    end_date = models.DateField('To', blank=True, null=True)

    def __str__(self):
        return self.message

    ## Verbose_name on the admin panel
    class Meta:
        verbose_name = "HomeMessage"
        verbose_name_plural = "HomeMessage"