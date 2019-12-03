# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.



class Soldier:
    def __init__(self, soldier):
        self.soldier = soldier

    def desc(self):
        print('{} fire:'.format(self.soldier))

class Gun(Soldier):
    def __init__(self, name):
        self.name = name
        self.bullets = 30

    def fire(self):
        for i in range(1, self.bullets +1):
            print('tigi-tish',i)
            if i == self.bullets:
                print('You must reload')

ryan = Soldier('Ryan')
ryan.desc()
type_of_gun = Gun('AK-47')
type_of_gun.bullets = 15
type_of_gun.fire()

