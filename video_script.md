# Video Script: Kubernetes MCP Server Setup & Testing

## Scene 1: Introduction (0:00-0:30)
**Narration**: "Today I'll show you how to set up a Model Context Protocol server for Kubernetes observability. This will give you powerful debugging capabilities for your cluster."

**On-screen text**: "Kubernetes MCP Server Setup" | "Debug Your Cluster with MCP"

## Scene 2: Prerequisites Check (0:30-1:00)
**Action**: Show that kubectl and Python are already available
**Commands to run**:
```bash
kubectl version --client
python3.11 --version
```

**Narration**: "First, let's verify we have kubectl and Python 3.11 available. These are the only prerequisites you need."

## Scene 3: Install Dependencies (1:00-2:00)
**Action**: Install MCP and kubernetes packages
**Commands to run**:
```bash
python3.11 -m pip install mcp kubernetes
```

**Narration**: "Now let's install the required Python packages. We need MCP for the protocol and kubernetes for cluster access."

## Scene 4: Create Project Structure (2:00-2:30)
**Action**: Create project directory and files
**Commands to run**:
```bash
mkdir kubernetes-mcp-demo
cd kubernetes-mcp-demo
```

**Narration**: "Let's create a clean project directory for our MCP server."

## Scene 5: Create MCP Server (2:30-4:00)
**Action**: Create and explain the MCP server code
**File to create**: `mcp_server.py`
**Narration**: "Here's our MCP server that provides Kubernetes observability. It can list resources, read data, and execute debugging tools."

## Scene 6: Test MCP Server (4:00-5:30)
**Action**: Run the server and test functionality
**Commands to run**:
```bash
python3.11 mcp_server.py
```

**Narration**: "Let's test our MCP server to make sure it's working correctly."

## Scene 7: Demonstrate Capabilities (5:30-8:00)
**Action**: Show real cluster data through MCP
**Commands to run**:
```bash
python3.11 demo_script.py
```

**Narration**: "Now let's see what our MCP server can do. It's accessing real Kubernetes cluster data and providing observability insights."

## Scene 8: Debugging Workflow (8:00-10:00)
**Action**: Show debugging tools in action
**Commands to run**:
```bash
python3.11 debug_demo.py
```

**Narration**: "Let's demonstrate how to use MCP for debugging. We can check pod status, analyze services, and perform health checks."

## Scene 9: Integration Example (10:00-11:00)
**Action**: Show how to integrate with other tools
**Narration**: "This MCP server can be integrated with Claude Desktop, custom clients, or any MCP-compatible tool."

## Scene 10: Conclusion (11:00-12:00)
**Action**: Summary and next steps
**Narration**: "You now have a powerful MCP server for Kubernetes observability. Start debugging your cluster issues today!"

**On-screen text**: "Start Building Your MCP Server!" | "Debug Kubernetes Like a Pro"
