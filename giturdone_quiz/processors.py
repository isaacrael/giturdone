import datetime

def custom_processor(request):
    now = datetime.datetime.now()
    #welcome_message = "Welcome My Friends! ------"
    return {'DATE_TIME':now}