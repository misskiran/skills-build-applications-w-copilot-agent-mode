from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='thundergod', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='metalgeek', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='zerocool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='crashoverride', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='sleeptoken', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        for user in users:
            team1.members.add(user)
            team2.members.add(user)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=60, date='2025-05-30T08:00:00Z'),
            Activity(_id=ObjectId(), user=users[1], type='Crossfit', duration=120, date='2025-05-30T09:00:00Z'),
            Activity(_id=ObjectId(), user=users[2], type='Running', duration=90, date='2025-05-30T10:00:00Z'),
            Activity(_id=ObjectId(), user=users[3], type='Strength', duration=30, date='2025-05-30T11:00:00Z'),
            Activity(_id=ObjectId(), user=users[4], type='Swimming', duration=75, date='2025-05-30T12:00:00Z'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team1, points=100),
            Leaderboard(_id=ObjectId(), team=team2, points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0], description='Cycling Training', date='2025-05-30T08:00:00Z'),
            Workout(_id=ObjectId(), user=users[1], description='Crossfit', date='2025-05-30T09:00:00Z'),
            Workout(_id=ObjectId(), user=users[2], description='Running Training', date='2025-05-30T10:00:00Z'),
            Workout(_id=ObjectId(), user=users[3], description='Strength Training', date='2025-05-30T11:00:00Z'),
            Workout(_id=ObjectId(), user=users[4], description='Swimming Training', date='2025-05-30T12:00:00Z'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
