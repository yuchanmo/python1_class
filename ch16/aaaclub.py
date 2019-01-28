class AAAClub:
    club_name = "American Auto Association"

    def __init__(self,name,num):
        self.name =name
        self.member_id = num


John = AAAClub('john',123)
BOb = AAAClub('Bob',124)

print(AAAClub.club_name)
print(John.club_name)
print(BOb.club_name)

John.club_name = 'hoohoo'
print(AAAClub.club_name)
print(John.club_name)
print(BOb.club_name)


AAAClub.club_name = 'sdfsdf'
print(AAAClub.club_name)
print(John.club_name)
print(BOb.club_name)
