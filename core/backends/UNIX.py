import os

from core.backends.IUnikernelBackend import IUnikernelBackend
from core.utils.executor import exec_subprocess_call


class UNIXBackend(IUnikernelBackend):
    def __init__(self):
        self.work_dir = None

    def register(self, project, module, _id, config, unikernel):
        self.work_dir = os.path.join(
            os.path.join(
                '/home/ani',
                project,
                *module  # Unpack list to arguments
            ),
            str(_id)
        )

        os.makedirs(
            self.work_dir,
            exist_ok=True
        )

        with open(
                os.path.join(self.work_dir, 'config.ml'),
                'w'
        ) as file:
            file.write(config)

        with open(
                os.path.join(self.work_dir, 'unikernel.ml'),
                'w'
        ) as file:
            file.write(unikernel)

        # TODO: Save to database

        # TODO: Initialize scheduler

        return self.work_dir

    def configure(self, _id):
        # TODO: Need better exception handling
        exec_subprocess_call('mirage configure --unix', self.work_dir)
