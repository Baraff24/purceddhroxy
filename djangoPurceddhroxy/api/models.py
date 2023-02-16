from django.db import models


class Filter(models.Model):
    """Model definition for Filter."""
    name = models.CharField(max_length=255)
    function = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Filter."""

        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def __str__(self):
        """Unicode's representation of Filter."""
        return self.name


class Packet(models.Model):
    """Model definition for Packet."""
    packet = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Packet."""

        verbose_name = 'Packet'
        verbose_name_plural = 'Packets'

    def __str__(self):
        """Unicode's representation of Packet."""
        return self.packet