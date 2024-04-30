from gzoltar import gzoltar 
import sys

if __name__ == '__main__':
    src_file=sys.argv[1]
    dst_file=sys.argv[2] 
    gz = gzoltar()
    gz.transfer_for_simfix(src_file, dst_file)
