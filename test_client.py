#!/usr/bin/env python3.11
"""
Test client for Simple Kubernetes MCP Server
"""

import asyncio
import os
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

async def test_simple_server():
    """Test the MCP server functionality"""
    
    # Configure server parameters
    server_params = StdioServerParameters(
        command="python3.11",
        args=["simple_mcp_server.py"]
    )
    
    print("🚀 Testing Simple Kubernetes MCP Server...")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                
                # Test 1: List available resources
                print("\n📋 Available Resources:")
                resources = await session.list_resources()
                for resource in resources:
                    print(f"  - {resource.name}: {resource.uri}")
                
                # Test 2: Read pods
                print("\n📦 Pods in Cluster:")
                pods_data = await session.read_resource("k8s://pods")
                print("✅ Successfully retrieved pod data")
                print(f"   Data length: {len(pods_data)} characters")
                
                # Test 3: Read services
                print("\n🔗 Services in Cluster:")
                services_data = await session.read_resource("k8s://services")
                print("✅ Successfully retrieved service data")
                print(f"   Data length: {len(services_data)} characters")
                
                # Test 4: List tools
                print("\n🛠️  Available Tools:")
                tools = await session.list_tools()
                for tool in tools:
                    print(f"  - {tool.name}: {tool.description}")
                
                # Test 5: Test health check tool
                print("\n🏥 Cluster Health Check:")
                health_result = await session.call_tool("cluster_health_check", {})
                if health_result:
                    print("✅ Health check completed successfully")
                    print("   Sample output:")
                    lines = health_result[0].text.split('\n')[:5]  # First 5 lines
                    for line in lines:
                        if line.strip():
                            print(f"   {line}")
                
                # Test 6: Test pod status check
                print("\n📊 Pod Status Check (test-mcp namespace):")
                pod_status_result = await session.call_tool("check_pod_status", {"namespace": "test-mcp"})
                if pod_status_result:
                    print("✅ Pod status check completed successfully")
                    print("   Output:")
                    lines = pod_status_result[0].text.split('\n')
                    for line in lines:
                        if line.strip():
                            print(f"   {line}")
                
                print("\n✅ All tests completed successfully!")
                print("🎉 Your MCP server is working correctly!")
                
    except Exception as e:
        print(f"❌ Error testing MCP server: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = asyncio.run(test_simple_server())
    exit(0 if success else 1)
