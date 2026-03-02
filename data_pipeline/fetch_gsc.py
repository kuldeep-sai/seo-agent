from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
from config import SITE_URL

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
KEY_FILE = 'service_account.json'   # download from GCP

def fetch_gsc_data():

    credentials = service_account.Credentials.from_service_account_file(
        KEY_FILE, scopes=SCOPES)

    service = build('searchconsole', 'v1', credentials=credentials)

    request = {
        'startDate': '2026-02-20',
        'endDate': '2026-03-01',
        'dimensions': ['query', 'page'],
        'rowLimit': 25000
    }

    response = service.searchanalytics().query(
        siteUrl=SITE_URL, body=request).execute()

    rows = []

    for row in response.get('rows', []):
        rows.append({
            "query": row["keys"][0],
            "page": row["keys"][1],
            "clicks": row["clicks"],
            "impressions": row["impressions"],
            "ctr": row["ctr"],
            "position": row["position"]
        })

    return pd.DataFrame(rows)
