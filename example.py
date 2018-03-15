#!/usr/bin/env python

import butlerian
import os

job = os.getenv('butlerian.job-name', 'build-apps-apk')
app = os.getenv('butlerian.app-name', 'tables2')

if __name__ == '__main__':
    server = butlerian.JenkinsApi()
    job = server.get_job(job, app)
    for build in job.builds:
        print build
