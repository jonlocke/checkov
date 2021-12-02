from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.checks.resource.base_spec_check import BaseK8Check


class ApiServerTokenAuthFile(BaseK8Check):
    def __init__(self):
        id = "CKV_K8S_70"
        name = "Ensure that the --token-auth-file argument is not set"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def scan_spec_conf(self, conf):
        if conf.get("command") is not None:
            if "kube-apiserver" in conf["command"]:
                if any(x.startswith('--token-auth-file') for x in conf["command"]):
                    return CheckResult.FAILED

        return CheckResult.PASSED


check = ApiServerTokenAuthFile()
