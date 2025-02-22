from django.db import models


class Inverter1Data(models.Model):
    # Holding registers as floating-point numbers
    holding_reg1 = models.FloatField(default=0.0)
    holding_reg2 = models.FloatField(default=0.0)
    holding_reg3 = models.FloatField(default=0.0)
    holding_reg4 = models.FloatField(default=0.0)
    holding_reg5 = models.FloatField(default=0.0)
    holding_reg6 = models.FloatField(default=0.0)
    holding_reg7 = models.FloatField(default=0.0)
    holding_reg8 = models.FloatField(default=0.0)
    holding_reg9 = models.FloatField(default=0.0)
    holding_reg10 = models.FloatField(default=0.0)
    holding_reg11 = models.FloatField(default=0.0)
    holding_reg12 = models.FloatField(default=0.0)

    # Add a timestamp field
    last_updated = models.DateTimeField(auto_now_add=True)

