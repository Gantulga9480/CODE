from googleapiclient.discovery import build

api_key = "AIzaSyC_BARnD6aYIznCjychbMEl_qDwv6jKZos"

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        id="E_v21-sY5yybk8JfiXDDdw"
)
response = request.execute()
print(response)