#!/bin/bash
# Quick Start Script for Kubernetes MCP Server

echo "🚀 Kubernetes MCP Server - Quick Start"
echo "======================================"

# Check if kubectl is available
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl not found. Please install kubectl first."
    exit 1
fi

# Check if Python 3.11+ is available
if ! command -v python3.11 &> /dev/null; then
    echo "❌ Python 3.11 not found. Please install Python 3.11+ first."
    exit 1
fi

# Check cluster connectivity
echo "🔍 Checking Kubernetes cluster..."
if ! kubectl cluster-info &> /dev/null; then
    echo "❌ Cannot connect to Kubernetes cluster. Please check your kubeconfig."
    exit 1
fi

echo "✅ Kubernetes cluster is accessible"

# Install dependencies
echo "📦 Installing Python dependencies..."
python3.11 -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Run verification
echo "🔍 Running setup verification..."
python3.11 verify_setup.py

if [ $? -eq 0 ]; then
    echo "✅ Setup verification completed"
else
    echo "❌ Setup verification failed"
    exit 1
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "Next steps:"
echo "1. Run demo: python3.11 demo_script.py"
echo "2. Run debugging demo: python3.11 debug_demo.py"
echo "3. Start MCP server: python3.11 mcp_server.py"
echo ""
echo "Happy debugging! 🚀"
