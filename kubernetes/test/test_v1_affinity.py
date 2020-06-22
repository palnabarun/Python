# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_affinity import V1Affinity  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1Affinity(unittest.TestCase):
    """V1Affinity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Affinity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_affinity.V1Affinity()  # noqa: E501
        if include_optional :
            return V1Affinity(
                node_affinity = kubernetes.client.models.v1/node_affinity.v1.NodeAffinity(
                    preferred_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.v1/preferred_scheduling_term.v1.PreferredSchedulingTerm(
                            preference = kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                                match_expressions = [
                                    kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_fields = [
                                    kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                        key = '0', 
                                        operator = '0', )
                                    ], ), 
                            weight = 56, )
                        ], 
                    required_during_scheduling_ignored_during_execution = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                        node_selector_terms = [
                            kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm()
                            ], ), ), 
                pod_affinity = kubernetes.client.models.v1/pod_affinity.v1.PodAffinity(
                    preferred_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.v1/weighted_pod_affinity_term.v1.WeightedPodAffinityTerm(
                            pod_affinity_term = kubernetes.client.models.v1/pod_affinity_term.v1.PodAffinityTerm(
                                label_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                                    match_expressions = [
                                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                            key = '0', 
                                            operator = '0', 
                                            values = [
                                                '0'
                                                ], )
                                        ], 
                                    match_labels = {
                                        'key' : '0'
                                        }, ), 
                                namespaces = [
                                    '0'
                                    ], 
                                topology_key = '0', ), 
                            weight = 56, )
                        ], 
                    required_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.v1/pod_affinity_term.v1.PodAffinityTerm(
                            topology_key = '0', )
                        ], ), 
                pod_anti_affinity = kubernetes.client.models.v1/pod_anti_affinity.v1.PodAntiAffinity(
                    preferred_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.v1/weighted_pod_affinity_term.v1.WeightedPodAffinityTerm(
                            pod_affinity_term = kubernetes.client.models.v1/pod_affinity_term.v1.PodAffinityTerm(
                                label_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                                    match_expressions = [
                                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                            key = '0', 
                                            operator = '0', 
                                            values = [
                                                '0'
                                                ], )
                                        ], 
                                    match_labels = {
                                        'key' : '0'
                                        }, ), 
                                namespaces = [
                                    '0'
                                    ], 
                                topology_key = '0', ), 
                            weight = 56, )
                        ], 
                    required_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.v1/pod_affinity_term.v1.PodAffinityTerm(
                            topology_key = '0', )
                        ], )
            )
        else :
            return V1Affinity(
        )

    def testV1Affinity(self):
        """Test V1Affinity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
