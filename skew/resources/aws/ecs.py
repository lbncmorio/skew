# Copyright (c) 2014 Scopely, Inc.
# Copyright (c) 2015 Mitch Garnaat
#
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

import logging

import jmespath

from skew.resources.aws import AWSResource


LOG = logging.getLogger(__name__)


class Cluster(AWSResource):

    class Meta(object):
        service = 'ecs'
        type = 'cluster'
        resourcegroups_tagging = False
        enum_spec = ('list_clusters', 'clusterArns', None)
        detail_spec = ('describe_clusters', 'clusters', 'clusters[0]')
        id = None
        tags_spec = ('list_tags_for_resource', 'tags[]',
                     'resourceArn', 'arn')

        filter_name = None
        name = 'clusterName'
        date = None
        dimension = None

    @property
    def arn(self):
        return self.data['clusterArn']

    def __init__(self, client, data, query=None):
        super(Cluster, self).__init__(client, data, query)
        self._id = data
        detail_op, param_name, detail_path = self.Meta.detail_spec
        params = {param_name: [self.id]}
        data = client.call(detail_op, **params)
        self.data = jmespath.search(detail_path, data)


class TaskDefinition(AWSResource):

    class Meta(object):
        service = 'ecs'
        type = 'task-definition'
        resourcegroups_tagging = False
        enum_spec = ('list_task_definitions', 'taskDefinitionArns', None)
        detail_spec = ('describe_task_definition', 'taskDefinition', 'taskDefinition')
        id = None
        name = None
        filter_name = None
        date = None
        dimension = None

    def __init__(self, client, data, query=None):
        super(TaskDefinition, self).__init__(client, data, query)
        self._id = data
        detail_op, param_name, detail_path = self.Meta.detail_spec
        params = {param_name: self.id}
        data = client.call(detail_op, **params)
        self.data = jmespath.search(detail_path, data)

    @property
    def arn(self):
        return self.data['taskDefinitionArn']