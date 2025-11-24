
import argparse
import random
import json

class IoTProvisioningSimulator:
    def __init__(self, ssid, password, num_devices):
        self.ssid = ssid
        self.password = password
        self.devices = self._generate_devices(num_devices)
        self.connection_log = []

    def _generate_devices(self, num_devices):
        return [{"id": f"device_{i+1}", "status": "disconnected"} for i in range(num_devices)]

    def connect_devices(self):
        print(f"Connecting {len(self.devices)} devices to SSID '{self.ssid}'...")
        for device in self.devices:
            success = self._attempt_connection()
            device["status"] = "connected" if success else "failed"
            self.connection_log.append({"device": device["id"], "status": device["status"]})
        print("Connection attempt complete.")

    def _attempt_connection(self):
        # Simulate connection success rate (80%)
        return random.random() < 0.8

    def troubleshoot_failed_connections(self):
        print("Retrying failed connections...")
        for device in self.devices:
            if device["status"] == "failed":
                success = self._attempt_connection()
                device["status"] = "connected" if success else "failed"
                self.connection_log.append({
                    "device": device["id"],
                    "status": device["status"],
                    "retry": True
                })
        print("Troubleshooting complete.")

    def export_log(self, filename="connection_log.json"):
        with open(filename, "w") as f:
            json.dump(self.connection_log, f, indent=4)
        print(f"Connection log exported to {filename}.")

def main():
    parser = argparse.ArgumentParser(description="IoT Device Provisioning Simulator")
    parser.add_argument("--ssid", type=str, required=True, help="Wi-Fi SSID")
    parser.add_argument("--password", type=str, required=True, help="Wi-Fi Password")
    parser.add_argument("--devices", type=int, default=10, help="Number of IoT devices to simulate")
    parser.add_argument("--logfile", type=str, default="connection_log.json", help="Output log file name")

    args = parser.parse_args()

    simulator = IoTProvisioningSimulator(ssid=args.ssid, password=args.password, num_devices=args.devices)
    simulator.connect_devices()
    simulator.troubleshoot_failed_connections()
    simulator.export_log(filename=args.logfile)

if __name__ == "__main__":
    main()
