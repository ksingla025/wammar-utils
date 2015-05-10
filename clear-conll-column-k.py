import io
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("-i", "--input_filename", required=True)
argparser.add_argument("-o", "--output_filename", required=True)
argparser.add_argument("-k", "--one_based_column_numbers", nargs="+", type=int, required=True, help="space delimited list of one-based column indeces to clear.")
args = argparser.parse_args()

columns_to_clear = set(args.one_based_column_numbers)

with io.open(args.input_filename) as input_file:
  with io.open(args.output_filename, mode='w') as output_file: 
    for line in input_file:
      if len(line.strip()) == 0:
        output_file.write(u'\n')
      else:
        conll_fields = line.strip().split('\t')
        for column_index in columns_to_clear:
          conll_fields[column_index - 1] = u'_'
        output_file.write(u'\t'.join(conll_fields) + u'\n')
