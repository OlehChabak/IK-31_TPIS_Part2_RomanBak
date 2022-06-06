"""This module number convert to word."""
import ConNumtoWord.example as phrase
import ConNumtoWord.module1 as num2word
import pydocstyle

if __name__ == "__main__":
    phrase.hello()
    print("Number to Word:", num2word.num2words.num2words(phrase.request_num()))


