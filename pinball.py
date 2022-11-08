import play

play.set_backdrop('light blue')
frames = 25#Kare sıklığı
lose = play.new_text(words='YOU LOSE', font_size=100, color='red')
win = play.new_text(words='YOU WIN', font_size=100, color='yellow')
platform = play.new_box(color='brown', y = -250, width = 150, height = 15)
ball = play.new_circle(color='green', y = -160, radius = 15)
blocks = []
 
 
@play.when_program_starts
def start():
   
    platform.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=1
    )
   
    ball.start_physics(
        stable=False, x_speed=30, y_speed=30, obeys_gravity=False, bounciness=1, mass=10
    )
 
    
    block_x = play.screen.left+75
    block_y = play.screen.top-50
 
    for i in range(3): 
        while (block_x <= play.screen.right-30):
        #for i in range(5):
            block=play.new_box(
                color='grey', x=block_x, y=block_y, width=110, height=30, border_color='dark grey', border_width=1
            )
            blocks.append(block)
            block_x=block_x + block.width
        block_x=play.screen.left+75
        block_y=block.y-block.height
 
        platform.show()
    lose.hide()
    win.hide()
 
@play.repeat_forever
async def game():
   
    if play.key_is_pressed('a'):
        platform.physics.x_speed = -20
    elif play.key_is_pressed('d'):
        platform.physics.x_speed = 20
    else:
        platform.physics.x_speed = 0
 
   
    for b in blocks:
        if b.is_touching(ball):
            ball.physics.x_speed = -1 * ball.physics.x_speed
            ball.physics.y_speed = -1 * ball.physics.y_speed
            b.hide()
            blocks.remove(b)
 
    #kaybetme
    if ball.y <= platform.y:
        lose.show()
        ball.physics.x_speed=0
        ball.physics.y_speed=0
    #kazanma
    if len(blocks) == 0:
        win.show()
        ball.physics.x_speed=0
        ball.physics.y_speed=0
    await play.timer(seconds=1/frames)#kare değişim hızı

play.start_program()                  