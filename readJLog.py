
import json, argparse

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


data = []
parser = argparse.ArgumentParser()

## -f FILENAME -tid THREADID
parser.add_argument("-f", "--filename", help="log file name")
parser.add_argument("-tid", "--threadid", help="thread Id", type=int)
parser.add_argument("-pfl", "--printfirstline", help="print first line mode", type=str2bool, default=False)

args = parser.parse_args()

filename = 'ec1_current.log.txt'
threadId = -1

if not args.filename :
  filename = args.filename

if not args.threadid is None:
  threadId = args.threadid

print( "filename {} threadid {} ".format(filename, threadId) )

with open('ec1_current.log.txt') as json_file:
    for line in json_file:
      data = json.loads(line)
      if args.printfirstline :
        print data
        break
      if threadId < 0 or data['threadId'] == threadId :
        print(data['timestamp']+', '+ data['level']+ ', '+ data['message'])


