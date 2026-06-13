#!/usr/bin/env python3
import subprocess
import sys
import shutil
import http.server
import socketserver
import os

PORT = 8000
PUBLIC_DIR = "public"

def check_hugo():
    if not shutil.which("hugo"):
        print("Error: 'hugo' is not installed or not in your PATH.", file=sys.stderr)
        print("To install it on macOS, please run:", file=sys.stderr)
        print("  brew install hugo", file=sys.stderr)
        sys.exit(1)

def run_hugo_server():
    check_hugo()
    print("Starting Hugo's native server with live-reload on http://localhost:1313 ...")
    try:
        subprocess.run(["hugo", "server", "-D"])
    except KeyboardInterrupt:
        print("\nStopping Hugo server.")

def run_python_server():
    check_hugo()
    print("Compiling Hugo site to static files...")
    # Clean previous public dir if it exists
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    
    # Run hugo build
    result = subprocess.run(["hugo", "--minify"])
    if result.returncode != 0:
        print("Error: Hugo build failed.", file=sys.stderr)
        sys.exit(1)
        
    # Change directory to public to serve files from it
    os.chdir(PUBLIC_DIR)
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        pass
        
    print(f"Serving static site from '{PUBLIC_DIR}/' at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Python web server.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--static":
        run_python_server()
    else:
        run_hugo_server()
