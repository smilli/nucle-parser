"""Creates a constituency tree out of the NUCLE CoNLL format"""
import sys


def create_constituency_tree(read_file, write_file):
  pass


def main(read_file_path, write_file_path):
  try:
    read_file = open(sys.argv[1], 'r')
  except IOError:
    print("Cannot open file %s" % sys.argv[1])
    return
  try:
    write_file = open(sys.argv[2], 'w')
  except IOError:
    print("Cannot create or write to file %s" % sysargv[2])
    return
  create_constituency_tree(read_file, write_file)


if __name__ == '__main__':
  assert(len(sys.argv) == 3)
  main(sys.argv[1], sys.argv[2])