from leaveSystem.models import Application

# function to query db and check if there is any pending application request with username
def pending_requests(username=None):
    queryset = Application.objects.filter(username=username, status=-1)
    return queryset
