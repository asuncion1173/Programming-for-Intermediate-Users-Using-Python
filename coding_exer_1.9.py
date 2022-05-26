class ClubMembers:
    def __init__(self, name, birthday, age, favorite, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite = favorite
        self.goal = goal

    def display1(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite Food: ", self.favorite)
        print("Goal: ", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite, goal)

    def display2(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite Food: ", self.favorite)
        print("Goal: ", self.goal)
        print("Position: ", self.position)

m_1 = ClubMembers("Tom", 'January 16', 14, 'Ice Cream', 'To be happy')
o_4 = ClubOfficers("Vera", "June 22", 16, 'Beef strogranoff', "To be the world's greatest chef", "Treasurer")

m_1.display1()
o_4.display2()