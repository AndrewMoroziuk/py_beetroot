from download import read_and_copy_text_by_sentence as copy_text, \
    count_row, count_chr
from Homework_Plus.data import row_for_hm_9 as row

if __name__ == "__main__":
    copy_text(row)
    count_row(row)
    count_chr(row)
