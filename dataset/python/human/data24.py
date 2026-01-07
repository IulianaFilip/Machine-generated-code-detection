 def get_right_motor(self, degrees, gatillo):
        #se asume que para avanzar derecho los dos motores se ponen en 1
        if degrees <= 90:
            return self.smooth_between(90, 0, degrees) * (-1 * gatillo)
        elif degrees <= 180:
            return (-1 * gatillo)
        elif degrees <= 270:
            return self.smooth_between(180, 270, degrees) * (-1 * gatillo)
        elif degrees <= 360:
            return gatillo
        else:
            return 0