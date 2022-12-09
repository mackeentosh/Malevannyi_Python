from unittest import TestCase
from task3 import Vacancy, DataSet, InputConnect, Report

class VacancyTests(TestCase):
    def test_vacancy_type(self):
        self.assertEqual(type(Vacancy(['Программист', 70000, 500000, 'RUR', 'Москва', '2022-05-31T17:32:31+0300'])).__name__, 'Vacancy')

    def test_vacancy_name(self):
        self.assertEqual(Vacancy(['Программист', 70000, 500000, 'RUR', 'Москва', '2022-05-31T17:32:31+0300']).name, 'Программист')

    def test_salary_from(self):
        self.assertEqual(Vacancy(['Программист', 70000, 500000, 'RUR', 'Москва', '2022-05-31T17:32:31+0300']).salary_from, 70000.0)

    def test_salary_to(self):
        self.assertEqual(Vacancy(['Программист', 70000, 500000, 'RUR', 'Москва', '2022-05-31T17:32:31+0300']).salary_to,
            500000.0)

    def test_salary_currency(self):
        self.assertEqual(Vacancy(['Программист', 70000, 500000, 'RUR', 'Москва', '2022-05-31T17:32:31+0300']).salary_currency,
                         'RUR')

    def test_area_name(self):
        self.assertEqual(Vacancy(['Программист', 70000, 500000, 'RUR', 'Москва', '2022-05-31T17:32:31+0300']).area_name,
            'Москва')

    def test_published_at(self):
        self.assertEqual(Vacancy(['Программист', 70000, 500000, 'RUR', 'Москва', '2022-05-31T17:32:31+0300']).published_at,
            '2022-05-31T17:32:31+0300')


class InputConnectTests(TestCase):
    def test_inputconnect_type(self):
        self.assertEqual(type(InputConnect()).__name__, 'InputConnect')

    def test_convert_currency(self):
        self.assertEqual(InputConnect().convert_currency(Vacancy(["name", "40000.0", "80000.0", "RUR", "area", "date"])), 60000)
        self.assertEqual(InputConnect().convert_currency(Vacancy(["name", "35000.0", "70000.0", "AZN", "area", "date"])), 1873200)
        self.assertEqual(InputConnect().convert_currency(Vacancy(["name", "1000.0", "3000.0", "USD", "area", "date"])), 121320)


class DataSetTests(TestCase):
    def test_dataset_type(self):
        self.assertEqual(type(DataSet("file_name")).__name__, 'DataSet')

    def test_dataset_file_name(self):
        self.assertEqual(DataSet("vacancies.csv").file_name, 'vacancies.csv')

    def test_dataset_vacancies(self):
        self.assertEqual(DataSet("vacancies.csv").vacancies, [])

    def test_csv_filer(self):
        self.assertEqual(DataSet("file_name").csv_filer(['Название', 'Описание', 'Средняя з/п'], [['Программист', 'Middle Frontend', '150000']]),
                         [{'Название': 'Программист', 'Описание': 'Middle Frontend', 'Средняя з/п': '150000'}])

    def test_empty_csv_filer(self):
        self.assertEqual(DataSet("file_name").csv_filer([], [[]]), [{}])

    def test_remove_html_tags(self):
        self.assertEqual(DataSet("file_name").remove_html_tags(["Программист<p></p>", "<strong>Особенности</strong>"]),
                         ['Программист', 'Особенности'])

    def test_remove_html_tags_and_spaces(self):
        self.assertEqual(DataSet("file_name").remove_html_tags(["Програм<strong>ми</strong >ст", "<h1>Особен</   h1 >ности"]),
                         ['Программист', 'Особенности'])

    def test_remove_html_tags_without_text(self):
        self.assertEqual(DataSet("file_name").remove_html_tags(["<    >", "<div><  /div >"]), ['', ''])


class ReportTests(TestCase):
    def test_report_type(self):
        self.assertEqual(type(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291}, {'Москва': 0.1893}, "Программист")).__name__,
                         'Report')

    def test_report_salary_by_year(self):
        self.assertEqual(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291},
                   {'Москва': 0.1893}, "Программист").salary_by_year,
                         {2022: 204316})

    def test_report_vacs_by_years(self):
        self.assertEqual(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291},
                   {'Москва': 0.1893}, "Программист").vacs_by_years,
                         {2022: 428})

    def test_report_vac_salary_by_years(self):
        self.assertEqual(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291},
                   {'Москва': 0.1893}, "Программист").vac_salary_by_years,
                         {2022: 103546})

    def test_report_vac_counts_by_years(self):
        self.assertEqual(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291},
                   {'Москва': 0.1893}, "Программист").vac_counts_by_years,
                         {2022: 21})

    def test_report_salary_by_cities(self):
        self.assertEqual(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291},
                   {'Москва': 0.1893}, "Программист").salary_by_cities,
                         {'Казань': 156337, 'Москва': 142291})

    def test_report_vacs_by_cities(self):
        self.assertEqual(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291},
                   {'Москва': 0.1893}, "Программист").vacs_by_cities,
                         {'Москва': '18,93%'})

    def test_report_profession(self):
        self.assertEqual(Report({2022: 204316}, {2022: 428}, {2022: 103546}, {2022: 21}, {'Казань': 156337, 'Москва': 142291},
                   {'Москва': 0.1893}, "Программист").profession,
                         'Программист')


