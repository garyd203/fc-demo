"""Stub file for live coding demo"""

from flyingcircus import fn
from flyingcircus.core import Stack
from flyingcircus.service.cloudwatch import Alarms
from flyingcircus.service.ec2 import Instance


def create_ec2_stack():
    stack = Stack()
    return stack


if __name__ == '__main__':
    stack = create_ec2_stack()
    print(stack.export())
