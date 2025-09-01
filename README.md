# Kubernetes MCP Server - Complete Setup & Demo

A production-ready Model Context Protocol (MCP) server for Kubernetes observability and debugging.

## 🚀 What This Provides

- **MCP Server**: Standardized interface for Kubernetes cluster access
- **Real-time Data**: Live access to pods, services, nodes, and events
- **Debugging Tools**: Built-in tools for cluster health and issue analysis
- **Video Demo**: Complete scripts for video creation and demonstration

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
python3.11 -m pip install mcp kubernetes
```

### 3. Verify Setup
```bash
python3.11 verify_setup.py
```

## 🎬 Video Creation Workflow

This repository contains everything needed to create a video about Kubernetes MCP servers:

### Core Files
- `mcp_server.py` - Production-ready MCP server
- `demo_script.py` - Enhanced demonstration script
- `debug_demo.py` - Debugging workflow demonstration
- `video_script.md` - Complete video script with timestamps

### Video Scenes
1. **Introduction** (0:00-0:30) - Overview and benefits
2. **Prerequisites** (0:30-1:00) - Verify kubectl and Python
3. **Installation** (1:00-2:00) - Install MCP packages
4. **Project Setup** (2:00-2:30) - Create directory structure
5. **Server Creation** (2:30-4:00) - Build MCP server
6. **Testing** (4:00-5:30) - Verify server functionality
7. **Capabilities** (5:30-8:00) - Demonstrate real cluster access
8. **Debugging** (8:00-10:00) - Show debugging tools
9. **Integration** (10:00-11:00) - Connect with other tools
10. **Conclusion** (11:00-12:00) - Summary and next steps

## 🔧 MCP Server Features

### Resources Available
- `k8s://pods` - All pods with status and details
- `k8s://services` - Services with endpoints
- `k8s://nodes` - Node health and capacity
- `k8s://events` - Recent cluster events
- `k8s://deployments` - Deployment status

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

## 🎥 Recording Tips

### Screen Recording
- Use **Loom** for quick recordings
- Use **OBS Studio** for professional quality
- Use **ScreenFlow** (macOS) for advanced editing

### Audio
- Record in quiet environment
- Use external microphone if possible
- Speak clearly and at moderate pace

### Visual Elements
- Use terminal with dark theme for better contrast
- Zoom in on important code sections
- Highlight key outputs and results

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

## 🎯 Video Success Metrics

- **Engagement**: Viewers download and try the code
- **Learning**: Clear understanding of MCP benefits
- **Action**: Implementation in their own environments
- **Community**: Questions and discussions in comments

---

**Ready to debug Kubernetes like a pro?** 🚀

Clone this repo and follow along with the video to build your own MCP server!
