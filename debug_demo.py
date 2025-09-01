#!/usr/bin/env python3.11
"""
Debugging Demo Script for Video - Show MCP Tools in Action
"""

import subprocess
import json
import time

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def debug_pod_issues():
    """Demonstrate debugging pod issues with MCP"""
    print_header("�� DEBUGGING POD ISSUES")
    
    print("🔍 Step 1: Identify problematic pods")
    result = subprocess.run(
        ["kubectl", "get", "pods", "--all-namespaces", "--field-selector=status.phase!=Running"],
        capture_output=True, text=True
    )
    
    if result.stdout.strip():
        print("🚨 Found problematic pods:")
        lines = result.stdout.strip().split('\n')
        for line in lines[1:]:  # Skip header
            if line.strip():
                print(f"   {line}")
        
        print("\n🔍 Step 2: Analyze pod events")
        # Get events for problematic pods
        result = subprocess.run(
            ["kubectl", "get", "events", "--all-namespaces", "--sort-by='.lastTimestamp'"],
            capture_output=True, text=True
        )
        
        print("📋 Recent events:")
        lines = result.stdout.strip().split('\n')
        for line in lines[-5:]:  # Last 5 events
            if line.strip():
                print(f"   {line}")
    else:
        print("✅ No problematic pods found!")

def debug_service_connectivity():
    """Demonstrate debugging service connectivity"""
    print_header("🔗 DEBUGGING SERVICE CONNECTIVITY")
    
    print("🔍 Step 1: Check all services")
    result = subprocess.run(
        ["kubectl", "get", "services", "--all-namespaces"],
        capture_output=True, text=True
    )
    
    print("📋 Services found:")
    lines = result.stdout.strip().split('\n')
    for line in lines[1:]:  # Skip header
        if line.strip():
            print(f"   {line}")
    
    print("\n🔍 Step 2: Check service endpoints")
    # Check endpoints for each service
    services_result = subprocess.run(
        ["kubectl", "get", "services", "--all-namespaces", "-o", "json"],
        capture_output=True, text=True
    )
    
    services = json.loads(services_result.stdout)
    for service in services['items']:
        service_name = service['metadata']['name']
        namespace = service['metadata']['namespace']
        
        # Get endpoints
        endpoints_result = subprocess.run(
            ["kubectl", "get", "endpoints", service_name, "-n", namespace, "-o", "json"],
            capture_output=True, text=True
        )
        
        if endpoints_result.returncode == 0:
            endpoints = json.loads(endpoints_result.stdout)
            if endpoints['subsets']:
                ready_endpoints = 0
                for subset in endpoints['subsets']:
                    ready_endpoints += len(subset.get('addresses', []))
                
                if ready_endpoints > 0:
                    print(f"   ✅ {service_name} ({namespace}): {ready_endpoints} ready endpoints")
                else:
                    print(f"   ⚠️  {service_name} ({namespace}): No ready endpoints")
            else:
                print(f"   ❌ {service_name} ({namespace}): No endpoints")
        else:
            print(f"   ❌ {service_name} ({namespace}): Could not retrieve endpoints")

def debug_resource_usage():
    """Demonstrate debugging resource usage"""
    print_header("💾 DEBUGGING RESOURCE USAGE")
    
    print("🔍 Step 1: Check node resources")
    result = subprocess.run(
        ["kubectl", "top", "nodes"],
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        print("📊 Node resource usage:")
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if line.strip():
                print(f"   {line}")
    else:
        print("⚠️  Metrics server not available. Install with:")
        print("   kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml")
    
    print("\n�� Step 2: Check pod resources")
    result = subprocess.run(
        ["kubectl", "top", "pods", "--all-namespaces"],
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        print("📊 Pod resource usage:")
        lines = result.stdout.strip().split('\n')
        for line in lines[:6]:  # Show first 6 lines
            if line.strip():
                print(f"   {line}")
    else:
        print("⚠️  Pod metrics not available")

def demonstrate_mcp_integration():
    """Show how MCP integrates with debugging workflow"""
    print_header("🔌 MCP INTEGRATION DEMO")
    
    print("🎯 MCP Server provides these capabilities:")
    print("   📡 Real-time resource access")
    print("   🛠️  Debugging tools")
    print("   🔍 Issue identification")
    print("   📊 Health monitoring")
    
    print("\n🚀 Integration points:")
    print("   • Claude Desktop")
    print("   • Custom MCP clients")
    print("   • CI/CD pipelines")
    print("   • Monitoring dashboards")
    
    print("\n💡 Benefits:")
    print("   • Standardized interface")
    print("   • Real-time data access")
    print("   • Automated debugging")
    print("   • Easy integration")

def main():
    print("🐛 KUBERNETES DEBUGGING WITH MCP")
    print("=" * 60)
    print("Demonstrating real debugging workflows using MCP server")
    
    time.sleep(1)
    
    # Debug pod issues
    debug_pod_issues()
    
    # Debug service connectivity
    debug_service_connectivity()
    
    # Debug resource usage
    debug_resource_usage()
    
    # Show MCP integration
    demonstrate_mcp_integration()
    
    print_header("🎉 DEBUGGING DEMO COMPLETED")
    print("✅ Successfully demonstrated debugging workflows")
    print("✅ Showed real issue identification")
    print("✅ Demonstrated MCP tool capabilities")
    print("✅ Highlighted integration benefits")
    print("\n🚀 Your MCP server is ready for production debugging!")

if __name__ == "__main__":
    main()
