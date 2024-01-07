from adafruit_motor import servo
import pwmio


class MotorsModel:
    SG90 = 1
    GEEKSERVO = 2


class Motors:
    """Motors utility"""

    def __init__(self, left_pin, right_pin, motors_model=MotorsModel.SG90):
        if motors_model == MotorsModel.SG90:
            min_pulse, max_pulse = 1000, 2000
            self.speed_multiplier = 0.2 
        else:
            min_pulse, max_pulse = 500, 2500
            self.speed_multiplier = 0.5 
        self.left = servo.ContinuousServo(
            pwmio.PWMOut(left_pin, frequency=50),
            min_pulse=min_pulse,
            max_pulse=max_pulse,
        )
        self.right = servo.ContinuousServo(
            pwmio.PWMOut(right_pin, frequency=50),
            min_pulse=min_pulse,
            max_pulse=max_pulse,
        )

    def drive(self, left_throttle, right_throttle):
        # Every cheap servo is a unique snowflake and if you want to get
        # better precision, you might want to calibrate the constants used
        # here until calling drive(0, 0) consistently results in fully stopped
        # motors
        self.left.throttle = min(
            1, max(self.speed_multiplier * left_throttle - 0.07, -1)
        )
        self.right.throttle = min(
            1, max(-1 * self.speed_multiplier * right_throttle, -1)
        )