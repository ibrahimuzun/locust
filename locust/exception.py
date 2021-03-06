class LocustError(Exception):
    pass

class ResponseError(Exception):
    pass

class CatchResponseError(Exception):
    pass

class MissingWaitTimeError(LocustError):
    pass

class InterruptTaskSet(Exception):
    """
    Exception that will interrupt a Locust when thrown inside a task
    """
    
    def __init__(self, reschedule=True):
        """
        If *reschedule* is True and the InterruptTaskSet is raised inside a nested TaskSet,
        the parent TaskSet whould immediately reschedule another task.
        """
        self.reschedule = reschedule

class StopLocust(Exception):
    pass

class RescheduleTask(Exception):
    """
    When raised in a task it's equivalent of a return statement.
    
    Used internally by TaskSet. When raised within the task control flow of a TaskSet, 
    but not inside a task, the execution should be handed over to the parent TaskSet.
    """

class RescheduleTaskImmediately(Exception):
    """
    When raised in a Locust task, another locust task will be rescheduled immediately
    """

class RPCError(Exception):
    """
    Exception that shows bad or broken network.

    When raised from zmqrpc, RPC should be reestablished.
    """

class AuthCredentialsError(ValueError):
    """
    Exception when the auth credentials provided
    are not in the correct format
    """
    pass

class RunnerAlreadyExistsError(Exception):
    pass
