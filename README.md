# Связка Redis, Celery / Celery Beat
1. `celery -A <tasks> worker -Q <to_compute> -l info` - запуск воркеров, где:
   -  tasks - имя модуля, в котором лежит селери
   -  to_compute - имя списка в редис, из которого воркеры будут читать задачи
2. `celery -A <tasks> beat -l INFO` - запуск скедуллера