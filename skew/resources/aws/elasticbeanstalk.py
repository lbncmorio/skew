# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from skew.resources.aws import AWSResource


class Application(AWSResource):

    class Meta(object):
        service = 'elasticbeanstalk'
        type = 'application'
        resourcegroups_tagging = False
        enum_spec = ('describe_applications', 'Applications', None)
        detail_spec = None
        id = 'ApplicationName'
        filter_name = None
        filter_type = None
        name = 'ApplicationName'
        date = None
        dimension = None

class Environment(AWSResource):

    class Meta(object):
        service = 'elasticbeanstalk'
        type = 'environment'
        resourcegroups_tagging = True
        enum_spec = ('describe_environments', 'Environments', None)
        detail_spec = None
        id = 'EnvironmentName'
        filter_name = None
        filter_type = None
        name = 'EnvironmentName'
        date = None
        dimension = None

    @property
    def arn(self):
        return self.data['EnvironmentArn']
