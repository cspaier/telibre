import os
import sys
import subprocess
from multiprocessing import Process
from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import (
    Command as StaticFilesRunserverCommand,
)

class Command(StaticFilesRunserverCommand):
    """This command removes the need for two terminal windows when running runserver.
    https://github.com/django-commons/django-tailwind-cli/blob/main/src/django_tailwind_cli/management/commands/tailwind.py
    """

    help = (
        "Starts a lightweight Web server for development and also serves static files. "
        "Also runs a js build worker in another thread."
    )
    
    def inner_run(self, *args, **options):
        watch_cmd = ["npm", "start"]
        watch_process = Process(
            target=subprocess.run,
            args=(watch_cmd,),
            kwargs={
                "cwd": os.path.join(settings.BASE_DIR, "theme", "static_src") ,
                "check": True,
            },
        )
        
        debug_server_cmd = [
            sys.executable,
            "manage.py",
            "runserver",
        ]

        debugserver_process = Process(
            target=subprocess.run,
            args=(debug_server_cmd,),
            kwargs={
                "cwd": settings.BASE_DIR,
                "check": True,
            },
        )
    
        try:
            watch_process.start()
            debugserver_process.start()
            watch_process.join()
            debugserver_process.join()
        except KeyboardInterrupt:  # pragma: no cover
            watch_process.terminate()
            debugserver_process.terminate()

