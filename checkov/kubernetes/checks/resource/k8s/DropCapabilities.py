from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.checks.resource.base_spec_check import BaseK8Check


class DropCapabilities(BaseK8Check):

    def __init__(self):
        # CIS-1.3 1.7.7
        # CIS-1.5 5.2.7
        # NET_RAW allows a process to spy on packets on its network
        name = "Minimize the admission of containers with the NET_RAW capability"
        id = "CKV_K8S_28"
        # Location: container .securityContext.capabilities.drop
        supported_kind = ['containers', 'initContainers']
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_kind)

    def scan_spec_conf(self, conf):
        if conf.get("securityContext"):
            if conf["securityContext"].get("capabilities"):
                if conf["securityContext"]["capabilities"].get("drop"):
                    for d in conf["securityContext"]["capabilities"]["drop"]:
                        if any(cap in d for cap in ("ALL", "all", "NET_RAW")):
                            return CheckResult.PASSED
        return CheckResult.FAILED


check = DropCapabilities()
