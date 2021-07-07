import boto3
import random

CWclient = boto3.client('cloudwatch')


def lambda_handler(event, context):

    response = CWclient.put_metric_data(

        Namespace='Han_CustomMetrics',

        MetricData=[
            {
                'MetricName': 'numbers_of_library',

                'Dimensions': [
                    {
                        'Name': "NiaoWuBookStore",
                        'Value': "NumbersEachDay"
                    },
                ],

                'Value': random.randint(40, 100),
                'Unit': 'Count'
            },
        ]
    )
    print(response)