import wpilib
from wpilib import Joystick, PWMSpeedController

class Arm:
    """Class to control a robot arm with a pivot motor."""
    
    def __init__(self, arm_pivot_motor: PWMSpeedController):
        self.arm_pivot_motor = arm_pivot_motor
        self._i_accumulator = 0
        self._last_error = 0

    def lift(self, stick: Joystick) -> None:
        """
        Controls the arm pivot motor based on joystick buttons.
        Button 4: move arm up
        Button 3: move arm down
        """
        power = self._get_motor_power(stick)
        self.arm_pivot_motor.set(power)

    @staticmethod
    def _get_motor_power(stick: Joystick) -> float:
        """Determine motor power from joystick button input."""
        if stick.getRawButton(4):
            return 0.5
        elif stick.getRawButton(3):
            return -0.5
        else:
            return 0.0
