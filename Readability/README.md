# Readability of a text using the Coleman-Liau index

This is a program that computes the approximate grade level needed to comprehend some text.

**Coleman-Liau index**

The Coleman-Liau index of a text is designed to output what (U.S.) grade level is needed to understand the text. The formula is: index = 0.0588 * L - 0.296 * S - 15.8.
Where "L" is represented by (letters * 100) / words; and "S" is represented by (sentences * 100) / words.

The output of this program is the Coleman-Liau index, ranging from less than 1 to 16+.
