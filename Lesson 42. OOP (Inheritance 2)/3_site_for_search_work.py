class Profile:
    def __init__(self, job_name):
        self.job_name = job_name

    def info(self):
        return ''

    def describe(self):
        print(self.info())


class Vacancy(Profile):
    def __init__(self, job_name, salary_want):
        super().__init__(job_name)
        self.salary_want = salary_want

    def info(self):
        return f'Предлагаемая зарплата: {self.salary_want}'


class Resume(Profile):
    def __init__(self, job_name, worktime):
        super().__init__(job_name)
        self.worktime = worktime

    def info(self):
        return f'Стаж работы: {self.worktime}'
