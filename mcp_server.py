#!/usr/bin/env python3.11
"""
Kubernetes MCP Server - Production Ready Version
"""

import asyncio
import json
import subprocess
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Resource, Tool, TextContent

class KubernetesMCPServer:
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
                    description="All pods in the cluster with status and details",
                    mimeType="application/json"
                ),
                Resource(
                    uri="k8s://services",
                    name="Kubernetes Services",
                    description="All services with endpoints and connectivity info",
                    mimeType="application/json"
                ),
                Resource(
                    uri="k8s://nodes",
                    name="Kubernetes Nodes",
                    description="Cluster nodes with health and capacity info",
                    mimeType="application/json"
                ),
                Resource(
                    uri="k8s://events",
                    name="Kubernetes Events",
                    description="Recent cluster events for troubleshooting",
                    mimeType="application/json"
                ),
                Resource(
                    uri="k8s://deployments",
                    name="Kubernetes Deployments",
                    description="All deployments with replica status",
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
                elif uri == "k8s://deployments":
                    result = subprocess.run(
                        ["kubectl", "get", "deployments", "--all-namespaces", "-o", "json"],
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
                    description="Perform comprehensive cluster health check",
                    inputSchema={"type": "object", "properties": {}}
                ),
                Tool(
                    name="check_pod_status",
                    description="Check pod status and identify issues",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "namespace": {
                                "type": "string",
                                "description": "Namespace to check (default: all)"
                            }
                        }
                    }
                ),
                Tool(
                    name="analyze_service_connectivity",
                    description="Analyze service endpoints and connectivity",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "service_name": {
                                "type": "string",
                                "description": "Service name to analyze"
                            },
                            "namespace": {
                                "type": "string",
                                "description": "Namespace of the service"
                            }
                        }
                    }
                ),
                Tool(
                    name="get_pod_logs",
                    description="Retrieve and analyze pod logs",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "pod_name": {
                                "type": "string",
                                "description": "Name of the pod"
                            },
                            "namespace": {
                                "type": "string",
                                "description": "Namespace of the pod"
                            }
                        },
                        "required": ["pod_name", "namespace"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict) -> list:
            try:
                if name == "cluster_health_check":
                    result = subprocess.run(
                        ["kubectl", "get", "pods", "--all-namespaces"],
                        capture_output=True, text=True
                    )
                    return [TextContent(type="text", text=result.stdout)]
                
                elif name == "check_pod_status":
                    namespace = arguments.get("namespace", "all")
                    if namespace == "all":
                        cmd = ["kubectl", "get", "pods", "--all-namespaces"]
                    else:
                        cmd = ["kubectl", "get", "pods", "-n", namespace]
                    
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    return [TextContent(type="text", text=result.stdout)]
                
                elif name == "analyze_service_connectivity":
                    service_name = arguments.get("service_name")
                    namespace = arguments.get("namespace", "default")
                    
                    if not service_name:
                        return [TextContent(type="text", text="Error: service_name is required")]
                    
                    # Get service info
                    service_cmd = ["kubectl", "get", "service", service_name, "-n", namespace, "-o", "json"]
                    service_result = subprocess.run(service_cmd, capture_output=True, text=True)
                    
                    # Get endpoints info
                    endpoints_cmd = ["kubectl", "get", "endpoints", service_name, "-n", namespace, "-o", "json"]
                    endpoints_result = subprocess.run(endpoints_cmd, capture_output=True, text=True)
                    
                    analysis = f"Service Analysis for {service_name} in {namespace}:\n\n"
                    analysis += "Service Info:\n" + service_result.stdout + "\n\n"
                    analysis += "Endpoints Info:\n" + endpoints_result.stdout
                    
                    return [TextContent(type="text", text=analysis)]
                
                elif name == "get_pod_logs":
                    pod_name = arguments.get("pod_name")
                    namespace = arguments.get("namespace")
                    
                    if not pod_name or not namespace:
                        return [TextContent(type="text", text="Error: pod_name and namespace are required")]
                    
                    cmd = ["kubectl", "logs", pod_name, "-n", namespace, "--tail=50"]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    
                    if result.returncode != 0:
                        return [TextContent(type="text", text=f"Error getting logs: {result.stderr}")]
                    
                    return [TextContent(type="text", text=result.stdout)]
                
                else:
                    return [TextContent(type="text", text=f"Unknown tool: {name}")]
                    
            except Exception as e:
                return [TextContent(type="text", text=f"Error executing tool {name}: {str(e)}")]
    
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
    server = KubernetesMCPServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
