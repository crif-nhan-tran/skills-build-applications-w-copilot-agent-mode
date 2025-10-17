from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='TestTeam', members=['A', 'B'])
        self.assertEqual(team.name, 'TestTeam')
        self.assertEqual(team.members, ['A', 'B'])

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test', activity='Running', duration=10)
        self.assertEqual(activity.user, 'Test')
        self.assertEqual(activity.activity, 'Running')
        self.assertEqual(activity.duration, 10)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='TestTeam', points=100)
        self.assertEqual(lb.team, 'TestTeam')
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user='Test', workout='Pushups', reps=20)
        self.assertEqual(workout.user, 'Test')
        self.assertEqual(workout.workout, 'Pushups')
        self.assertEqual(workout.reps, 20)
