# Kubernetes MCP Server - Production Ready

A production-ready Model Context Protocol (MCP) server for Kubernetes observability and debugging.

## 🚀 What This Provides

- **MCP Server**: Standardized interface for Kubernetes cluster access
- **Real-time Data**: Live access to pods, services, nodes, and events
- **Debugging Tools**: Built-in tools for cluster health and issue analysis
- **Production Ready**: Clean, tested code ready for production use

## 📋 Prerequisites

- Kubernetes cluster (local or remote)
- kubectl configured and working
- Python 3.11+
- pip package manager

## 🛠️ Quick Setup

### 1. Clone the Repository
```bash
git clone https://github.com/vivekbala/mcp.git
cd mcp
```

### 2. Install Dependencies
```bash
python3.11 -m pip install -r requirements.txt
```

### 3. Verify Setup
```bash
python3.11 verify_setup.py
```

## 🔧 MCP Server Features

### Resources Available
- `k8s://pods` - All pods with status and details
- `k8s://services` - Services with endpoints and connectivity info
- `k8s://nodes` - Node health and capacity info
- `k8s://events` - Recent cluster events for troubleshooting
- `k8s://deployments` - Deployment status and replica info

### Tools Available
- `cluster_health_check` - Comprehensive health analysis
- `check_pod_status` - Pod status and issue identification
- `analyze_service_connectivity` - Service endpoint analysis
- `get_pod_logs` - Log retrieval and analysis

## 📱 Usage Examples

### Basic Demo
```bash
python3.11 demo_script.py
```

### Debugging Demo
```bash
python3.11 debug_demo.py
```

### Run MCP Server
```bash
python3.11 mcp_server.py
```

## 🔗 Integration Options

### Claude Desktop
```json
{
  "mcpServers": {
    "kubernetes-observability": {
      "command": "python3.11",
      "args": ["/path/to/mcp_server.py"],
      "env": {
        "KUBECONFIG": "/path/to/kubeconfig"
      }
    }
  }
}
```

### Custom Clients
- Use the MCP client libraries
- Build custom debugging interfaces
- Integrate with existing monitoring tools

## 📚 Learning Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Python MCP Library](https://github.com/anthropics/anthropic-cookbook)

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this MCP server.

## 📄 License

This project is open source and available under the MIT License.

---

**Ready to debug Kubernetes like a pro?** 🚀

Clone this repo and start debugging your cluster issues today!
