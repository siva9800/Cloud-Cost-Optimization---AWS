
#sample response i got when i called for snapshots details
response = ec2.describe_snapshots(OwnerIds=['self'])
#this is actually when i called an aws api(ec2,snapshots) and returned in form of jason we can convert to dictonary in python and use it

{
    'Snapshots': [
        {
            'SnapshotId': 'snap-1',
            'VolumeId': 'vol-1',
            'StartTime': '2022-02-15T12:00:00.000Z',
            'Description': 'Snapshot 1',
            'Tags': [{'Key': 'Name', 'Value': 'Snapshot1'}]
        },
        {
            'SnapshotId': 'snap-2',
            'VolumeId': 'vol-2',
            'StartTime': '2022-02-15T12:00:00.000Z',
            'Description': 'Snapshot 2',
            'Tags': [{'Key': 'Name', 'Value': 'Snapshot2'}]
        },
        .
        .
    ],
    'ResponseMetadata': {
        'RequestId': '12345678-1234-1234-1234-123456789012',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'content-type': 'application/x-amz-json-1.1',
            'date': 'Sun, 06 Feb 2022 12:00:00 GMT',
            'x-amzn-requestid': '12345678-1234-1234-1234-123456789012',
            'content-length': '1200',
            'connection': 'keep-alive'
        },
        'RetryAttempts': 0
    }
}




instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
# it will return information about EC2 instances that are currently in the "running" state.

{
    'Reservations': [
        {
            'ReservationId': 'r-0abc123def456ghi7',
            'Instances': [
                {
                    'InstanceId': 'i-1234567890abcdef0',
                    'InstanceType': 't2.micro',
                    'State': {
                        'Name': 'running',
                        'Code': 16
                    },
                    'LaunchTime': '2022-02-15T12:00:00.000Z',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'ExampleInstance'},
                        {'Key': 'Environment', 'Value': 'Production'}
                    ]
                },
                # More instance entries may follow...
            ]
        },
        # More reservation entries may follow... like reservationID: 'adh'... (other running instances)
    ],
    'ResponseMetadata': {
        'RequestId': '12345678-1234-1234-1234-123456789012',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'content-type': 'application/x-amz-json-1.1',
            'date': 'Sun, 06 Feb 2022 12:00:00 GMT',
            'x-amzn-requestid': '12345678-1234-1234-1234-123456789012',
            'content-length': '1200',
            'connection': 'keep-alive'
        },
        'RetryAttempts': 0
    }
}
