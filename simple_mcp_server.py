#!/usr/bin/env python3.11
"""
Simple Kubernetes MCP Server for Testing
"""

import asyncio
import json
import subprocess
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Resource, Tool, TextContent

class SimpleK8sMCPServer:
    def __init__(self):
        self.server = Server("kubernetes-observability")
        self.setup_handlers()
    
    def setup_handlers(self):
        @self.server.list_resources()
        async def list_resources():
            return [
                Resource(
                    uri="k8s://pods",
                    name="Kubernetes Pods",
                    description="All pods in the cluster",
                    mimeType="application/json"
                ),
                Resource(
                    uri="k8s://services",
                    name="Kubernetes Services",
                    description="All services in the cluster",
                    mimeType="application/json"
                ),
                Resource(
                    uri="k8s://nodes",
                    name="Kubernetes Nodes",
                    description="All nodes in the cluster",
                    mimeType="application/json"
                ),
                Resource(
                    uri="k8s://events",
                    name="Kubernetes Events",
                    description="Recent cluster events",
                    mimeType="application/json"
                )
            ]
        
        @self.server.read_resource()
        async def read_resource(uri: str) -> str:
            try:
                if uri == "k8s://pods":
                    result = subprocess.run(
                        ["kubectl", "get", "pods", "--all-namespaces", "-o", "json"],
                        capture_output=True, text=True
                    )
                    return result.stdout
                elif uri == "k8s://services":
                    result = subprocess.run(
                        ["kubectl", "get", "services", "--all-namespaces", "-o", "json"],
                        capture_output=True, text=True
                    )
                    return result.stdout
                elif uri == "k8s://nodes":
                    result = subprocess.run(
                        ["kubectl", "get", "nodes", "-o", "json"],
                        capture_output=True, text=True
                    )
                    return result.stdout
                elif uri == "k8s://events":
                    result = subprocess.run(
                        ["kubectl", "get", "events", "--all-namespaces", "-o", "json"],
                        capture_output=True, text=True
                    )
                    return result.stdout
                else:
                    return json.dumps({"error": f"Unknown resource: {uri}"})
            except Exception as e:
                return json.dumps({"error": str(e)})
        
        @self.server.list_tools()
        async def list_tools():
            return [
                Tool(
                    name="cluster_health_check",
                    description="Perform a basic cluster health check",
                    inputSchema={"type": "object", "properties": {}}
                ),
                Tool(
                    name="check_pod_status",
                    description="Check the status of pods in a namespace",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "namespace": {
                                "type": "string",
                                "description": "Namespace to check (default: all namespaces)"
                            }
                        }
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict) -> list:
            if name == "cluster_health_check":
                try:
                    # Check pods
                    result = subprocess.run(
                        ["kubectl", "get", "pods", "--all-namespaces"],
                        capture_output=True, text=True
                    )
                    return [TextContent(type="text", text=result.stdout)]
                except Exception as e:
                    return [TextContent(type="text", text=f"Error: {str(e)}")]
            elif name == "check_pod_status":
                try:
                    namespace = arguments.get("namespace", "all")
                    if namespace == "all":
                        cmd = ["kubectl", "get", "pods", "--all-namespaces"]
                    else:
                        cmd = ["kubectl", "get", "pods", "-n", namespace]
                    
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    return [TextContent(type="text", text=result.stdout)]
                except Exception as e:
                    return [TextContent(type="text", text=f"Error: {str(e)}")]
            else:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    async def run(self):
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="kubernetes-observability",
                    server_version="1.0.0",
                    capabilities={
                        "resources": {},
                        "tools": {}
                    }
                )
            )

async def main():
    server = SimpleK8sMCPServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
