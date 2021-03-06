from django.db import models


class PickValue(models.Model):
    draft_round = models.IntegerField()
    round_pick = models.IntegerField()
    overall_pick = models.IntegerField()
    trade_value = models.IntegerField()


class Trade(models.Model):
    team_a = models.CharField(max_length=3)
    team_a_gets = models.CharField(max_length=255)
    team_b = models.CharField(max_length=3)
    team_b_gets = models.CharField(max_length=255)
    grade = models.CharField(max_length=100)


class TeamPick(models.Model):
    year = models.IntegerField()
    team = models.CharField(max_length=3)
    draft_round = models.IntegerField()
    round_pick = models.IntegerField()
    overall_pick = models.IntegerField()
    selection = models.CharField
    

class CombineResult(models.Model):
    year = models.IntegerField()
    player_name = models.CharField(max_length=256)
    combine_id = models.CharField(max_length=4)
    position = models.CharField(max_length=3)
    player_school = models.CharField(max_length=256)
    draft_age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    arm_length = models.IntegerField()
    hand_size = models.IntegerField()
    wingspan = models.IntegerField()
    forty_yd_dash = models.IntegerField()
    twenty_yd_forty_split = models.IntegerField()
    ten_yd_forty_split = models.IntegerField()
    shuttle = models.IntegerField()
    three_cone = models.IntegerField()
    bench_press = models.IntegerField()
    vertical = models.IntegerField()
    broad_jump = models.IntegerField()


class SparqResult(models.Model):
    year = models.IntegerField()
    position_rank = models.IntegerField()
    player_name = models.CharField(max_length=256)
    combine_id = models.CharField(max_length=4)
    position = models.CharField(max_length=3)
    player_school = models.CharField(max_length=256)
    draft_age = models.IntegerField()
    psparq = models.IntegerField()
    z_score = models.IntegerField()
    nfl_percentile = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    arm_length = models.IntegerField()
    hand_size = models.IntegerField()
    wingspan = models.IntegerField()
    forty_yd_dash = models.IntegerField()
    twenty_yd_forty_split = models.IntegerField()
    ten_yd_forty_split = models.IntegerField()
    shuttle = models.IntegerField()
    three_cone = models.IntegerField()
    bench_press = models.IntegerField()
    vertical = models.IntegerField()
    broad_jump = models.IntegerField()