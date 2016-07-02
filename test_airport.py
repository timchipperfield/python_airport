import unittest
execfile('/Users/timchipperfield/projects/python_airport/airport.py')
execfile('/Users/timchipperfield/projects/python_airport/plane.py')


def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test_check_airport_exists(self):
        self.assertTrue(Airport)
    def test_check_plane_exists(self):
        self.assertTrue(Plane)
    def test_starts_in_air(self):
        plane = Plane
        self.assertEqual(plane.location, "in air", "the plane start in the air")
    def test_plane_lands(self):
        plane = Plane()
        airport = Airport()
        plane.land(airport)
        self.assertEqual(plane.location, "on ground", "the plane is on the ground after landing")
    def test_plane_at_airport(self):
        plane = Plane()
        airport = Airport()
        plane.land(airport)
        self.assertEqual(airport.plane_roster, [plane], "the plane is in the airport")
    def test_plane_takes_off(self):
        plane = Plane()
        airport = Airport()
        airport.plane_roster = []
        plane.land(airport)
        plane.takeoff(airport)
        print airport.plane_roster
        self.assertEqual(airport.plane_roster, [], "no planes in airport")
        self.assertEqual(plane.location, "in air", "the plane is in the air")
unittest.main()
