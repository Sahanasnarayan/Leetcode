class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = []
        
        for asteroid in asteroids:
            if not i or asteroid > 0:
                i.append(asteroid)
            else:
                while i and i[-1] > 0 and i[-1] < abs(asteroid):
                    i.pop()

                if i and i[-1] == abs(asteroid):
                    i.pop()
                else:
                    if not i or i[-1] < 0:
                        i.append(asteroid)
        
        return i