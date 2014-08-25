from django.db import models

SITE_TYPE = (
    ('CM', 'Commercial'),
    ('GV', 'Government'),
    ('RS', 'Residential'),
)

COMMERCIAL_SITES = (
    ('BX', 'BTEX Gas Station'),
    ('FF', 'Firn Freeze'),
    ('KB', 'Kilroy\'s Bar'),
    ('PS', 'Plucker\'s Scrap Metal'),
    ('RM', 'Roche Mountonee Vineyard'),
    ('SL', 'Self-Lume Factory'),
    ('TD', 'Tillies All-Night Diner'),
    ('WN', 'Wedging Nursery'),
)
GOVERNMENT_SITES = (
    ('MG', 'Municipal Government'),
    ('TW', 'Town Well'),
    ('WT', 'Water Tower'),
)
RESIDENTIAL_SITES = (
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

PEOPLE_INTERVIEW = (
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
    site_order = models.IntegerField(default=1)
    image = models.ImageField(default='')
    text = models.TextField(default='')

class SiteHistory(models.Model):
    location_name = models.CharField(default='')
    site_history = models.TextField(default='')
    image_1 = models.ImageField(default='')
    image_2 = models.ImageField(default='')

class Testing(models.Model):
    test_type = models.CharField(max_length=3, choices=TEST_TYPE, unique=True)
    test_background = models.TextField(default='')
    location_name = models.CharField(default='')
    site_history = models.TextField(default='')
    image_1 = models.ImageField(default='')
    image_2 = models.ImageField(default='')
