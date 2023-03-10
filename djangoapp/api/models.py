from django.db import models


class Filter(models.Model):
    """Model definition for Filter."""
    name = models.CharField(max_length=255)
    function = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Filter."""
        app_label = 'api'
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def __str__(self):
        """Unicode's representation of Filter."""
        return self.name


class Packet(models.Model):
    """Model definition for Packet."""
    src_ip = models.CharField(max_length=17)
    dst_ip = models.CharField(max_length=17)
    type = models.CharField(max_length=5)
    payload = models.TextField()
    dangerous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Packet."""
        app_label = 'api'
        verbose_name = 'Packet'
        verbose_name_plural = 'Packets'

    def __str__(self):
        """Unicode's representation of Packet."""
        return self.src_ip + " -> " + self.dst_ip + " " + str(self.dangerous)
