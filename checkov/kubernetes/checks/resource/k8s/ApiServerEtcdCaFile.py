from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.checks.resource.base_spec_check import BaseK8Check
from checkov.kubernetes.checks.resource.k8s.k8s_check_utils import extract_commands


class ApiServerEtcdCaFile(BaseK8Check):
    def __init__(self):
        id = "CKV_K8S_102"
        name = "Ensure that the --etcd-ca-file argument is set as appropriate"
        categories = [CheckCategories.KUBERNETES]
        supported_entities = ['containers']
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_entities)

    def scan_spec_conf(self, conf):
        keys, values = extract_commands(conf)

        if "kube-apiserver" in keys:
            if '--etcd-ca-file' not in keys:
                return CheckResult.FAILED

        return CheckResult.PASSED


check = ApiServerEtcdCaFile()
