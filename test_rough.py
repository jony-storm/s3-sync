import argparse
import requests
# import ijson

parser = argparse.ArgumentParser(description="A CLI for syncing files to S3")
parser.add_argument("--issuers", type=str, action="append", required=True, help="Provide issuers")
parser.add_argument("--type", type=str, action="append", required=True)
parser.add_argument("--bucket", type=str, required=True)
parser.add_argument("--url", type=str, required=True)

# f = urlopen("https://transparency-in-coverage.uhc.com/api/v1/uhc/blobs/")
parser.add_argument("-p", "--path", type=str, default="root", help="provide a path or the path will be defaults to root")

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : 'bytes', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return str(size) + " " + power_labels[n]

args = parser.parse_args()
resp = requests.request('HEAD', args.url)
print("your file has {}.".format(format_bytes(int(resp.headers['content-length']))))
# for i in args.type:
#     print(i)

