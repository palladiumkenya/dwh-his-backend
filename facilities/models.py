from django.db import models
import uuid
# Create your models here.



class Counties(models.Model):
    name = models.CharField(max_length=50)


class Sub_counties(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(Counties, on_delete=models.CASCADE)


class SDP_agencies(models.Model):
    name = models.CharField(max_length=50)


class Partners(models.Model):
    name = models.CharField(max_length=100)
    agency = models.ForeignKey(SDP_agencies, on_delete=models.CASCADE)


class EMR_type(models.Model):
    type = models.CharField(max_length=100)


class HTS_use_type(models.Model):
    hts_use_name = models.CharField(max_length=100)


class HTS_deployment_type(models.Model):
    deployment = models.CharField(max_length=100)


class Owner(models.Model):
    name = models.CharField(max_length=100)

class EMR_modules(models.Model):
    name = models.CharField(max_length=100)

class IL_modules(models.Model):
    name = models.CharField(max_length=100)


class Facility_Info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mfl_code = models.IntegerField()
    name = models.CharField(max_length=100)
    county = models.ForeignKey(Counties, on_delete=models.CASCADE)
    sub_county = models.ForeignKey(Sub_counties, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    #hts_use_and_deployment = models.ForeignKey(HTS_use_and_deployment, on_delete=models.CASCADE)
    #hts_info = models.ForeignKey(HTS_Info, on_delete=models.CASCADE)
    #il_info = models.ForeignKey(IL_Info, on_delete=models.CASCADE)
    #emr_info = models.ForeignKey(EMR_Info, on_delete=models.CASCADE)
    #mhealth_info = models.ForeignKey(MHealth_Info, on_delete=models.CASCADE)
    #implementation = models.DecimalField(max_digits=9, decimal_places=6)
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    #agency = models.ForeignKey(SDP_agencies, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class EMR_Info(models.Model):
    type = models.ForeignKey(EMR_type, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    ovc = models.CharField(max_length=10, default=None)
    otz = models.CharField(max_length=10, default=None)
    prep = models.CharField(max_length=10, default=None)
    tb = models.CharField(max_length=10, default=None)
    facility_info = models.ForeignKey(Facility_Info, on_delete=models.CASCADE)


class HTS_Info(models.Model):
    # if only two options are available (N/A or active), a Boolean field might be better
    status = models.CharField(max_length=100)
    hts_use_name = models.ForeignKey(HTS_use_type, on_delete=models.CASCADE)
    deployment = models.ForeignKey(HTS_deployment_type, on_delete=models.CASCADE)
    facility_info = models.ForeignKey(Facility_Info, on_delete=models.CASCADE)


class IL_Info(models.Model):
    # consider Boolean field
    status = models.CharField(max_length=100)
    registration_ie = models.CharField(max_length=10)
    pharmacy_ie = models.CharField(max_length=10)
    facility_info = models.ForeignKey(Facility_Info, on_delete=models.CASCADE)


class MHealth_Info(models.Model):
    # consider Boolean field
    #status = models.CharField(max_length=100)
    Ushauri = models.BooleanField(default=False)
    C4C = models.BooleanField(default=False)
    Nishauri = models.BooleanField(default=False)
    Mlab = models.BooleanField(default=False)
    ART_Directory = models.BooleanField(default=False)
    Psurvey = models.BooleanField(default=False)
    facility_info = models.ForeignKey(Facility_Info, on_delete=models.CASCADE)


class Implementation_type(models.Model):
    type = models.CharField(max_length=100)
    ct = models.BooleanField(default=False)
    hts = models.BooleanField(default=False)
    il = models.BooleanField(default=False)
    kp = models.BooleanField(default=False)
    facility_info = models.ForeignKey(Facility_Info, on_delete=models.CASCADE)





