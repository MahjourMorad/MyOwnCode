import boto3

session = boto3.Session(aws_access_key_id="XXXXXXXXXXXXXXXXXXXX",
                        aws_secret_access_key='XXXXXXXXXXXXXXXXXXXX',
                        aws_session_token='XXXXXXXXXXXXXXXXXXXX')

session = session.resource('s3')
my_bucket = session.Bucket('bucketNAme or allias')
client = boto3.client("s3")
s3 = boto3.resource('s3')


s3.meta.client.copy_objec('DMT_PLANT_CSSU.csv',
                           'bucketNAme',
                           'folder/fileName.csv'
                           ,ExtraArgs={'ServerSideEncryption': 'public-AES256'})


