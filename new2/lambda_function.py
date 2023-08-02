import json
import pymysql
hostname = ecomdb.cjy9ii6a47cp.us-east-1.rds.amazonaws.com
user = ecomuser
password = ecompassword
db = ecomdb
conn = pymysql.connect(host=hostname, user=user, passwd=password, db=db, connect_timeout=60)
claimdict = {0: "member_id", 1: "claim_id", 2: "insurance_covered", 3: "total_cost", 4: "test_code"}
def lambda_handler(event, context):
req_body = json.loads(event["body"])
    with conn.cursor() as cur:
        print("Received member idL {}".format(req_body["member_id"]))
        cur.execute("SELECT * from claims where member_id={}".format(req_body["member_id"]))
        print("Query executed")
        claim_details = []
        try:
            # TODO: write code...
            for claim in cur.fetchall():
                claim_detail = {}
                for row in range(0, len(claim)):
                    claim_detail[claimdict[row]] = claim[row]
        
                claim_details.append(claim_detail)
        except Exception as e:
            print(e)
return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(claim_details)
    }
