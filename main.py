import numpy as np


# Constants (NOTE: dropped decimals for simplicity)
TABLE_WIDTH = 152
TABLE_LENGTH = 274
TABLE_HEIGHT = 76
NET_HEIGHT = 15



class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.data = np.array([float(x), float(y), float(z)])
        
    def x(self):
        return self.data[0]
   
    def y(self):
        return self.data[1]
    
    def z(self):
        return self.data[2]  
       
    def __str__(self):
        return '<%s, %s, %s>' % (self.x(), self.y(), self.z())
        
   
    
    

# position for the first hit, [0] for player1, [1] for player2
BALL_SERVE_POS = [
    Vector(0, TABLE_WIDTH // 2, TABLE_HEIGHT + 10),
    Vector(TABLE_LENGTH, TABLE_WIDTH // 2, TABLE_HEIGHT + 10)
]


class Paddle:
    def __init__(self, player):
        pass
        

    def hit():
        # hit the ball
        pass
        

class Ball:
    def __init__(self, position=BALL_SERVE_POS[0], velocity=Vector(0, 0, 0), acceleration=Vector(0, 0, 0), spin=0):
        # pva, are all numpy arrays of 3 values. [x, y, z]
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.spin = spin
    
    def off_table(self, ball):
        if (self.z > TABLE_HEIGHT):
            print("Checking table bounds BAD. ball is too high to bounce")
            return
        
        # when the height is 76, check the position based on the table, and the current reciever's side
        pass 
        
    
    def bounce(self):
        pass
    
    
    def ball_info(self):
        print(f'position = %s \n velocity = %s \n acceleration = %s \n spin = %d' % (self.position, self.velocity, self.acceleration, self.spin))
        
    

def init_pp():
    print(BALL_SERVE_POS[0])
    
    velocity = Vector(0,0,0)
    acceleration = Vector(0,0,0)
    
    ball = Ball(BALL_SERVE_POS[0], velocity, acceleration, 10)
    return ball
    

    


in_game = True

def main():
    
    ball = init_pp()
    ball.ball_info()
    

main()
