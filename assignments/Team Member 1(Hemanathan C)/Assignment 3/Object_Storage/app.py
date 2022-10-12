from flask import Flask,redirect,url_for,render_template,request
import ibm_boto3
from ibm_botocore.client import Config, ClientError

COS_ENDPOINT="https://s3.us-south.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID="hCWy8fCUovcHArBvzzTBR6NLpcC8Nw0k_9-a2k3ieUsQ"
COS_INSTANCE_CRN="crn:v1:bluemix:public:cloud-object-storage:global:a/b57420b8a0a84c9c880e56bef28624fd:655d9e08-2c7b-4669-89fe-491ba51c0cbb::"

cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

app=Flask(__name__)

def get_bucket_contents(bucket_name):
    try:
        files = cos.Bucket(bucket_name).objects.all()
        files_names = []
        for file in files:
            files_names.append(file.key)
        return files_names
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))

@app.route('/')
def index():
    files = get_bucket_contents('hemu-first')
    return render_template('index.html', len=len(files),files = files)
    
if __name__=='__main__':
    app.run(debug=True)