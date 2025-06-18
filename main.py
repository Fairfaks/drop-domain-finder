import os

from extract_data import GetDomains
from domains_tools import FindDomains


def check_data_file(file):
    """
    Check CSV file with data and initiate parse data if file not found or needs to update.
    """
    all_archives = {'net.ru': 'https://ru-tld.ru/files/NET-RU_Domains_ru-tld.ru.gz',
                    'org.ru': 'https://ru-tld.ru/files/ORG-RU_Domains_ru-tld.ru.gz',
                    'pp.ru': 'https://ru-tld.ru/files/PP-RU_Domains_ru-tld.ru.gz',
                    '*.ru': 'https://ru-tld.ru/files/3d_domains_ru-tld.ru.gz',
                    'ru': 'https://ru-tld.ru/files/RU_Domains_ru-tld.ru.gz',
                    'rf': 'https://ru-tld.ru/files/RF_Domains_ru-tld.ru.gz',
                    'su': 'https://ru-tld.ru/files/SU_Domains_ru-tld.ru.gz'}
    if file not in os.listdir():
        get_domains = GetDomains(file)
        get_domains.worker(all_archives)
    else:
        while True:
            choice = input('Do you want UPDATE CSV file? (YES/NO)\n').strip().lower()
            if choice == 'yes':
                get_domains = GetDomains(file)
                get_domains.worker(all_archives)
            elif choice == 'no':
                break
            else:
                print('Please enter YES or NO')
    return file


base_file = 'all_domains.csv'
res_file = 'result.csv'

work_file = check_data_file(base_file)

days_free = int(input('Enter days left number: ').strip())
search_mask = input('Enter domains search mask (word or RegEx): ').strip()

domains_tools = FindDomains(work_file, res_file)
domains_tools.worker(days_free, search_mask)

