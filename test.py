from openanalytics.version import VERSION
from openanalytics.client import Client
import threading
import time
import random
from openanalytics.connectors import (
    MongoDBConnector,
    SQLiteConnector,
    InfluxDBConnector,
)
from openanalytics.models.Identify import Identify
from openanalytics.models.Token import Token
from openanalytics.models.Track import Track
from openanalytics.models.Page import Page
from openanalytics.models.Log import Log
from datetime import datetime, timezone

connector = MongoDBConnector(host="mongodb://localhost:27017/", dbname="handshake")
# connector = SQLiteConnector(dbname="handshake.sqlite3")
# connector = InfluxDBConnector(
#     token="5wttcrwYX3COT8OQaorbOKUYAmPPNE-7oC_2itF60bBqIfC33L9g4k3APNjcCkCAuBuwWurOVEBo6gNYP0cAuA==",
#     org="asdasd",
#     url="http://localhost:8086",
#     bucket="handshake",
# )
client = Client(connector=connector, sync_mode=False, debug=True)

# client.idetify(
#     Identify(userID="Lakitha", event="Report Request", metadata={"data": "sample data"})
# )

# client.token(
#     Token(
#         event="Incident Reported",
#         action="Similarity",
#         count=532,
#         metadata={
#             "data": 3244,
#             "location": {"city": "colombo", "country": "sri lanka"},
#         },
#     )
# )

# client.track(
#     Track(
#         endpoint="http:localhost:1233/search",
#         event="Profile Search",
#         properties={"params": "q=sdfsf"},
#         timestamp=datetime.now(timezone.utc),
#     )
# )

# client.page(Page(name="Dashboard", category="Stats", properties={"status": 0}))

# client.logger(
#     Log(
#         summary="This is a log test function call",
#         level="Debug",
#         event="test.py",
#         metadata={"sample": "samasdasd"},
#     )
# )


def make():
    for i in range(100000):
        _val = int(random.random() * 100)
        client.token(
            Token(
                event="Incident Reported",
                action="Generate",
                count=_val,
                metadata={
                    "text_count": 3244,
                    "location": {"city": "colombo", "country": "sri lanka"},
                },
            )
        )
        time.sleep(0.1)


# t = threading.Thread(target=make)
# t.start()
# t.join()

make()

client.shutdown()
