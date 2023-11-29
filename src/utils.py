import logging
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from requests import RequestException

from constants import EXPECTED_STATUS, MAIN_PEP_URL
from exceptions import ParserFindTagException


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def put_info_from_tables_to_tuples(abbr_tags, a_tags):
    """
    Объединяет статусы из таблицы и ссылки в кортежи для удобства их сравниния.
    """
    table_statuses = []
    links = []
    for tag in abbr_tags[2:]:
        table_statuses.append(tag.text[1:])
    for i in range(1, len(a_tags)-2, 2):
        links.append(a_tags[i]['href'])
    tuples = []
    for i in range(0, len(table_statuses)):
        tuples.append((links[i], table_statuses[i]))
    return tuples


def get_statuses_from_pep_card(session, tuples):
    """Парсит статусы из карточки со страницы каждого PEP."""
    statuses = []
    for tup in tuples[0:500]:
        link = tup[0]
        pep_url = urljoin(MAIN_PEP_URL, link)
        response = get_response(session, pep_url)
        if response is None:
            continue
        soup = BeautifulSoup(response.text, features='lxml')
        pep_info = find_tag(
            soup, 'dl', attrs={'class': 'rfc2822 field-list simple'}
        )
        lines = pep_info.text.split('\n')
        status_line_index = next(
            i for i, line in enumerate(lines)
            if line.strip().startswith('Status:')
        )
        status_value = lines[status_line_index + 1].strip()
        statuses.append(status_value)
    return statuses


def compare_table_and_card_statuses(tuples, statuses):
    """Сравнивает статусы в общей таблице и в карточке конкретного PEP."""
    for i in range(0, 500):
        if statuses[i] in EXPECTED_STATUS[tuples[i][1]]:
            continue
        else:
            logging.info(
                '\nНесовпадающие статусы:\n'
                f'{urljoin(MAIN_PEP_URL, tuples[i][0])}\n'
                f'Статус в карточке: {statuses[i]}\n'
                f'Ожидаемые статусы: {EXPECTED_STATUS[tuples[i][1]]}'
            )


def count_statuses(statuses):
    """Подсчитывает количество каждого статуса."""
    statuses_counter = {}
    for status in statuses:
        if status in statuses_counter:
            statuses_counter[status] += 1
            continue
        else:
            statuses_counter[status] = 1
            continue
    return statuses_counter
