from argparse import ArgumentParser
from openproject_google_calendar.google_calendar.calendar import Calendar
from openproject_google_calendar.openproject import OpenProject, Project, WorkPackage
from oauth2client import tools


def main():
    parser = ArgumentParser(description='Import OpenProject work packages into Google calendar',
                            parents=[tools.argparser])
    parser.add_argument('-u', '--url', nargs='?', type=str, dest="url",
                        help='OpenProject instance url')
    parser.add_argument('-k', '--api-key', nargs='?', type=str, dest="api_key",
                        help='OpenProject API key')
    parser.add_argument('-n', '--project-name', nargs='?', type=str, dest="project_name",
                        help='OpenProject project name')
    parser.add_argument('-f', '--calendar-credentials-file', nargs='?', type=str, dest="credentials_file",
                        help='path to the Google Calendar credentials file')
    parser.add_argument('-id', '--calendar-id', nargs='?', type=str, dest="calendar_id",
                        help='Google Calendar id')

    args = parser.parse_args()

    cal = Calendar(args.credentials_file)
    op = OpenProject(url=args.url, apikey=args.api_key)
    project = op.projects[args.project_name]

    for id, wp in project.work_packages.items():
        print(wp)
        if wp.planned:
            cal.create_event(args.calendar_id, start=wp.start_date, end=wp.end_date, name=wp.subject, desc=wp.content)
        else:
            print(f"Ignoring wp [{wp.subject}]")


if __name__ == '__main__':
    main()

