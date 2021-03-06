#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from gitlab.Client import Client

import json

if gitlab_server is None:
    raise Exception("No GitLab server provided.")

client = Client.get_client()
latestTag = client.gitlab_tag_statuses(locals())[0]
newTriggerState = json.dumps(latestTag)

if triggerState != newTriggerState:
    tagName = latestTag["name"]
    tagMessage = latestTag["message"]
    commitId = latestTag["commit"]["id"]
    commitTitle = latestTag["commit"]["title"]
    commitMessage = latestTag["commit"]["message"]
    commitAuthor = latestTag["commit"]["author_name"]
    commitCommitter = latestTag["commit"]["committer_name"]
    commitCreationDatetime = latestTag["commit"]["created_at"]
    commitAuthoredDatetime = latestTag["commit"]["authored_date"]
    commitCommittedDatetime = latestTag["commit"]["committed_date"]
    print("GitLab triggered release for commit %s tagged as %s" % (commitId, tagName))

triggerState = newTriggerState
