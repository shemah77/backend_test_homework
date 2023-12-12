print('Я домашка')

courses = {
    'Python-разработчик': {
        'Стек': {
            'Python',
            'Django',
            'GitHub',
            'SQL',
            'PostgreSQL',
            'Bash',
            'Nginx',
            'Gunicorn',
            'Docker',
            'Docker Hub'
        },
        'Продолжительность': '9 месяцев'
    },
    'Python-разработчик плюс': {
        'Стек': {
            'Python',
            'Django',
            'GitHub',
            'SQL',
            'PostgreSQL',
            'Bash',
            'Nginx',
            'Gunicorn',
            'Docker',
            'Docker Hub',
            'Flask',
            'FastAPI',
            'Scrapy',
            'Selenium',
            'SQLAlchemy'
        },
        'Продолжительность': '14 месяцев'
    }
}

diff = set.difference(
    courses['Python-разработчик плюс']['Стек'],
    courses['Python-разработчик']['Стек']
)
courses_diff = str.join(', ', diff)

print(
    'Отличия стеков в курсах «Python-разработчик плюс» и '
    f'«Python-разработчик»: {courses_diff}'
)
