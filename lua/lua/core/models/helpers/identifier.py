import random
import time

OFFSET = 0.01
START_TIME = int(time.time()*OFFSET)
BITS = 16


def make_identifier():
	# https://stackoverflow.com/a/37605582/7899348

	t = int(time.time()*OFFSET) - START_TIME
	u = random.SystemRandom().getrandbits(BITS)
	return (t << BITS) | u


def reverse_identifier(identifier):
	t = identifier >> BITS
	return t + START_TIME
