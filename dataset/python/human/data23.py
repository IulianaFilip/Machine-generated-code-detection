import wpilib

class Arm:
    def __init__(self, arm_pivot_motor: wpilib.PWMSpeedController):
        self.arm_pivot_motor = arm_pivot_motor
        self.i_acc       = 0
        self.last_error  = 0
    
    def lift(self, stick: wpilib.Joystick):
        if stick.getRawButton(4):
            self.arm_pivot_motor.set(0.5)  
        elif stick.getRawButton(3):
            self.arm_pivot_motor.set(-0.5)
        else:
            self.arm_pivot_motor.set(0)
