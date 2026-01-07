def get_right_motor(self, degrees: float, gatillo: float) -> float:
    """
    Calculates the power for the right motor based on the robot's heading in degrees
    and the throttle input (gatillo). Positive gatillo moves forward, negative backward.

    Args:
        degrees (float): Current heading of the robot in degrees (0–360+).
        gatillo (float): Throttle value, typically in range [-1, 1].

    Returns:
        float: Right motor power.
    """
    if degrees <= 90:
        # Gradually reduce power from -gatillo to 0 as degrees goes 90->0
        return self.smooth_between(90, 0, degrees) * (-1 * gatillo)
    elif degrees <= 180:
        return -1 * gatillo
    elif degrees <= 270:
        # Gradually increase power from -gatillo to 0 as degrees goes 180->270
        return self.smooth_between(180, 270, degrees) * (-1 * gatillo)
    elif degrees <= 360:
        return gatillo
    else:
        return 0
