import requests
from bs4 import BeautifulSoup


def parse():
    url = 'https://omgtu.ru/general_information/faculties/'

    page = requests.get(url)
    print(f"Status Code: {page.status_code}")

    if page.status_code != 200:
        print("Ошибка при получении страницы")
        return

    soup = BeautifulSoup(page.text, "html.parser")

    faculty_links = soup.find_all('a', href=True)

    faculties = []

    for link in faculty_links:
        text = link.get_text(strip=True)

        if "факультет" in text.lower():
            faculties.append(text)

    print("Список факультетов:")
    for faculty in faculties:
        print(faculty)

    with open('faculties.txt', 'w', encoding='utf-8') as file:
        for faculty in faculties:
            file.write(faculty + '\n')

    print("Список факультетов успешно записан в файл 'faculties.txt'.")


if __name__ == "__main__":
    parse()

