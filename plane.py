class Plane:
    location = 'in air'
    def land(self, airport):
        self.location = 'on ground'
        airport.plane_roster.append(self)
