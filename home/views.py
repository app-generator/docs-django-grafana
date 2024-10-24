from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import os
import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings

# Create your views here.

from .models import *


def index(request):
    context = {
        "date": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return HttpResponse("Hello DJANGO! time is: " + context["date"])


# Regular expression to match SQL query logs
LOG_REGEX = r"\((?P<time>\d+\.\d+)\)\s*(?P<query>[^\n]+);\s*args=(?P<args>[^;]+);\s*alias=(?P<alias>\w+)"

@api_view(['GET'])
def get_sql_logs(request):
    log_file = os.path.join(settings.BASE_DIR, 'sql_queries.log')
    data = {
        'total_queries': 0,
        'total_time': 0,
        'query_details': []
    }

    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()

        # Parse each log entry using the regex
        for log in logs:
            match = re.search(LOG_REGEX, log)
            if match:
                time_taken = float(match.group('time'))
                query = match.group('query').strip()
                args = match.group('args').strip()
                alias = match.group('alias').strip()

                # Update the total number of queries and total time
                data['total_queries'] += 1
                data['total_time'] += time_taken

                # Add the structured query details to the list
                data['query_details'].append({
                    'time_taken': time_taken,
                    'query': query,
                    'args': args,
                    'alias': alias
                })

        # Calculate average query time
        data['average_time'] = data['total_time'] / data['total_queries'] if data['total_queries'] > 0 else 0

        return Response(data)

    except FileNotFoundError:
        return Response({"error": "Log file not found."}, status=404)
