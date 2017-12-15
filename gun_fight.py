class Player:
    """创建一个玩家的类"""
    def __init__(self, model):
        self.model = model
        self.hp = 100
        self.gun_temp = None

    @staticmethod
    def load_bullet(clip_temp, bullet_temp):
        # 把子弹安装到弹夹里
        clip_temp.add_bullet(bullet_temp)

    @staticmethod
    def load_gun(gun_temp, clip_temp):
        # 把弹夹上到枪里
        gun_temp.add_clip(clip_temp)

    def take_gun(self, gun_temp):
        # 拿枪
        self.gun_temp = gun_temp

    def shoot(self, bandit):
        # 射击
        self.gun_temp.fire(bandit)

    def hurt(self, damage_num):
        # 造成伤害
        if self.hp > 0:
            self.hp -= damage_num

    def __str__(self):
        # 返回玩家信息
        if self.gun_temp:
            return "%s有枪,%s,血量为:%d" % (self.model, self.gun_temp, self.hp)
        else:
            if self.hp <= 0:
                return "%s血量为%d,已经挂了" % (self.model, self.hp)
            return "%s没枪,血量为:%d" % (self.model, self.hp)

class Gun:
    """创建一把枪的对象"""
    def __init__(self, model):
        self.model = model
        self.clip_temp = None

    def add_clip(self, clip_temp):
        # 把弹夹安到枪上面
        self.clip_temp = clip_temp

    def fire(self, bandit):
        # 开火
        bullet = self.clip_temp.reduce_bullet()
        if bullet:
            bullet.hit(bandit)
        else:
            print("%s没有子弹，没有击中敌人" % self.model)

    def __str__(self):
        # 返回枪的信息
        return "枪的信息：%s,%s" % (self.model, self.clip_temp)

class Clip:
    """创建一个弹夹的类"""
    def __init__(self, max_bullets):
        self.max_bullets = max_bullets
        self.bullet_list = []
        self.bullet_temp = None

    def add_bullet(self, bullet_temp):
        # 把子弹加到弹夹里，弹夹当做列表
        self.bullet_temp = bullet_temp
        for i in range(self.max_bullets):
            self.bullet_list.append(self.bullet_temp)
        # print(self.bullet_list)

    def reduce_bullet(self):
        # 开火的时候，子弹会减少
        if self.bullet_list:
            return self.bullet_list.pop()
        print(self.bullet_list)

    def __str__(self):
        # 返回弹夹的信息
        return "弹夹的信息为：%d/%d,%s" % (len(self.bullet_list), self.max_bullets, self.bullet_temp)

class Bullet:
    """创建一个子弹的类"""
    def __init__(self, damage):
        self.damage = damage

    def hit(self, bandit):
        # 子弹击中人，对人造成伤害
        bandit.hurt(self.damage)
        if bandit.hp >= 0:
            print("%s被击中，损失%d生命值" % (bandit.model, self.damage))

    def __str__(self):
        # 返回子弹的信息
        return "子弹的伤害为%s" % self.damage

def main():
    # 1、创建一个警察对象(角色类型)
    police = Player("police")
    # 2、创建一把枪对象(枪的类型)
    gun = Gun("AWM")
    # 3、创建弹夹对象(最大容量)
    clip = Clip(10)
    # 4、创建子弹对象(杀伤力)
    bullet = Bullet(20)
    # 5、警察把子弹安装到弹夹
    police.load_bullet(clip, bullet)
    # 6、警察把弹夹安装到枪上
    police.load_gun(gun, clip)
    # 7、警察拿枪
    police.take_gun(gun)
    # 8、创建一个匪徒对象
    bandit = Player("bandit")
    # 9、警察拿枪射击匪徒
    print(police)
    print(bandit)
    while bandit.hp > 0:
        # print(bandit.hp)
        police.shoot(bandit)
        if not clip.bullet_list:
            print("%s没有子弹了，无法射击" % police.model)
            break
    print(bandit)
    print(police)


if __name__ == '__main__':
    main()
