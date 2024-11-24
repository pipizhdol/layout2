"""
© Skuratov's Team, 2024

Задача: сравнить нагрузку на пальцы на двух раскладках:
йцукен и diktor с использованием 2-х файлов: voina-i-mir и 1grams-3.
"""

from text_analyzer import TextAnalyzer
from visualization import *


def main():
    filename = (r'C:\voina-i-mir.txt', r'C:\1grams-3.txt')
    symbols_with_shift = (('!', '"', '№', ';', '%', ':', '?',
                           '*', '(', ')', '_', '+', '/', ','),
                          ('№', '%', ':', ';', '-', '"', '(',
                           ')', '+', 'ъ', '?', '!', '_'),
                          ('!', '"', '№', ';', '%', ':', '?',
                           '*', '(', ')', '_', '+', '/'))
    homerows = (('ф', 'ы', 'в', 'а', 'о', 'л', 'д', 'ж', ' '),
                ('у', 'и', 'е', 'о', 'н', 'т', 'с', 'р', ' '),
                ('г', 'и', 'е', 'о', 'т', 'с', 'н', 'з', ' '),
                (' ', ))
    keylout_dd = {'rfi1б': [(' ', ),
                            (' ', ),
                            (' ', )],
                  'rfi5м': [('+', '_', ')', '-', '=', 'з', 'х',
                             'ъ', 'ж', 'э'),
                            ('+', '_', ')', '0', '*', '=', 'ч',
                             'ш', 'щ', 'р', 'й', 'ж'),
                            ('0', ')', '-', '_', '=', '+', 'х',
                             'ц', 'щ', '/', 'з', 'ж', 'ч')],
                  'rfi4б': [('(', '0', 'щ', 'д', 'ю', '.'),
                            ('(', '9', 'д', 'с', 'г'),
                            ('9', '(', 'п', 'н', 'к')],
                  'rfi3с': [('*', '8', '9', 'ш', 'л', 'б'),
                            ('"', '8', 'к', 'т', 'п'),
                            ('8', '*', 'р', 'с', 'в')],
                  'rfi2у': [('6', '?', '7', 'н', 'г', 'р', 'о',
                             'т', 'ь'),
                            ('6', '-', ';', '7', 'з', 'в', 'л',
                             'н', 'м', 'б'),
                            ('7', '?', '6', ':', 'й', 'л', 'б',
                             'м', 'т', 'д')],
                  'lfi2у': [('4', '%', '5', 'к', 'е', 'а', 'п',
                             'м', 'и'),
                            ('4', '5', '.', ',', '!', '?', 'а',
                             'ы', 'ю', 'о'),
                            ('5', '4', '%', ';', ',', '.', 'я',
                             'о', 'у', 'э')],
                  'lfi3с': [('№', '3', 'у', 'в', 'с'),
                            ('3', '№', 'я', 'е', 'х'),
                            ('3', '№', 'а', 'е', 'ю')],
                  'lfi4б': [('"', '2', 'ц', 'ы', 'ч'),
                            ('2', 'ь', 'ъ', 'и', 'э'),
                            ('2', '"', 'ы', 'и', 'ь', 'ъ')],
                  'lfi5м': [('!', 'ё', 'й', 'ф', 'я', '1'),
                            ('ё', '1', 'ц', 'у', 'ф'),
                            ('ё', '1', '!', 'ф', 'г', 'ш')]}

    symbol_counter = TextAnalyzer(filename, keylout_dd,
                                  symbols_with_shift, homerows)
    final_loads = symbol_counter.count_symbols()
    # symbol_counter.display_counts()
    print(final_loads)
    print(final_loads[-1])
    loads_for_fines = final_loads[-1]
    draw_histogram(filename, final_loads)
    draw_histogram_fines(loads_for_fines)


if __name__ == "__main__":
    main()
