#!/usr/bin/env python3
"""
CareerLaunch AI Project Structure Generator
Run this script to create the complete folder structure for the project
"""

import os
import sys

def create_structure(base_path):
    """Create the complete folder structure for CareerLaunch AI"""
    
    structure = {
        'docs': {
            'system-requirements': [],
            'architecture': ['system-architecture-diagrams', 'database-schema', 'deployment-diagrams'],
            'compliance': [],
        },
        'src': {
            'backend': {
                'auth-service': ['src', 'tests'],
                'job-intelligence-service': {
                    'src': ['job-aggregation', 'job-enrichment', 'market-intelligence'],
                    'tests': []
                },
                'resume-service': {
                    'src': ['resume-parsing', 'resume-optimization', 'template-engine'],
                    'tests': []
                },
                'transparency-service': {
                    'src': ['application-analytics', 'competitive-positioning', 'success-patterns'],
                    'tests': []
                },
                'application-service': {
                    'src': ['application-tracking', 'status-management', 'performance-analytics'],
                    'tests': []
                },
                'analytics-service': {
                    'src': ['predictive-models', 'skill-roi-analysis', 'ml-pipelines'],
                    'tests': []
                },
                'api-gateway': ['src', 'tests']
            },
            'frontend': {
                'web-app': {
                    'public': [],
                    'src': {
                        'components': ['dashboard', 'resume-builder', 'job-search', 'analytics', 'shared'],
                        'pages': [],
                        'hooks': [],
                        'services': [],
                        'utils': [],
                        'styles': []
                    }
                },
                'browser-extension': {
                    'src': ['content-scripts', 'popup', 'background', 'options']
                }
            },
            'mobile': ['android', 'ios', 'src']  # Phase 4
        },
        'data': {
            'databases': ['postgres/migrations', 'redis', 'elasticsearch'],
            'data-warehouse': ['dbt-models', 'sql-scripts'],
            'ml-models': ['resume-analysis', 'success-prediction', 'training-scripts', 'model-evaluation']
        },
        'infrastructure': {
            'kubernetes': ['namespaces', 'deployments', 'services', 'configmaps', 'secrets'],
            'docker': [],
            'terraform': {
                'modules': [],
                'environments': ['dev', 'staging', 'prod']
            },
            'monitoring': ['prometheus', 'grafana', 'alerts']
        },
        'tests': ['unit', 'integration', 'e2e', 'performance', 'security'],
        'scripts': ['deployment', 'database', 'data-migration', 'backup-recovery'],
        'third-party-integrations': {
            'job-boards': ['linkedin', 'indeed', 'glassdoor'],
            'email-providers': [],
            'calendar-systems': [],
            'auth-providers': []
        },
        'config': {
            'app-config': [],
            'feature-flags': [],
            'environment': [],
            'nginx': []
        },
        'assets': {
            'templates': ['resume-templates', 'email-templates'],
            'images': [],
            'icons': [],
            'translations': []
        },
        '.github': {
            'workflows': [],
            'ISSUE_TEMPLATE': []
        }
    }

    # Root files
    root_files = [
        '.gitignore',
        'README.md',
        'package.json',
        'docker-compose.yml',
        'Makefile',
        'LICENSE',
        'ROADMAP.md'
    ]

    def create_directories(path, structure_dict):
        """Recursively create directories"""
        for name, contents in structure_dict.items():
            current_path = os.path.join(path, name)
            print(f"Creating: {current_path}")
            os.makedirs(current_path, exist_ok=True)
            
            if isinstance(contents, dict):
                create_directories(current_path, contents)
            elif isinstance(contents, list):
                for item in contents:
                    if '/' in item:  # Handle nested paths like 'postgres/migrations'
                        nested_path = os.path.join(current_path, item)
                        os.makedirs(nested_path, exist_ok=True)
                        print(f"Creating: {nested_path}")
                    else:
                        item_path = os.path.join(current_path, item)
                        os.makedirs(item_path, exist_ok=True)
                        print(f"Creating: {item_path}")

    print("🚀 Creating CareerLaunch AI Project Structure...")
    print("=" * 50)
    
    # Create base directory
    os.makedirs(base_path, exist_ok=True)
    print(f"Base directory: {base_path}")
    
    # Create all directories
    create_directories(base_path, structure)
    
    # Create root files
    print("\n📄 Creating root files...")
    for file in root_files:
        file_path = os.path.join(base_path, file)
        with open(file_path, 'w') as f:
            if file == 'README.md':
                f.write("# CareerLaunch AI\n\nTransform job seeking from speculative activity into data-driven, transparent process.\n")
            elif file == '.gitignore':
                f.write("# Dependencies\nnode_modules/\n\n# Environment variables\n.env\n.env.local\n\n# Logs\nlogs/\n*.log\n\n# OS\n.DS_Store\nThumbs.db\n\n# IDE\n.vscode/\n.idea/\n\n# Build outputs\ndist/\nbuild/\n*.tar.gz\n")
            elif file == 'docker-compose.yml':
                f.write("version: '3.8'\nservices:\n  # Development environment setup\n  postgres:\n    image: postgres:14\n    environment:\n      POSTGRES_DB: careerlaunch\n      POSTGRES_USER: admin\n      POSTGRES_PASSWORD: password\n    ports:\n      - \"5432:5432\"\n\n  redis:\n    image: redis:alpine\n    ports:\n      - \"6379:6379\"\n")
            else:
                f.write(f"# {file}\n\nPlaceholder content for {file}\n")
        print(f"Created: {file_path}")
    
    # Create essential configuration files
    print("\n⚙️  Creating configuration files...")
    config_files = {
        'config/environment/dev.env': 'NODE_ENV=development\nDB_HOST=localhost\nREDIS_URL=redis://localhost:6379\n',
        'config/environment/staging.env': 'NODE_ENV=staging\n',
        'config/environment/production.env': 'NODE_ENV=production\n',
        '.github/workflows/ci.yml': 'name: CI Pipeline\n\non: [push, pull_request]\n\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v2\n      - name: Run tests\n        run: echo "Tests will be implemented here"',
    }
    
    for file_path, content in config_files.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"Created: {full_path}")
    
    # Create placeholder files for key services
    print("\n🔧 Creating service placeholders...")
    service_files = [
        'src/backend/auth-service/package.json',
        'src/backend/job-intelligence-service/package.json',
        'src/backend/resume-service/package.json',
        'src/backend/transparency-service/package.json',
        'src/backend/application-service/package.json',
        'src/backend/analytics-service/package.json',
        'src/backend/api-gateway/package.json',
        'src/frontend/web-app/package.json',
        'src/frontend/browser-extension/manifest.json',
    ]
    
    for file_path in service_files:
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write('{\n  "name": "%s",\n  "version": "1.0.0"\n}' % os.path.basename(os.path.dirname(file_path)))
        print(f"Created: {full_path}")
    
    # Create Dockerfiles for services
    print("\�🐳 Creating Dockerfiles...")
    dockerfiles = [
        'src/backend/auth-service/Dockerfile',
        'src/backend/job-intelligence-service/Dockerfile',
        'src/backend/resume-service/Dockerfile',
        'src/backend/transparency-service/Dockerfile',
        'src/backend/application-service/Dockerfile',
        'src/backend/analytics-service/Dockerfile',
        'src/backend/api-gateway/Dockerfile',
        'src/frontend/web-app/Dockerfile',
    ]
    
    for dockerfile in dockerfiles:
        full_path = os.path.join(base_path, dockerfile)
        with open(full_path, 'w') as f:
            f.write(f"# {os.path.basename(os.path.dirname(dockerfile))} Dockerfile\nFROM node:18-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm install\nCOPY . .\nEXPOSE 3000\nCMD [\"npm\", \"start\"]")
        print(f"Created: {full_path}")
    
    print("\n" + "=" * 50)
    print("✅ Project structure created successfully!")
    print(f"📁 Location: {os.path.abspath(base_path)}")
    print("\n🎯 Next steps:")
    print("   1. cd into the project directory")
    print("   2. Review the generated structure")
    print("   3. Start implementing Phase 1 components")
    print("   4. Run 'docker-compose up' to start dependencies")

if __name__ == "__main__":
    # Get target directory from command line or use current directory
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "./careerlaunch-ai"
    
    try:
        create_structure(target_dir)
    except Exception as e:
        print(f"❌ Error creating structure: {e}")
        sys.exit(1)