#!/usr/bin/env python

class PID:
	# TODO: Complete the PID class. You may add any additional desired functions
    def __init__(self, Kp, Ki=0.0, Kd=0.0, max_integral=10):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.point = 0
        self.p_value = 0
        self.i_value = 0
        self.d_value = 0
        self.prev_error = 0
        self.max_integral = max_integral
        self.result = 0

    def UpdateError(self, cte):
        error = self.point - cte
        self.p_value = error
        self.i_value += error
        self.i_value = min(self.i_value, self.max_integral)
        self.i_value = max(self.i_value, -self.max_integral)
        self.d_value = 0.0
        self.d_value = (error - self.prev_error)
        self.prev_error = error

    def TotalError(self):
        self.result = self.Kp * self.p_value + self.Ki * self.i_value + self.Kd * self.d_value
        return self.result
