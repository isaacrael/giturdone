import datetime

def get_current_time(request):
  # Create a 'context' dictionary,
  # populate it with the current time
  # and return it
  context = {}
  context['current_time'] = datetime.datetime.now()
  return context
