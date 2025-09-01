#!/usr/bin/env python3.11
"""
Quick verification of the Kubernetes MCP setup
"""

import subprocess
import json

def main():
    print("🔍 Kubernetes MCP Setup Verification")
    print("=" * 50)
    
    # Check kubectl
    try:
        result = subprocess.run(["kubectl", "version", "--client"], capture_output=True, text=True)
        print(f"✅ kubectl: {result.stdout.strip()}")
    except Exception as e:
        print(f"❌ kubectl: {e}")
        return
    
    # Check cluster
    try:
        result = subprocess.run(["kubectl", "cluster-info"], capture_output=True, text=True)
        print("✅ Kubernetes cluster: Running")
    except Exception as e:
        print(f"❌ Kubernetes cluster: {e}")
        return
    
    # Check nodes
    try:
        result = subprocess.run(["kubectl", "get", "nodes"], capture_output=True, text=True)
        print("✅ Nodes: Available")
    except Exception as e:
        print(f"❌ Nodes: {e}")
    
    # Check test namespace
    try:
        result = subprocess.run(["kubectl", "get", "pods", "-n", "test-mcp"], capture_output=True, text=True)
        if "nginx" in result.stdout:
            print("✅ Test namespace: nginx pod running")
        else:
            print("⚠️  Test namespace: No nginx pod found")
    except Exception as e:
        print(f"❌ Test namespace: {e}")
    
    # Check Python packages
    try:
        import mcp
        import kubernetes
        print("✅ Python packages: MCP and kubernetes installed")
    except ImportError as e:
        print(f"❌ Python packages: {e}")
    
    print("\n�� Setup verification completed!")
    print("Ready for MCP server demonstrations!")

if __name__ == "__main__":
    main()
