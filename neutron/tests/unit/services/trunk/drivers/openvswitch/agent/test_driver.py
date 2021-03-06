# Copyright 2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock

from neutron.api.rpc.callbacks import resources
from neutron.services.trunk.drivers.openvswitch.agent import driver
from neutron.tests import base


class OvsTrunkSkeletonTest(base.BaseTestCase):

    @mock.patch("neutron.api.rpc.callbacks.resource_manager."
                "ConsumerResourceCallbacksManager.unregister")
    def test___init__(self, mocked_unregister):
        test_obj = driver.OVSTrunkSkeleton(mock.ANY)
        mocked_unregister.assert_called_with(test_obj.handle_trunks,
                                             resources.TRUNK)
