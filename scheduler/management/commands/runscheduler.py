from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler import util
from django.conf import settings
from scheduler.jobs.delete_tokens import *
from apscheduler.schedulers.base import BaseScheduler

class Command(BaseCommand):
  help = 'Starts the APScheduler'
  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE, threadpool_size=5)

    scheduler.add_jobstore(DjangoJobStore(), "default")


    scheduler.add_job(
            delete_tokens,
            trigger=CronTrigger(hour=2, minute=0),
            id="delete_token",
            max_instances=1,
            replace_existing=True,
            misfire_grace_time=120
    )

    scheduler.start()



