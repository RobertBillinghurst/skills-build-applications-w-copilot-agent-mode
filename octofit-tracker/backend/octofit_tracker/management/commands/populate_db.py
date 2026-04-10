from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

from octofit_tracker.models import Team, Activity, LeaderboardEntry, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
        ]

        # Create Activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            Activity.objects.create(user=users[1], type='cycle', duration=45, distance=20),
            Activity.objects.create(user=users[2], type='swim', duration=60, distance=2),
            Activity.objects.create(user=users[3], type='walk', duration=90, distance=8),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Morning Cardio', description='A quick morning run', suggested_for='Marvel'),
            Workout.objects.create(name='Strength Training', description='Heavy lifting', suggested_for='DC'),
        ]

        # Create Leaderboard
        LeaderboardEntry.objects.create(user=users[0], points=100)
        LeaderboardEntry.objects.create(user=users[1], points=80)
        LeaderboardEntry.objects.create(user=users[2], points=120)
        LeaderboardEntry.objects.create(user=users[3], points=110)


        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))

# Models assumed to exist: Team, Activity, LeaderboardEntry, Workout
# If not, they must be created in octofit_tracker/models.py
