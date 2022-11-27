import celery


# 自定义celery task 类
class MyTask(celery.Task):
    # 任务失败时执行
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    # 任务成功时执行
    def on_success(self, retval, task_id, args, kwargs):
        pass

    # 任务重试时执行
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        pass
