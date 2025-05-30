
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

CODESPACE_URL = "https://miniature-guacamole-p5p64q4wjxqh757g-8000.app.github.dev"
LOCAL_URL = "http://localhost:8000"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "codespace_url": f"{CODESPACE_URL}/api/users/",
            "local_url": f"{LOCAL_URL}/api/users/",
            "results": response.data
        }
        return response

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "codespace_url": f"{CODESPACE_URL}/api/teams/",
            "local_url": f"{LOCAL_URL}/api/teams/",
            "results": response.data
        }
        return response

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "codespace_url": f"{CODESPACE_URL}/api/activity/",
            "local_url": f"{LOCAL_URL}/api/activity/",
            "results": response.data
        }
        return response

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "codespace_url": f"{CODESPACE_URL}/api/leaderboard/",
            "local_url": f"{LOCAL_URL}/api/leaderboard/",
            "results": response.data
        }
        return response

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "codespace_url": f"{CODESPACE_URL}/api/workouts/",
            "local_url": f"{LOCAL_URL}/api/workouts/",
            "results": response.data
        }
        return response
