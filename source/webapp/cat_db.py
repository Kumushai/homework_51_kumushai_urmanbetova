class CatsDb:

    def __init__(self):
        self.name = ''
        self.age = 1
        self.happiness = 40
        self.satiety = 40
        self.cat_state = 'awake'
        self.img_path = ''
        self.get_img_path()

    def get_img_path(self):
        print(self.name)
        if self.happiness <= 40:
            self.img_path = "images/cat.jpeg"
        elif self.happiness <= 70:
            self.img_path = "images/play.jpeg"
        elif self.happiness <= 100:
            self.img_path = "images/sleep.jpeg"
