from django.db import models

class Team(models.Model):
    team_id = models.IntegerField(db_column='id', primary_key=True)
    city = models.CharField(max_length=13)
    full_name = models.CharField(db_column='fullName', max_length=22)
    nick_name = models.CharField(db_column='nickName', max_length=13)
    logo = models.CharField(max_length=138)
    short_name = models.CharField(db_column='shortName', max_length=3)
    conf_name = models.CharField(db_column='confName', max_length=4)
    div_name = models.CharField(db_column='divName', max_length=9)

    def __str__(self):
        return self.full_name
    
    class Meta:
        managed = False
        db_table = 'teams'

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(db_column='firstName', max_length=12)
    last_name = models.CharField(db_column='lastName', max_length=18, blank=True, null=True)
    team = models.ForeignKey(Team, db_column='teamId', on_delete=models.CASCADE)
    years_pro = models.IntegerField(db_column='yearsPro')
    college_name = models.CharField(db_column='collegeName', max_length=34, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)
    affiliation = models.CharField(max_length=50, blank=True, null=True)
    height_in_meters = models.DecimalField(db_column='heightInMeters', max_digits=4, decimal_places=2, blank=True, null=True)
    weight_in_kilograms = models.DecimalField(db_column='weightInKilograms', max_digits=5, decimal_places=1, blank=True, null=True)
    pos = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = False
        db_table = 'players'

class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away')
    date_time = models.CharField(max_length=50)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

class Standing(models.Model):
    team = models.OneToOneField(Team, primary_key=True, on_delete=models.CASCADE)
    win = models.IntegerField()
    loss = models.IntegerField()
    conference = models.CharField(max_length=4)
    conference_rank = models.IntegerField()
    division = models.CharField(max_length=20)
    division_rank = models.IntegerField()
