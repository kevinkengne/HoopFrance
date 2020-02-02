from django.db import models

class Team(models.Model):
    team_id = models.IntegerField(db_column='id', primary_key=True)
    city = models.CharField(max_length=13)
    full_name = models.CharField(db_column='fullName', max_length=22)  # Field name made lowercase.
    nick_name = models.CharField(db_column='nickName', max_length=13)  # Field name made lowercase.
    logo = models.CharField(max_length=138)
    short_name = models.CharField(db_column='shortName', max_length=3)  # Field name made lowercase.
    conf_name = models.CharField(db_column='confName', max_length=4)  # Field name made lowercase.
    div_name = models.CharField(db_column='divName', max_length=9)  # Field name made lowercase.

    def __str__(self):
        return self.full_name
    
    class Meta:
        managed = False
        db_table = 'teams'

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(db_column='firstName', max_length=12)  # Field name made lowercase.
    last_name = models.CharField(db_column='lastName', max_length=18, blank=True, null=True)  # Field name made lowercase.
    team = models.ForeignKey(Team, db_column='teamId', on_delete=models.CASCADE)  # Field name made lowercase.
    years_pro = models.IntegerField(db_column='yearsPro')  # Field name made lowercase.
    college_name = models.CharField(db_column='collegeName', max_length=34, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=32, blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    affiliation = models.CharField(max_length=50, blank=True, null=True)
    height_in_meters = models.DecimalField(db_column='heightInMeters', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    weight_in_kilograms = models.DecimalField(db_column='weightInKilograms', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = False
        db_table = 'players'