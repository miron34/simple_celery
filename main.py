from tasks.tasks import add

# print(type(add))
for i in range(20):
    print(add.apply_async((i, i), queue='to_compute'))
print('all transfered to celery')
