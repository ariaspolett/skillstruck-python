#Checkpoint - 
class Vacation:
    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather
    
    def tuesday(self):
        print("We will be hiking on Tuesday")
summer = Vacation("Hawaii", 2000, "Sunny")
print(summer)
summer.rating = 10
print(summer.rating)
summer.weather = "rainy"
print(summer.weather)

#Challenge - Weekend
class Friday: 
    def __init__(self, activity, friend):
        self.activity = activity
        self.friend = friend
    def pictures(self):
        print("We took so many pictures!")
thisWeekend = Friday("Movie", "Charlotte")
thisWeekend.money = 20
thisWeekend.friend = "Shane"
print(thisWeekend)
print(thisWeekend.money)
print(thisWeekend.friend)

#Challenge - Shopping
class Shopping:
    def __init__(self, item, quality):
        self.item = item 
        self.quality = quality
        self.total = []
    def spending(self, cost):
        self.total.append(cost)
sportStore = Shopping("Kayak","High Quality")
sportStore.spending(235)
sportStore.spending(867)
sportStore.spending(536)
print(sportStore.total)