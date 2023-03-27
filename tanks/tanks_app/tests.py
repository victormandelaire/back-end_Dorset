from django.test import TestCase
from .models import Tank

class TankModelTestCase(TestCase):
    def setUp(self):
        self.tank = Tank.objects.create(
            tankname='T-34', nationality='Soviet Union',
            crewmates_num=4, turret=True
        )

    def test_tank_string_representation(self):
        self.assertEqual(str(self.tank), "T-34 (Soviet Union)")

    def test_tank_has_required_fields(self):
        self.assertIsNotNone(self.tank.tankname)
        self.assertIsNotNone(self.tank.nationality)
        self.assertIsNotNone(self.tank.crewmates_num)
        self.assertIsNotNone(self.tank.turret)

    def test_tank_creation(self):
        initial_tanks_count = Tank.objects.count()
        Tank.objects.create(
            tankname='Panzer IV', nationality='Germany',
            crewmates_num=5, turret=True
        )
        self.assertEqual(Tank.objects.count(), initial_tanks_count + 1)

    def test_tank_update(self):
        self.tank.tankname = "KV-1"
        self.tank.save()
        updated_tank = Tank.objects.get(id=self.tank.id)
        self.assertEqual(updated_tank.tankname, "KV-1")

    def test_tank_deletion(self):
        initial_tanks_count = Tank.objects.count()
        self.tank.delete()
        self.assertEqual(Tank.objects.count(), initial_tanks_count - 1)
