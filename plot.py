import matplotlib.pyplot as plt
import numpy as numpy

grants = ['CA', 'GM', 'DK', 'HL', 'MH', 'NS', 'AI', 'AG', 'AA', 'ES', 'HD', 'HG', 'UL', 'OD', 'AR', 'DA', 'RR', 'DC', 'UH', 'EY', 'DP', 'MD', 'DE', 'LM', 'RF', 'HH', 'OT', 'EB', 'UM', 'RC', 'NR', 'UK', 'ZI', 'TL', 'KL', 'RO', 'RM', 'WH', 'LI', 'AT', 'OX', 'NI', 'TT', 'BD', 'HC', 'TW', 'CT', 'NC', 'TR', 'PA', 'UC']

frequencies = [477, 326, 289, 273, 159, 147, 102, 96, 85, 69, 66, 65, 65, 64, 64, 45, 34, 34, 30, 28, 24, 21, 20, 19, 17, 16, 11, 11, 10, 9, 7, 6, 4, 4, 4, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
plt.bar(grants[:10], frequencies[:10], align="center")
plt.xticks(grants[:10])
plt.tick_params(axis='x', which="major", labelsize=10)
plt.ylabel('Citations that mention NIH grants')
plt.xlabel('NIH institutes')
plt.show()

