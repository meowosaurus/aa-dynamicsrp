"""App Tasks"""

# Standard Library
import logging

# Third Party
from celery import shared_task

logger = logging.getLogger(__name__)

# Create your tasks here


# dynamicsrp Task
@shared_task
def dynamicsrp_task():
    """dynamicsrp Task"""

    pass
