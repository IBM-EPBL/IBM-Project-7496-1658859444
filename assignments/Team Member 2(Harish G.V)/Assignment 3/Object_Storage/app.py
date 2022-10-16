from flask import Flask,redirect,url_for,render_template,request
import ibm_boto3
from ibm_botocore.client import Config, ClientError

COS_ENDPOINT="https://s3.jp-tok.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID="0uPq-PML4sGWWJSuaaGPl5w3XgGfTYBP1kmwLQoq1r9a"
COS_INSTANCE_CRN="crn:v1:bluemix:public:cloud-object-storage:global:a/8dc4dc04ab874211bafd39dc685c6d56:bbabd782-2562-4259-bf19-f13c8ae73693::"
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
    files = get_bucket_contents('harysh')
    return render_template('index.html', len=len(files),files = files)
    
if __name__=='__main__':
    app.run(debug=True)