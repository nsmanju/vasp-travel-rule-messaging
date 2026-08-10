import json
from datetime import datetime

class TravelRuleMessenger:
    def __init__(self, vasp_code):
        self.vasp_code = vasp_code
        self.threshold_hkd = 8000

    def create_payload(self, originator, beneficiary, amount, asset="BTC"):
        return {
            "originator_vasp": self.vasp_code,
            "timestamp": datetime.utcnow().isoformat(),
            "transaction": {"amount": amount, "asset": asset, "threshold_triggered": amount >= 8000},
            "ivms101": {"originator": originator, "beneficiary": beneficiary}
        }

if __name__ == "__main__":
    m = TravelRuleMessenger("OSL123")
    print(json.dumps(m.create_payload({"name":"Chan"}, {"name":"Lee"}, 15000), indent=2))
