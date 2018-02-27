from flyingcircus import fn
from flyingcircus.core import Stack
from flyingcircus.service.cloudwatch import Alarms
from flyingcircus.service.ec2 import Instance


def get_standard_ec2_instance(name, instance_type="t2.micro"):
    return Instance(Properties={
        "ImageId": "ami-942dd1f6",
        "InstanceType": instance_type,
        "Monitoring": False,
        "Tags": [
            {"Key": "Name", "Value": name},
            {"Key": "Owner", "Value": "garyd"},
            {"Key": "Team", "Value": "My Super Team"},
        ],
    })


def create_ec2_stack():
    stack = Stack()
    stack.Resources["WebServer"] = get_standard_ec2_instance("Web Server")
    stack.Resources["DBServer"] = dbserver = get_standard_ec2_instance("Database Server", instance_type="t2.nano")

    stack.Resources["DBServerAlarm"] = alarm = Alarms.high_cpu(85)
    alarm.Properties.setdefault("Dimensions", []).append({
        "Name": "InstanceId",
        "Value": fn.Ref(dbserver),
    })

    return stack


if __name__ == '__main__':
    stack = create_ec2_stack()
    print(stack.export())
