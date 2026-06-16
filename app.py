from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        {"title":"Secure Azure Storage with Private Endpoints","problem":"Storage needed to be locked down without account keys or SAS tokens.","solution":"Configured Private Endpoint, Private DNS, Managed Identity, and Azure RBAC.","tech":["Storage Account","Private Endpoint","Private DNS","RBAC","Managed Identity"],"result":"Blob access worked privately through Entra authentication with public access disabled."},
        {"title":"Hub-Spoke Network with Azure Bastion","problem":"Administrators needed secure VM access without exposing public IPs.","solution":"Built hub-spoke VNets, Bastion, NSGs, and route controls.","tech":["VNet Peering","Azure Bastion","NSG","UDR","Windows Server"],"result":"VMs were reachable through Bastion only, with no direct RDP exposure."},
        {"title":"Key Vault with Managed Identity","problem":"Application secrets needed to be removed from configuration files.","solution":"Enabled system-assigned identity and assigned Key Vault Secrets User permissions.","tech":["Key Vault","Managed Identity","Azure RBAC","Private Endpoint"],"result":"Application identity retrieved secrets securely without stored credentials."},
        {"title":"Azure Backup and VM Recovery","problem":"A critical VM needed restore testing and file-level recovery validation.","solution":"Configured Recovery Services Vault, backup policy, recovery points, and restore testing.","tech":["Recovery Services Vault","Azure Backup","VM Restore","File Recovery"],"result":"Validated file-level and full VM recovery scenarios."},
        {"title":"Containerized Python Portfolio","problem":"Needed a portable showcase website for employers.","solution":"Built a Flask website, containerized it with Docker, and deployed it to Azure.","tech":["Python","Flask","Docker","ACR","ACI"],"result":"Created a repeatable cloud-hosted portfolio deployment."},
        {"title":"Hybrid Environment Configuration Using Site to Site VPN","problem":"Client wanted to utilize a hybrid environment by having a secondary domain controller in Azure","solution":"Created Azure VPN GW, configured a S2S tunnel between Azure and client's Watchguard firewall. Spun up new Windows Server VM in Azure and configured secondary DC on domain.","tech":["Vnet","NSG","VNG","S2S","Active Directory"],"result":"Created intersite connectivity between Azure and on premise network for redundancy."},
        {"title":"ARM/Bicep Infrastructure Deployment","problem":"Infrastructure needed to be deployed consistently across environments.","solution":"Built reusable templates with parameters, variables, outputs, and dependencies.","tech":["ARM","Bicep","Azure CLI","PowerShell"],"result":"Improved repeatability and reduced manual deployment effort."}
    ]
    return render_template("index.html", projects=projects)

@app.route("/health")
def health():
    return {"status": "healthy", "app": "azure-portfolio-site"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
