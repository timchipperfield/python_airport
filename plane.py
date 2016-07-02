class Plane:
    location = 'in air'
    def land(self, airport):
        self.location = 'on ground'
        airport.plane_roster.append(self)
    def takeoff(self, airport):
        self.location = 'in air'
        airport.plane_roster.remove(self)
