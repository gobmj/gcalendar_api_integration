from django.shortcuts import redirect
from django.urls import reverse
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from rest_framework.response import Response
from rest_framework.views import APIView


class GoogleCalendarInitView(APIView):
    def get(self, request):
        # Set up OAuth credentials and scopes
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json',
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri=
            'https://gcalapiintegration.govindm3.repl.co/rest/v1/calendar/redirect/'
        )

        # Generate authorization URL and redirect user
        authorization_url, state = flow.authorization_url(prompt='consent')
        request.session['state'] = state
        return redirect(authorization_url)


class GoogleCalendarRedirectView(APIView):
    def get(self, request):
        # Retrieve authorization code and state
        code = request.query_params.get('code')
        state = request.query_params.get('state')

        # Verify state to prevent CSRF attacks
        if state != request.session['state']:
            return Response({'error': 'Invalid state parameter'}, status=400)

        # Set up OAuth flow
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json',
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri=
            'https://gcalapiintegration.govindm3.repl.co/rest/v1/calendar/redirect/'
        )

        # Exchange authorization code for access token
        flow.fetch_token(code=code)

        # Get access token
        credentials = flow.credentials
        access_token = credentials.token

        # Use access token to retrieve calendar events
        service = build('calendar',
                        'v3',
                        credentials=credentials,
                        static_discovery=False)
        events_result = service.events().list(calendarId='primary').execute()
        events = events_result.get('items', [])

        return Response(events)
