import json
import operator
data = [[], [], [], ['DC', 'DC', 'DC'], ['ES', 'ES', 'ES', 'ES'], ['AR', 'AR', 'AR', 'AR'], [], [], [], ['HL', 'HL', 'HL', 'HL', 'HL', 'HL'], [], [], [], ['NS'], [], ['CA'], [], ['MH', 'DA', 'GM', 'MH', 'DA', 'DA', 'RF', 'MH', 'MH', 'MH', 'MH', 'MH', 'AG', 'AG', 'MH'], [], [], [], ['GM', 'HL', 'HL', 'HL', 'HL', 'DK'], [], [], [], [], [], ['EB', 'CA'], [], [], [], [], [], [], [], [], ['DK', 'DK', 'DK'], [], [], [], [], ['LM'], ['CA', 'CA', 'CA'], [], ['DK'], ['CA'], ['GM', 'GM', 'GM', 'MD', 'MD', 'HL', 'MD', 'MD'], ['RR', 'OD', 'OD', 'OD'], [], ['HL', 'HL', 'HL', 'HL', 'HL', 'HL'], ['AR', 'AI', 'AR'], ['ES'], [], [], ['DK', 'DK', 'GM', 'DK', 'UL'], [], [], ['MH', 'HD', 'NS', 'HD', 'MH', 'HD', 'NS', 'GM', 'GM'], [], [], [], [], ['HL', 'GM', 'AR', 'GM'], [], [], [], ['NS', 'CA', 'CA'], ['CA', 'CA', 'AI', 'HL', 'DK', 'HL', 'LM', 'CA', 'DK', 'HD'], ['AR', 'RR'], [], [], ['OT', 'HL', 'CA', 'HL'], ['CA', 'HL'], ['UH', 'UH', 'UH', 'UH', 'UH', 'HG', 'UH', 'UH', 'HG', 'AR', 'UH', 'UL', 'UH', 'UM', 'UH'], ['ES', 'HL', 'ES'], ['NS', 'MH', 'MH', 'AG', 'RC', 'AI'], [], ['DC', 'DC', 'UL'], [], ['HG', 'GM', 'MH', 'GM', 'GM'], ['UK', 'TT', 'TT'], ['OD'], [], ['OT', 'CA', 'HL'], [], [], ['DK', 'DK', 'GM', 'GM', 'HG'], [], [], [], [], ['DK'], [], [], [], ['HL', 'CA'], [], ['DC', 'GM'], [], [], ['CA', 'GM', 'GM', 'DK', 'AG', 'AI', 'AI', 'CA', 'HL'], [], ['DP', 'AI'], [], ['NI', 'CA'], ['NS', 'DK', 'HL', 'HL', 'CA', 'DK', 'CA', 'GM', 'DK'], [], ['NS', 'NS'], [], ['DK', 'HL', 'CA', 'CA', 'DK', 'HL', 'CA', 'DK', 'CA', 'DP'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['OD', 'OD', 'RR', 'AI'], [], ['HG', 'HG', 'HG', 'DK', 'HG'], ['DA', 'MH', 'CA', 'CA', 'GM', 'DA', 'DP', 'CA', 'GM', 'DA', 'MH'], [], ['DK', 'OD', 'DK', 'DK', 'DK'], [], [], ['DK'], [], ['MH', 'MH', 'MH', 'HL', 'GM', 'OD', 'UL', 'MH'], ['GM', 'NS'], ['OX', 'HL', 'DK', 'HL', 'DK', 'HL', 'DK', 'HL', 'HL', 'HL', 'DK', 'HG'], ['NS'], ['CA', 'DK', 'LM', 'HL', 'CA', 'CA', 'CA', 'DK'], [], [], [], [], ['DK', 'DK', 'AA'], [], ['HD', 'HD', 'HL'], [], ['MH', 'NS', 'HD', 'GM', 'NS'], [], [], [], [], ['HL', 'HL', 'HL', 'HL'], [], [], ['DE'], [], [], [], ['MH', 'RM', 'RF', 'DP', 'RF', 'AG'], [], ['DK', 'DK', 'HD', 'GM', 'HL', 'DK', 'DK', 'DK', 'DK', 'DK', 'AI'], [], [], [], ['CA'], [], ['CA', 'AR', 'CA', 'RR'], ['CA'], [], [], [], ['HL', 'HL', 'HL'], [], [], [], [], [], [], [], [], ['AR', 'HL', 'DC', 'HL', 'GM', 'AR', 'CA', 'AR'], ['HL', 'CA'], [], [], [], ['NS', 'MH', 'DC', 'DP', 'NS'], [], [], [], ['OD'], [], ['HL', 'GM', 'HL'], ['NS'], ['HL', 'HL', 'AI'], ['CA', 'CA', 'CA', 'CA', 'GM', 'GM', 'CA', 'CA', 'CA'], [], [], [], [], ['NS', 'ES'], [], ['DK', 'HD', 'AG', 'EY', 'ES', 'MH', 'CA', 'EY', 'EY'], ['HD'], ['AA', 'AA', 'AA', 'AA', 'AA'], [], [], [], ['DK', 'HD', 'AG', 'EY', 'ES', 'MH', 'CA', 'EY', 'EY'], [], [], ['CA', 'CA', 'GM'], [], [], [], [], ['MH', 'HD', 'NS', 'NS', 'MH', 'HD', 'NS'], ['DK', 'DK', 'DK', 'AT'], [], [], ['AI', 'GM', 'UH', 'HL'], [], [], [], ['CA'], [], ['GM', 'CA', 'CA', 'CA', 'CA', 'KL', 'CA', 'CA', 'CA'], [], [], [], [], ['DA', 'DA', 'DA', 'DA', 'DA'], ['GM'], ['TL', 'UL'], [], [], [], [], ['AI', 'TL', 'HL'], [], [], [], [], [], ['GM', 'ES', 'ES'], ['DK', 'DK', 'DK'], ['AR', 'AG'], [], ['CA', 'CA', 'GM', 'GM', 'CA', 'GM', 'GM'], [], [], ['AI', 'AI', 'OD', 'AI'], [], ['LM'], ['AI', 'HL', 'OD', 'CA', 'CA', 'CA'], ['DK', 'DK', 'DK', 'HL', 'DK', 'CA', 'CA', 'DK'], [], [], ['DK', 'HL', 'AI', 'DK', 'AI', 'CA', 'UL', 'DK', 'AI', 'DK', 'UL', 'UH', 'DK'], ['NS', 'NS', 'NS'], ['OD', 'MH', 'NS', 'MH', 'MH'], [], [], [], ['AR', 'AR', 'AG', 'GM', 'MH'], ['CA', 'UL', 'UL'], ['ES', 'HL', 'HL', 'HL'], [], ['MH', 'DA', 'OD', 'DA', 'DA', 'DA'], ['HD', 'DK', 'HL', 'HL', 'MD', 'HL', 'HL', 'HL', 'UL', 'HL'], [], ['ES', 'ES'], ['HL'], [], ['CA'], [], ['CA', 'ES', 'AI', 'ES'], ['MH', 'DP', 'AG', 'RF', 'MH', 'DA', 'NS', 'MH'], ['CA', 'CA', 'CA'], [], [], ['GM'], [], ['GM', 'HL', 'HL', 'HL'], [], ['HG'], [], ['GM', 'GM', 'HD'], ['CA', 'AR', 'AR', 'DP'], [], ['DE', 'CA', 'CA', 'CA'], [], ['HG', 'HG'], ['NS', 'AG', 'NS'], [], [], ['EB', 'CA', 'CA', 'GM', 'CA'], ['CA', 'AR'], [], ['RR', 'DK', 'DK', 'DK', 'DK', 'DK'], [], ['CA'], ['UK', 'UK', 'UM'], [], [], ['DP', 'AI', 'UC'], [], [], [], ['DK', 'DK', 'HL', 'DK', 'DK'], [], [], ['MH'], [], ['NS', 'HD'], ['UK'], ['AA', 'AA', 'AA', 'AA', 'AA'], [], [], ['DK', 'CA', 'UL', 'DK', 'DK', 'UL', 'DK'], ['CA', 'CA', 'CA'], [], ['HL', 'HL', 'UL', 'UL', 'HL', 'AI'], [], [], [], ['PA', 'LM', 'HG', 'GM', 'HL', 'HL'], [], ['HD', 'OD', 'GM', 'NS', 'NS'], [], ['GM', 'CA', 'GM'], ['DK', 'GM'], ['CA', 'CA', 'GM', 'CA', 'CA', 'CA', 'CA', 'CA', 'OD'], ['DK', 'GM'], ['HL', 'OT', 'GM', 'CA', 'CA'], ['HL', 'AG', 'HL', 'HL', 'DK'], [], ['AI', 'AI', 'AI'], ['HL', 'AI'], [], [], ['MH', 'NS', 'NS', 'MH', 'GM'], [], ['OD', 'AI', 'AI', 'AI'], ['CA', 'CA', 'LM', 'OD', 'CA', 'CA', 'CA', 'HH', 'CA', 'GM'], ['GM', 'CA', 'CA', 'NS', 'GM', 'GM', 'CA'], [], [], [], ['ES', 'ES', 'ES'], ['NS', 'MH', 'MH', 'AG', 'GM', 'AG', 'AG', 'AG', 'NS', 'RF', 'NS', 'NS', 'RF', 'NS', 'RF'], [], ['DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK'], [], ['DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'HL', 'OT', 'HL', 'CA', 'CA'], [], [], [], [], [], ['GM', 'GM', 'GM'], ['HD'], ['EY', 'AG', 'AG', 'EY', 'UL', 'EY', 'EY', 'EY', 'EY', 'EY', 'CA', 'NS'], [], [], ['GM', 'CA', 'CA', 'HL'], [], ['HD', 'DK', 'DK', 'NS', 'DK', 'HD'], ['CA', 'RR', 'GM', 'GM', 'GM', 'OD'], ['DK', 'OD', 'MH', 'NS', 'NS'], [], [], [], [], [], ['CA', 'GM', 'GM'], [], ['GM', 'GM'], [], [], [], [], ['GM', 'NS', 'NS'], [], ['CA', 'CA'], [], ['AR', 'UL', 'HL', 'AI', 'HL', 'MD', 'HL'], ['HL', 'HL', 'CA', 'GM', 'CA', 'GM'], [], ['MH', 'ZI'], ['CA'], [], ['HH', 'AR', 'UL'], ['GM', 'GM'], ['GM', 'GM', 'GM', 'HD', 'CA'], [], [], ['DE'], ['CA', 'CA', 'CA'], ['DK', 'HD', 'EY', 'ES', 'MH', 'NS', 'EY', 'EY'], ['LI', 'AG', 'HL', 'OT', 'HG', 'OD', 'GM', 'HL', 'HG', 'HL', 'HG', 'HL', 'NS'], ['ES', 'HL'], [], ['AG', 'GM', 'HG'], ['AR', 'GM', 'CA', 'CA', 'HL', 'GM'], [], ['CA', 'CA', 'CA', 'GM'], ['ES', 'CA', 'OD', 'HG'], [], ['NS'], ['CA', 'RR', 'OD', 'MH', 'HD', 'HD', 'HD', 'NS', 'ES', 'RR', 'MH', 'ES'], ['RR', 'RF', 'HL', 'NS', 'AG', 'UL', 'CA', 'HD', 'UL', 'NS', 'NS'], ['NS', 'AG'], [], ['NS'], [], ['CA', 'HL'], [], ['CA', 'HG', 'HL', 'HL'], ['MH', 'MH', 'MH', 'AG', 'AG', 'HH', 'MH', 'MH', 'MH', 'MH'], ['AR'], [], [], [], ['NR', 'DK'], [], ['HL', 'GM', 'GM', 'GM'], ['CA', 'CA', 'CA', 'OD'], [], ['GM', 'CA', 'HL'], [], [], [], ['AR', 'AR', 'TL', 'UL'], [], [], [], [], [], ['HD', 'HD'], [], ['ES', 'ES', 'ES', 'RR', 'RR', 'HD'], ['CA', 'DK', 'UL'], ['DK', 'HL'], [], [], [], ['RR', 'UL', 'RR', 'AI', 'AG'], ['DK', 'GM', 'HD'], [], ['CA', 'CA', 'CA', 'CA'], ['CA', 'CA', 'CA'], [], [], ['GM'], ['CA', 'CA'], [], ['DK', 'DK', 'DK', 'OD'], ['AI'], ['CA', 'GM', 'HG', 'GM', 'GM'], ['CA', 'GM', 'GM', 'GM'], [], ['AR', 'CA', 'CA', 'CA'], ['CA', 'CA'], ['GM', 'DK', 'CA', 'HL', 'HL', 'HL', 'HD'], [], [], [], ['GM', 'CA', 'NS'], [], [], [], ['CA', 'ES', 'CA'], [], ['HG', 'DE', 'NS', 'HD', 'GM', 'GM', 'UM', 'GM', 'HG', 'HL'], [], [], [], ['DK', 'DK', 'DK', 'DK', 'DK'], [], [], ['DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK'], [], [], [], [], [], ['AG', 'AG', 'AG', 'RC', 'EB', 'LM'], ['CA', 'CA', 'CA', 'GM', 'DK'], [], [], ['GM'], ['CA', 'CA', 'CA'], [], [], [], ['CA', 'HL', 'CA', 'AI', 'CA', 'RR', 'CA', 'GM'], [], [], ['AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA'], ['DK', 'GM', 'DK', 'DK', 'DK'], ['GM', 'AG', 'RF', 'AG', 'AG', 'AG', 'AG', 'UL', 'CA'], ['GM', 'HL', 'CA', 'HL'], ['DK', 'DK', 'DK'], [], ['CA'], ['GM', 'ES', 'DK', 'OD', 'ES', 'NS'], [], [], ['OD', 'HD', 'HD', 'HD', 'AR', 'AR', 'HD'], [], ['GM', 'GM', 'GM'], ['HH', 'HD', 'UL', 'CA', 'HD', 'GM'], ['GM', 'GM'], ['AG', 'AG'], [], [], [], ['DK', 'GM', 'GM'], [], [], [], ['ES', 'DK', 'CA', 'UL'], [], [], ['MH', 'KL', 'HD', 'OD', 'HG', 'KL', 'MH'], ['CA'], [], [], ['GM', 'HG'], ['EY', 'EY', 'RF'], [], [], ['ZI'], ['AR', 'MD', 'AI'], ['AG'], [], [], [], [], ['GM', 'RR'], [], ['NS', 'MD', 'NS'], ['AI', 'AI', 'UL'], [], ['AA', 'AA', 'AA', 'AA', 'AA'], ['OD', 'DK', 'GM', 'GM', 'DK', 'DK'], [], ['DE', 'HL'], ['CA', 'GM', 'HL'], ['CA', 'CA', 'CA', 'GM'], ['CA', 'CA', 'DK', 'CA'], [], ['MH', 'MH'], ['UL', 'CA', 'CA', 'OD', 'CA', 'CA', 'CA', 'OD', 'CA'], [], ['CA', 'RR', 'RR', 'GM', 'OD'], ['CA', 'GM', 'RR', 'RR'], ['HG', 'HL', 'HL'], ['NS', 'MH', 'GM', 'GM', 'MH', 'NS', 'NS'], ['GM', 'AG'], [], [], [], ['NS', 'MH', 'NR', 'MH', 'GM'], [], ['AR'], [], ['MH', 'MH', 'HD', 'MH', 'MH'], ['HL', 'HL', 'GM', 'GM', 'CA'], ['CA'], ['HG', 'GM', 'UM', 'GM', 'NS', 'GM'], ['GM'], ['CA', 'UH', 'UL', 'CA', 'CA', 'CA', 'CA'], [], [], ['HL', 'GM', 'ES', 'UL'], ['HH', 'HH', 'HH', 'HH', 'HH', 'HH', 'CA', 'CA', 'HH', 'WH', 'WH', 'HH', 'HH'], ['GM', 'DA', 'DA', 'DA'], [], ['HL', 'CA'], [], [], [], ['RR', 'MH', 'MH', 'RC', 'NS', 'NS'], [], [], ['EB', 'CA'], ['HL', 'MH', 'MD', 'MD', 'GM', 'MD'], [], ['GM', 'CA', 'HL'], ['CA', 'HL'], ['CA', 'CA'], ['DK', 'GM'], [], ['DP', 'MH', 'MH', 'AG', 'HL', 'MH', 'GM', 'GM', 'MH', 'AA', 'CA', 'NS', 'MH'], ['AG', 'AG'], [], ['OD'], [], [], [], ['CA'], [], ['HL', 'HL', 'NS', 'NS', 'NS'], [], ['NS', 'NS'], ['AG', 'NS'], [], ['GM', 'HL', 'CA', 'HL'], [], [], [], ['DK', 'HL', 'DK', 'GM', 'CA', 'DK'], ['CA', 'OD', 'GM', 'GM', 'DK', 'DK', 'DK'], [], ['HL', 'HL', 'HL', 'HL'], ['GM', 'NS'], [], ['HL', 'GM', 'CA'], [], [], [], [], [], ['CA', 'CA', 'CA', 'CA', 'CA', 'CA'], ['GM', 'CA', 'HL'], [], ['GM', 'HL', 'CA', 'HL'], [], ['NR', 'AG', 'UL', 'NR', 'AA', 'NR', 'UL', 'MD', 'MD', 'NR', 'AG', 'AA'], [], [], [], [], ['OD'], [], [], ['GM', 'GM', 'EB', 'NS', 'MH', 'NS', 'NS', 'NS', 'HD', 'UL'], [], [], [], [], ['CA', 'DP', 'CA', 'DP', 'GM', 'GM', 'CA', 'EB', 'AI', 'AI', 'GM'], ['HD', 'DC', 'HG', 'UM'], [], ['HL', 'EB', 'GM', 'AR', 'AR', 'HL', 'DK', 'DK', 'GM', 'AR', 'CA', 'AR', 'AR', 'AR', 'CA', 'AR'], [], ['AI', 'AI'], ['CA', 'CA', 'HG', 'CA', 'AI', 'GM', 'CA', 'CA', 'AI', 'CA', 'CA', 'GM', 'CA', 'AG', 'CA', 'AG', 'HG'], [], ['NS', 'NS', 'HL'], [], [], [], [], ['GM', 'CA', 'HL'], [], [], ['AI', 'AR', 'AI', 'AI', 'AI', 'MD', 'HG', 'HG', 'HG', 'AI', 'AI', 'HG', 'AR', 'TR', 'UL', 'AI', 'UL', 'AI', 'MD', 'AI'], ['AI', 'AI', 'AI', 'AI', 'AI', 'AI', 'AI', 'AI'], ['UL', 'DK', 'DK', 'DK', 'DK', 'UL', 'DK', 'DK'], ['OD', 'AI', 'OD', 'AI', 'AI', 'AI'], ['AA', 'DK', 'CA', 'UL', 'AA', 'CA', 'AA', 'UL', 'AA'], [], ['HL', 'GM', 'DA', 'HL', 'HL', 'CA', 'CA', 'DA', 'DK', 'HL', 'HL', 'HL', 'HL', 'GM', 'CA', 'CA', 'HL', 'DK', 'CA', 'CA'], [], ['MH', 'MH', 'MH', 'MH'], [], [], [], [], [], ['AA', 'AA', 'AA'], [], ['AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA'], [], ['ES'], ['CA', 'GM'], ['HL', 'HL', 'DK', 'DK', 'HD', 'DK', 'CA', 'GM'], [], [], [], [], [], [], [], [], ['DK'], [], ['DK'], ['DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK'], ['HL', 'GM', 'AR', 'HL', 'DK', 'DK', 'GM', 'AR', 'CA', 'AR', 'AR', 'AR', 'CA', 'AR'], ['ES', 'ES', 'ES', 'ES', 'ES'], [], ['DA', 'GM', 'DA', 'HL', 'DA', 'NS', 'NS', 'DA', 'HG', 'NS', 'GM', 'CA', 'DA', 'CA', 'DA', 'DA', 'NS'], ['AI', 'AI', 'AI', 'AI'], [], ['GM', 'HL', 'CA', 'HL'], [], ['HG', 'HL', 'HG', 'HL', 'RC'], [], ['MD', 'CA', 'CA'], [], ['DK'], ['GM', 'HL', 'HG', 'HL', 'GM', 'CA', 'CA'], ['DE', 'DE', 'DE', 'DE', 'DE', 'DE', 'DE', 'DE'], [], [], ['MH', 'MH', 'DK', 'MH', 'GM', 'DK', 'NS', 'HD', 'MH', 'MH'], [], [], [], ['ES'], [], [], ['DK', 'DK', 'GM', 'GM', 'LM', 'DK', 'DK', 'OD', 'DK', 'DK', 'DK', 'GM', 'OD', 'GM', 'GM', 'DK', 'DK', 'DK', 'DK', 'DK'], [], [], ['AI', 'OD', 'AI', 'AI', 'HH'], ['OD', 'AI', 'AI'], [], [], ['NC', 'GM', 'GM', 'HL', 'CA', 'CA', 'GM', 'CA', 'CA', 'GM'], [], [], ['HL'], ['HG', 'DK', 'HL', 'HG', 'HL', 'HL'], [], ['MH', 'MH', 'MH', 'MH', 'MH', 'MH'], ['MH', 'MH', 'MH', 'MH'], [], ['GM', 'HG', 'HL', 'HL', 'GM', 'CA', 'HG', 'CA'], ['HG', 'GM', 'GM', 'DK', 'DK', 'HD', 'GM', 'GM', 'DK', 'RC', 'HG'], ['HG', 'HG', 'HG', 'GM', 'GM', 'DK', 'HL', 'GM', 'HG', 'DK', 'CA', 'GM'], ['MH', 'MH', 'MH', 'MH', 'MH', 'MH'], [], ['DE', 'DE', 'DE', 'DE'], [], ['DK', 'DK', 'DK', 'DK', 'DK', 'DK'], ['RC', 'HG', 'GM', 'GM', 'DK', 'GM', 'DK', 'RC', 'HG', 'GM'], ['GM', 'MH', 'MH', 'MH', 'MH'], ['GM', 'HL', 'HL', 'HL'], ['DK'], ['CA', 'CA', 'ES', 'RR'], [], ['MH', 'MH', 'MH', 'MH', 'MH', 'MH', 'GM', 'MH'], ['CA', 'DK', 'DK', 'CA', 'CA', 'DK'], ['RC', 'GM', 'GM', 'GM', 'DK', 'GM', 'DK', 'GM']]

data2 = [[], [], [], ['MH', 'MH', 'MH', 'MH', 'MH', 'MH', 'MH', 'MH'], ['DC', 'DC', 'DC'], ['ES', 'ES', 'ES', 'ES'], [], [], [], ['AR', 'AR', 'AR', 'AR'], [], [], [], [], [], [], ['HL', 'HL', 'HL', 'HL', 'HL', 'HL'], [], [], [], [], [], ['NS'], ['AI'], [], ['CA'], [], [], ['NS', 'NS', 'CA', 'AG'], [], [], [], [], [], ['HG', 'DK', 'HL', 'HL', 'HL', 'DK', 'DK', 'HL', 'DK', 'HL', 'DK', 'DK', 'HL', 'HL', 'DK', 'HL', 'DK'], [], [], ['NS', 'ZI', 'NS'], ['CA', 'CA'], ['GM', 'CA', 'GM', 'CA', 'DP', 'CA', 'DA', 'GM', 'RM', 'CA'], ['CA', 'CA'], [], [], [], [], [], [], [], ['AG', 'NS', 'NS', 'GM', 'EY', 'UM', 'MH', 'EY', 'HL', 'HL', 'AI', 'MH', 'GM', 'EY'], ['AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA'], ['CT'], [], ['EB', 'CA'], [], [], [], [], ['OD', 'NS', 'NS', 'HG', 'UM', 'NS'], ['CA'], [], [], ['CA', 'UL', 'UL'], [], [], [], [], [], [], [], [], [], [], ['GM', 'GM', 'GM', 'MD', 'MD', 'HL', 'MD', 'MD'], [], ['GM', 'CA'], [], [], ['AR', 'AI', 'AR'], [], [], [], ['ES'], [], [], [], ['DK', 'DK', 'GM', 'DK', 'UL'], [], ['AI', 'GM', 'AI', 'DK'], [], ['MH', 'HD', 'NS', 'HD', 'MH', 'HD', 'NS', 'GM', 'GM'], [], [], [], [], [], [], ['CA'], [], ['HL', 'GM', 'AR', 'GM'], [], [], ['LM', 'CA'], [], [], ['DE'], [], ['CA'], ['CA', 'CA', 'AI', 'HL', 'DK', 'HL', 'LM', 'CA', 'DK', 'HD'], ['AR', 'RR'], [], [], ['TW'], [], [], [], ['GM', 'GM'], ['OT', 'HL', 'CA', 'HL'], ['CA', 'HL'], [], ['UH', 'UH', 'UH', 'UH', 'UH', 'HG', 'UH', 'UH', 'HG', 'AR', 'UH', 'UL', 'UH', 'UM', 'UH'], [], [], [], ['DC', 'DC', 'UL'], [], ['MH', 'MH', 'MH', 'MH'], ['HG', 'GM', 'MH', 'GM', 'GM'], [], [], [], ['CA', 'DC', 'DC'], [], ['OD'], [], [], [], ['OT', 'CA', 'HL'], [], [], [], [], [], [], ['AG', 'AG', 'AG', 'NS', 'NS'], ['DK'], [], [], ['LM', 'LM', 'CA'], ['GM', 'GM'], [], ['CA'], [], ['DC', 'GM'], [], [], ['LM'], [], [], ['DP', 'AI'], [], ['NS', 'DK', 'HL', 'HL', 'CA', 'DK', 'CA', 'GM', 'DK'], ['CA', 'OD', 'CA', 'CA', 'GM'], [], [], ['NS', 'NS'], [], [], [], ['NS', 'OD', 'NS', 'NS', 'CA'], [], [], ['CA'], ['DA', 'AI', 'AI', 'DA'], [], [], [], [], ['CA', 'CA', 'DK', 'CA', 'CA'], [], [], [], [], ['CA', 'GM'], ['AA', 'OD', 'CA'], [], [], ['OD', 'MH', 'HL'], ['OD', 'OD', 'RR', 'AI'], [], [], ['DA', 'MH', 'CA', 'CA', 'GM', 'DA', 'DP', 'CA', 'GM', 'DA', 'MH'], [], [], [], [], [], ['DK'], [], [], ['HL'], ['AG', 'UL', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG', 'RF', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG'], [], [], [], ['GM', 'NS'], ['OX', 'HL', 'DK', 'HL', 'DK', 'HL', 'DK', 'HL', 'HL', 'HL', 'DK', 'HG'], ['CA', 'CA', 'HL', 'CA', 'CA', 'CA', 'CA'], ['NS'], ['CA', 'DK', 'LM', 'HL', 'CA', 'CA', 'CA', 'DK'], [], [], ['DP', 'HG', 'HL', 'DK', 'DP'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['CA', 'CA', 'CA', 'CA', 'CA', 'GM', 'CA'], ['HD', 'AG', 'AG', 'GM'], [], ['AI', 'AI', 'CA', 'CA'], [], [], [], [], ['MH', 'MH', 'GM', 'DE'], [], [], ['DK', 'DK', 'HD', 'GM', 'HL', 'DK', 'DK', 'DK', 'DK', 'DK', 'AI'], [], [], [], ['GM', 'AI', 'CA', 'CA'], [], ['CA', 'CA', 'RO', 'RO', 'CA', 'RO', 'CA', 'CA', 'CA'], ['GM'], ['CA'], [], [], [], [], [], ['RF', 'HG', 'GM', 'GM', 'HL'], [], [], [], ['CA', 'CA', 'CA', 'CA'], ['HL', 'CA'], [], ['HL', 'UH'], ['CA', 'GM', 'UL'], [], [], [], [], [], ['HL', 'HL', 'HL', 'UH', 'HL'], ['RR', 'CA', 'CA', 'RR', 'GM', 'GM', 'RR', 'RR', 'GM', 'GM', 'OD'], ['NS', 'MH', 'DC', 'DP', 'NS'], ['HL'], [], [], [], [], ['NS'], [], [], ['CA', 'CA', 'CA', 'CA', 'GM', 'GM', 'CA', 'CA', 'CA'], [], [], [], ['AI', 'HL', 'HL', 'HL', 'HL', 'AG', 'HL', 'AI', 'HL', 'HL', 'AG', 'ES', 'HL', 'ES'], [], ['CA', 'AI'], ['NS', 'NS', 'NS', 'CA', 'NS'], ['NS', 'ES'], [], [], [], ['HD'], ['AA', 'AA', 'AA', 'AA', 'AA'], [], [], [], [], [], [], [], ['CA', 'CA', 'GM'], [], ['CA', 'CA', 'CA', 'CA', 'HL', 'CA', 'OD'], [], ['HL'], [], [], ['MH', 'HD', 'NS', 'NS', 'MH', 'HD', 'NS'], ['DK', 'DK', 'DK', 'AT'], [], [], [], [], ['AA', 'AA'], [], ['CA', 'CA'], ['CA'], [], [], ['GM'], [], [], [], ['GM'], ['TL', 'UL'], [], [], [], ['DK'], ['LM'], [], [], [], [], ['GM', 'ES', 'ES'], ['CA', 'CA', 'GM', 'GM', 'CA', 'GM', 'GM'], [], ['AI'], [], ['AI', 'AI', 'OD', 'AI'], [], [], ['DK', 'DK', 'DK', 'HL', 'DK', 'CA', 'CA', 'DK'], [], ['RF', 'AG', 'RF', 'AG', 'AG', 'AG', 'AG', 'AG', 'AG'], ['DK', 'HL', 'AI', 'DK', 'AI', 'CA', 'UL', 'DK', 'AI', 'DK', 'UL', 'UH', 'DK'], [], [], ['AR', 'AR', 'AG', 'GM', 'MH'], ['CA', 'UL', 'UL'], ['ES', 'HL', 'HL', 'HL'], ['DK'], ['HL', 'HL', 'HH', 'HC', 'HL', 'UH', 'HL', 'HL', 'UH', 'UH', 'HL'], ['MH', 'DA', 'OD', 'DA', 'DA', 'DA'], [], ['MH', 'OD', 'HL'], [], ['CA'], [], [], ['KL', 'AI', 'UL'], ['MH', 'DP', 'AG', 'RF', 'MH', 'DA', 'NS', 'MH'], ['CA', 'CA', 'CA'], [], ['GM'], ['GM', 'GM', 'HD'], [], [], [], ['NS', 'AG', 'NS'], [], [], ['CA', 'AR'], ['RR', 'DK', 'DK', 'DK', 'DK', 'DK'], [], [], ['BD', 'OT', 'HL', 'HL'], ['UK', 'UK', 'UM'], ['ES', 'GM', 'HD', 'LM'], ['HL'], [], [], [], [], ['DK', 'DK', 'DK', 'DK'], [], [], [], [], [], [], ['CA', 'EB', 'CA', 'CA', 'CA', 'CA'], ['MH'], [], ['NS', 'HD'], ['AA', 'AA', 'AA', 'AA', 'AA'], [], ['CA', 'CA', 'CA'], ['CA'], ['CA', 'DK'], [], ['HL', 'HL', 'UL', 'UL', 'HL', 'AI'], [], [], ['CA'], [], [], ['AG', 'NS', 'RF'], [], [], ['HD', 'OD', 'GM', 'NS', 'NS'], [], ['GM', 'CA', 'GM'], ['DK', 'GM'], ['CA', 'CA', 'GM', 'CA', 'CA', 'CA', 'CA', 'CA', 'OD'], ['ES', 'ES'], ['DK', 'GM'], ['HL', 'ES'], [], ['HL', 'OT', 'GM', 'CA', 'CA'], ['HL', 'AG', 'HL', 'HL', 'DK'], ['CA', 'CA', 'GM', 'GM'], [], ['CA'], ['ES', 'OD', 'CA', 'CA', 'ES', 'CA'], ['DP'], [], [], [], ['CA', 'UL', 'CA', 'CA', 'CA', 'CA', 'CA'], ['CA', 'CA', 'CA'], [], [], ['MH', 'NS', 'NS', 'MH', 'GM'], [], [], ['GM', 'CA', 'CA', 'NS', 'GM', 'GM', 'CA'], ['GM', 'HG', 'DA', 'NS'], [], [], ['ES', 'ES', 'ES'], [], [], ['DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK'], ['AA', 'AA', 'AA', 'AA', 'AA', 'AA'], [], ['DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'HL', 'OT', 'HL', 'CA', 'CA'], ['DK'], [], ['CA', 'CA', 'EB', 'CA', 'CA', 'CA'], [], [], [], [], [], [], [], [], [], ['EY', 'AG', 'AG', 'EY', 'UL', 'EY', 'EY', 'EY', 'EY', 'EY', 'CA', 'NS'], [], [], [], [], [], ['HD', 'DK', 'DK', 'NS', 'DK', 'HD'], ['AR', 'CA', 'OD', 'CA', 'AR', 'AR', 'CA', 'OD'], ['CA', 'RR', 'GM', 'GM', 'GM', 'OD'], ['DK', 'OD', 'MH', 'NS', 'NS'], [], ['DP', 'AI', 'DK'], [], [], [], ['NS', 'HG', 'DP', 'GM', 'NS', 'NS', 'GM'], [], [], [], ['CA', 'GM', 'GM'], [], [], [], [], [], [], [], ['NI'], ['CA', 'CA', 'CA'], [], ['AA', 'AA', 'AA', 'AA', 'AA'], ['HL', 'HL', 'CA', 'GM', 'CA', 'GM'], ['DP', 'GM', 'GM'], ['LM', 'HD', 'GM', 'ES'], ['MH', 'ZI'], ['CA'], [], ['MH', 'MH', 'MH', 'MH', 'MH'], ['HH', 'AR', 'UL'], ['GM', 'GM'], [], ['UL'], ['DE'], [], [], ['LI', 'AG', 'HL', 'OT', 'HG', 'OD', 'GM', 'HL', 'HG', 'HL', 'HG', 'HL', 'NS'], [], [], ['CA', 'CA', 'CA', 'GM'], ['ES', 'CA', 'OD', 'HG'], ['DK', 'GM', 'GM', 'GM'], ['NS'], ['CA', 'CA', 'CA', 'CA', 'OD', 'CA', 'CA', 'CA', 'CA'], [], ['CA', 'RR', 'OD', 'MH', 'HD', 'HD', 'HD', 'NS', 'ES', 'RR', 'MH', 'ES'], [], [], ['NS'], [], ['CA', 'HL'], [], [], ['GM', 'GM'], [], [], [], [], [], [], ['NR', 'DK'], ['HL', 'GM', 'GM', 'GM'], ['AA', 'AA', 'UL', 'CA'], [], [], ['ES', 'ES', 'ES', 'RR', 'RR', 'HD'], ['CA', 'DK', 'UL'], ['CA', 'CA', 'CA'], ['DK', 'HL'], [], [], [], [], [], ['CA', 'UM'], ['GM'], [], [], ['AI'], [], ['CA', 'GM', 'HG', 'GM', 'GM'], ['CA', 'GM', 'GM', 'GM'], [], ['CA', 'GM', 'UL'], ['CA', 'CA'], ['GM', 'DK', 'CA', 'HL', 'HL', 'HL', 'HD'], ['DK', 'CA', 'UL'], [], [], [], ['MH', 'NS', 'MH', 'DK', 'NS', 'HL', 'DP'], ['AI', 'AI', 'AR', 'GM', 'UL', 'GM', 'AR', 'AR', 'UL'], [], ['CA', 'ES', 'CA'], [], [], [], [], [], [], [], [], ['DK', 'DK', 'DK', 'DK', 'DK', 'DK', 'DK'], [], [], [], ['DA', 'DA', 'DA', 'DA', 'GM'], ['MH', 'NS', 'HL', 'GM', 'RC', 'GM', 'NS', 'CA', 'NS', 'NS'], [], ['GM'], [], ['CA', 'CA', 'CA'], [], ['LM', 'CA', 'RR'], [], [], ['AA', 'AA', 'AA', 'AA', 'AA'], [], ['GM', 'AG', 'RF', 'AG', 'AG', 'AG', 'AG', 'UL', 'CA'], [], [], ['DK', 'DK', 'DK'], ['AG', 'AG'], [], [], [], [], ['HL', 'HL', 'HL', 'GM', 'CA', 'DK'], ['CA'], [], [], [], [], ['NS', 'MD', 'NS'], [], ['AA', 'AA', 'AA', 'AA', 'AA'], ['CA', 'GM', 'HL'], ['CA', 'CA', 'CA', 'GM'], ['GM'], ['CA', 'GM', 'GM', 'GM', 'CA', 'EB', 'GM', 'DA', 'AG', 'HG', 'GM', 'RM'], ['AI'], ['GM', 'GM', 'LM'], [], [], [], ['HL', 'HL', 'GM', 'GM', 'CA'], ['CA'], [], ['CA', 'UH', 'UL', 'CA', 'CA', 'CA', 'CA'], [], [], [], [], ['DP', 'MH', 'MH', 'AG', 'HL', 'MH', 'GM', 'GM', 'MH', 'AA', 'CA', 'NS', 'MH']]

total = []
for i in data:
    for j in i:
        total.append(j)
# print(total)

for i in data2:
    for j in i:
        total.append(j)
frequency = {}

for i in total:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

# names = []
# for key, value in frequency.items():
#     names.append(key)
# print(names)
print(frequency)
        
f = open("enrichr23586463.json", "w")
f.write(json.dumps(frequency))
f.close()

sorted_d = sorted(frequency.items(), key=operator.itemgetter(1))
keys = []
values = []
for i in sorted_d[::-1]:
    keys.append(i[0])
    values.append(i[1])
print(keys)
print(len(keys))
print(values)