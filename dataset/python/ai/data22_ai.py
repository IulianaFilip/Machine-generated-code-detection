class AngleNavigator:
    def __init__(self, angle_pairs):
        """
        angle_pairs: list of tuples (current_angle, target_angle)
        """
        self.angle_pairs = angle_pairs

    @staticmethod
    def normalize_angle(angle):
        """Normalize an angle to [-180, 180] degrees."""
        angle %= 360
        if angle > 180:
            angle -= 360
        return angle

    @staticmethod
    def calculate_best_offset(current, target):
        """Calculate the shortest rotation offset from current to target angle."""
        offset_a = target - current
        if offset_a > 0:
            offset_b = offset_a - 360
        else:
            offset_b = offset_a + 360
        return offset_a if abs(offset_a) <= abs(offset_b) else offset_b

    def run(self):
        for navx, target in self.angle_pairs:
            print(f"Robot points to {navx}°, target should be {target}°")
            
            navx_n = self.normalize_angle(navx)
            target_n = self.normalize_angle(target)
            print(f"Normalized angles: Robot = {navx_n}°, Target = {target_n}°")

            best_offset = self.calculate_best_offset(navx_n, target_n)
            print(f"Optimal rotation offset: {best_offset}°\n")


if __name__ == "__main__":
    angle_pairs = [(-247, 270)]
    navigator = AngleNavigator(angle_pairs)
    navigator.run()
