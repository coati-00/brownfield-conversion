from django.db import models


LOCATION_SITES = (
    ('BX', 'BTEX Gas Station'),
    ('FF', 'Firn Freeze'),
    ('KB', 'Kilroy\'s Bar'),
    ('PS', 'Plucker\'s Scrap Metal'),
    ('RM', 'Roche Mountonee Vineyard'),
    ('SL', 'Self-Lume Factory'),
    ('TD', 'Tillies All-Night Diner'),
    ('WN', 'Wedging Nursery'),
    ('MG', 'Municipal Government'),
    ('TW', 'Town Well'),
    ('WT', 'Water Tower'),
    ('EA', 'Eolian Acres'),
    ('FH', 'Fallow Home'),
    ('FE', 'Four Homes on Erratic'),
    ('KK', 'Kame Kondos'),
)

TEST_TYPE = (
    ('DRP', 'Drilling/Push'),
    ('EXC', 'Excavation'),
    ('MMD', 'MMD'),
    ('SGS', 'SGSA'),
    ('SRR', 'SRR'),
    ('TPS', 'Topographic Survey'),
    ('SPT', 'Super Test'),
)


# Create your models here.
class VisualRecon(models.Model):
    location = models.CharField(max_length=255)
    site_order = models.IntegerField(default=1)
    image = models.CharField(max_length=255)
    text = models.TextField(default='')

    class Meta:
        ordering = ['site_order']

    def __unicode__(self):
        return str(self.site_order) + " " + self.location

class SiteHistory(models.Model):
    location_name = models.CharField(max_length=255)
    site_history = models.TextField(default='')
    # image_1 = models.ImageField(default='')
    # image_2 = models.ImageField(default='')

class PeopleSiteHistory(models.Model):
    location = models.ForeignKey(SiteHistory, null=True, blank=True)
    name = models.CharField(max_length=255)

class Interview(models.Model):
    person = models.ForeignKey(PeopleSiteHistory, null=True, blank=True)
    question = models.CharField(max_length=255)
    answer = models.TextField(default='')

class Testing(models.Model):
    test_type = models.CharField(max_length=3, choices=TEST_TYPE, unique=True)
    test_background = models.TextField(default='')
    location_name = models.CharField(max_length=255)
    site_history = models.TextField(default='')
    # image_1 = models.ImageField(default='')
    # image_2 = models.ImageField(default='')
