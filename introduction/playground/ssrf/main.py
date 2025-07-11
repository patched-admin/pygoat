import os
from pathlib import Path


def ssrf_lab(file):
    try:
        base_dir = Path(__file__).parent
        file_path = base_dir / file
        
        # Ensure the file path doesn't escape the base directory
        if not str(file_path.resolve()).startswith(str(base_dir.resolve())):
            return {"blog": "Access denied: Invalid path"}
            
        with open(file_path, "r") as f:
            data = f.read()
        return {"blog": data}
    except FileNotFoundError:
        return {"blog": "No blog found"}
    except (PermissionError, OSError) as e:
        return {"blog": "Error accessing file"}