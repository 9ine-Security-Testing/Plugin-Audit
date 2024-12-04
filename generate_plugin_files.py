import os

def generate_files(input_file):
    # Define file paths
    pom_path = "pom.xml"
    package_json_path = "package.json"
    csproj_path = "dependency.csproj"

    # Prepare structures
    maven_dependencies = []
    npm_dependencies = []
    csproj_dependencies = []

    # Read input file
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  # Remove extra spaces and newline characters
            if not line:  # Skip blank lines
                continue
            try:
                plugin, version = line.split('\t')
                plugin = plugin.strip()
                version = version.strip()

                # Categorize plugins
                if "maven" in plugin.lower() or plugin.startswith("javax.") or plugin.startswith("org."):
                    maven_dependencies.append((plugin, version))
                elif ".js" in plugin or plugin.startswith("ngx") or plugin.startswith("jquery"):
                    npm_dependencies.append((plugin, version))
                else:
                    csproj_dependencies.append((plugin, version))
            except ValueError:
                print(f"Skipping invalid line: {line}")
                continue

    # Generate pom.xml
    with open(pom_path, 'w') as pom:
        pom.write('<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">\n')
        pom.write('<modelVersion>4.0.0</modelVersion>\n<dependencies>\n')
        for plugin, version in maven_dependencies:
            pom.write(f'  <dependency>\n    <groupId>{plugin}</groupId>\n    <artifactId>{plugin}</artifactId>\n    <version>{version}</version>\n  </dependency>\n')
        pom.write('</dependencies>\n</project>\n')

    # Generate package.json
    with open(package_json_path, 'w') as package_json:
        package_json.write('{\n  "dependencies": {\n')
        for plugin, version in npm_dependencies:
            package_json.write(f'    "{plugin}": "{version}",\n')
        if npm_dependencies:
            package_json.seek(package_json.tell() - 2, os.SEEK_SET)  # Remove the last comma
        package_json.write('\n  }\n}\n')

    # Generate .csproj file
    with open(csproj_path, 'w') as csproj:
        csproj.write('<Project Sdk="Microsoft.NET.Sdk">\n  <PropertyGroup>\n    <OutputType>Exe</OutputType>\n    <TargetFramework>net6.0</TargetFramework>\n  </PropertyGroup>\n  <ItemGroup>\n')
        for plugin, version in csproj_dependencies:
            csproj.write(f'    <PackageReference Include="{plugin}" Version="{version}" />\n')
        csproj.write('  </ItemGroup>\n</Project>\n')

    print(f"Files generated: {pom_path}, {package_json_path}, {csproj_path}")

# Usage
generate_files('plugins.txt')
