broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/London'
enable_utc = True

task_annotations = {
    # 'tasks.add': 'low-priority',
    'tasks.add': {'rate_limit': '10/m'}
    # Can do this at runtime too
    # celery -A tasks control rate_limit tasks.add 10/m
}