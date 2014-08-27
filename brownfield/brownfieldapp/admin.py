from django.contrib import admin
from brownfieldapp.models import VisualRecon, \
    SiteHistory, PeopleSiteHistory, Interview, Testing

admin.site.register(VisualRecon)
admin.site.register(SiteHistory)
admin.site.register(PeopleSiteHistory)
admin.site.register(Interview)
admin.site.register(Testing)
