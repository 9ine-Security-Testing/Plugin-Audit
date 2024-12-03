import os



# Dependencies divided by categories, changes to be made when dev team update any dependency version

java_dependencies = [

    "Selenium-java:4.13.0",

    "testng:7.7.1",

    "json-simple:1.1.1",

    "org.apache.poi:5.2.3",

    "poi-ooxml:5.2.3",

    "poi-ooxml-schemas:4.1.2",

    "poi-scratchpad:5.2.3",

    "log4j-api:3.0.0-alpha1",

    "extentreports:2.41.2",

    "sikuli-api:1.2.0",

    "io.rest-assured:5.3.2",

    "rest-assured-common:5.3.2",

    "commons-io:2.14.0",

    "javax.mail-api:1.6.2",

    "jsoup:1.16.1"

]



node_dependencies = [

    "jquery.min.js:3.6.4",

    "jquery-ui.min.js:1.13.1",

    "bootstrap.min.js:4.6.2",

    "moment.js:2.29.4",

    "bootstrap-table.min.js:1.21.0",

    "bootstrap-table-mobile.js:3.4.3",

    "bootstrap-table-resizable.min.js:1.21.0",

    "jquery.resizableColumns.min.js:0.1.0",

    "jquery.dragtable.js:2.0.15",

    "bootstrap-table-reorder-columns.min.js:1.21.0",

    "summernote-bs4.min.js:0.8.18",

    "google chart:2",

    "dhtmlxgantt.min.js:8.0.1",

    "bootstrap-select.min.js:1.13.9",

    "date-range-picker.js:3.1",

    "Userflow:-",

    "tagmanger:-",

    "termly:-",

    "html2canvas:1.4.1",

    "html2pdf:0.10.1",

    "tsparticles:3.0.3",

    "animate.css:4.1.1"

    "ngx-owl-carousel-o:14.0.1",

    "ng-image-slider:7.0.1",

    "ngx-bootstrap:5.2.3",

    "ngx-chips:3.0.0",

    "ngx-image-slider:2.0.2",

    "ngx-infinite-scroll:10.0.1",

    "ngx-summernote:0.9.0",

    "ngx-toaster:15.2.2",

    "oidc-client:1.11.5",

    "popper.js:1.16.0",

    "summernote:0.8.20",

    "vimeo-player:2.24.0"

]



python_dependencies = [

    "SendGrid==9.28.1",

    "Azure.Storage.Blobs==12.16.0",

    "Microsoft.Data.SqlClient==5.1.1",

    "Microsoft.EntityFrameworkCore==6.0.0",

    "Microsoft.ApplicationInsights.AspNetCore==2.14.0",

    "AutoMapper==12.0.1",

    "Newtonsoft.Json==13.0.3"

]



dotnet_dependencies = [

    "Microsoft.ApplicationInsights.AspNetCore:2.14.0",

    "Microsoft.AspNetCore.Identity:2.2.0",

    "Microsoft.Build:16.5.0",

    "Microsoft.EntityFrameworkCore.Proxies:6.0.0",

    "Microsoft.EntityFrameworkCore.SqlServer:6.0.0",

    "Microsoft.EntityFrameworkCore.Tools:6.0.0",

    "Microsoft.Extensions.Configuration.Abstractions:6.0.0",

    "Microsoft.Extensions.DependencyInjection:6.0.0",

    "Microsoft.Extensions.Logging.ApplicationInsights:2.14.0",

    "Microsoft.Extensions.Logging.Debug:3.1.4",

    "Microsoft.FeatureManagement.AspNetCore:2.5.1",

    "Microsoft.VisualStudio.Web.CodeGeneration.Design:3.1.5",

    "MSBuild.SonarQube.Runner.Tool:4.8.0",

    "Serilog:2.9.0",

    "Serilog.AspNetCore:3.2.0",

    "Serilog.Exceptions:5.5.0",

    "Serilog.Sinks.File:4.1.0",

    "Serilog.Sinks.RollingFile:3.3.0",

    "Serilog.Sinks.RollingFile.Extension:2.0.2",

    "SonarAnalyzer.CSharp:8.56.0.67649",

    "WebCompiler:1.0.1",

    "WindowsAzure.Storage:9.3.3",

    "Microsoft.Azure.Functions.Extensions:1.1.0",

    "Microsoft.Azure.WebJobs.Extensions.DurableTask:2.9.3",

    "Microsoft.Azure.WebJobs.Extensions.ServiceBus:5.12.0",

    "Microsoft.Azure.WebJobs.Extensions.Storage:5.2.1",

    "Microsoft.Extensions.Configuration.CommandLine:3.1.5",

    "Microsoft.Extensions.Configuration.EnvironmentVariables:3.1.5",

    "Microsoft.Extensions.Configuration.Json:3.1.5",

    "Microsoft.NET.Sdk.Functions:4.1.1",

    "CsvHelper:30.0.1",

    "Microsoft.AspNetCore.DataProtection.Abstractions:7.0.5",

    "Microsoft.AspNetCore.Http.Features:5.0.17",

    "Microsoft.Azure.Storage.Blob:11.2.3",

    "SonarAnalyzer.CSharp:8.56.0.67649",

    "System.Configuration.ConfigurationManager:7.0.0",

    "Azure.Storage.Blobs:12.16.0",

    "DocumentFormat.OpenXml:2.20.0",

    "Microsoft.Azure.Cosmos:3.41.0",

    "Microsoft.Azure.Storage.Common:11.2.3",

    "Microsoft.Data.SqlClient:5.1.1",

    "Microsoft.Extensions.Configuration.Binder:3.1.5",

    "MSBuild.SonarQube.Runner.Tool:4.8.0",

    "GemBox.Spreadsheet:49.0.1335",

    "Microsoft.ApplicationInsights.AspNetCore:2.14.0",

    "Microsoft.AspNetCore.Authentication.Cookies:2.2.0",

    "Microsoft.AspNetCore.Http.Abstractions:2.2.0",

    "Microsoft.AspNetCore.Mvc.Razor:2.2.0",

    "SendGrid:9.28.1",

    "Microsoft.AspNetCore.SpaServices:3.1.0",

    "Microsoft.AspNetCore.SpaServices.Extensions:6.0.1",

    "Microsoft.EntityFrameworkCore:6.0.0",

    "Microsoft.EntityFrameworkCore.Relational:6.0.0",

    "Microsoft.EntityFrameworkCore.SqlServer:6.0.0",

    "Newtonsoft.Json:13.0.3",

    "Devlooped.CloudStorageAccount:1.1.0",

    "System.Data.SqlClient:4.8.5",

    "Newtonsoft.Json.Bson:1.0.2",

    "Open-XML-SDK:2.9.1",

    "AutoMapper:12.0.1",

    "AutoMapper.Extensions.Microsoft.DependencyInjection:6.0.0",

    "BundlerMinifier.Core:3.2.449",

    "Microsoft.AspNetCore.Authentication.JwtBearer:3.1.28",

    "Microsoft.AspNetCore.Mvc.Razor.RuntimeCompilation:3.1.28",

    "Microsoft.Build:17.3.1",

    "Microsoft.Build.Framework:17.3.1",

    "Microsoft.Build.Utilities.Core:17.2.0",

    "Microsoft.Extensions.Configuration.Abstractions:6.0.0",

    "Microsoft.Extensions.Identity.Core:6.0.8",

    "Microsoft.Extensions.Logging.ApplicationInsights:2.21.0",

    "Microsoft.Extensions.Logging.Debug:6.0.0",

    "Serilog:2.11.0",

    "Serilog.AspNetCore:6.0.1",

    "Serilog.Exceptions:8.4.0",

    "Serilog.Sinks.ApplicationInsights:4.0.0",

    "Serilog.Sinks.File:5.0.0",

    "Serilog.Sinks.RollingFile:3.3.0",

    "Serilog.Sinks.RollingFile.Extension:2.0.2",

    "SonarAnalyzer.CSharp:8.44.0.52574",

    "Microsoft.AspNetCore.Mvc.Core:2.2.5",

    "Azure.Storage.Blobs:12.13.1",

    "Azure.Storage.Common:12.12.0",

    "Microsoft.Data.SqlClient:5.0.0"

]



# File paths

output_dir = "/home/kali/9ine/Plugin_Audit/test"

java_dependencies_path = os.path.join(output_dir, "pom.xml")

node_dependencies_path = os.path.join(output_dir, "package.json")

python_dependencies_path = os.path.join(output_dir, "requirements.txt")

dotnet_dependencies_path = os.path.join(output_dir, "packages.config")



# Ensure the output directory exists

os.makedirs(output_dir, exist_ok=True)



# Function to write dependencies and return count

def write_dependencies(file_path, dependencies, formatter):

    count = 0

    with open(file_path, 'w') as file:

        count = formatter(file, dependencies)

    return count



# Formatters for each dependency type

def format_java(file, dependencies):

    count = 0

    file.write("<dependencies>\n")

    for dep in dependencies:

        try:

            name, version = dep.split(':')

            file.write(f"  <dependency>\n    <groupId>{name}</groupId>\n    <artifactId>{name}</artifactId>\n    <version>{version}</version>\n  </dependency>\n")

            count += 1

        except ValueError:

            print(f"Skipping invalid Java dependency: {dep}")

    file.write("</dependencies>\n")

    return count



def format_node(file, dependencies):

    count = 0

    file.write("{\n  \"dependencies\": {\n")

    for dep in dependencies:

        try:

            name, version = dep.split(':')

            file.write(f"    \"{name}\": \"{version}\",\n")

            count += 1

        except ValueError:

            print(f"Skipping invalid Node.js dependency: {dep}")

    file.write("  }\n}\n")

    return count



def format_python(file, dependencies):

    count = len(dependencies)

    file.write("\n".join(dependencies))

    return count



def format_dotnet(file, dependencies):

    count = 0

    file.write("<packages>\n")

    for dep in dependencies:

        try:

            name, version = dep.split(':')

            file.write(f"  <package id=\"{name}\" version=\"{version}\" />\n")

            count += 1

        except ValueError:

            print(f"Skipping invalid .NET dependency: {dep}")

    file.write("</packages>\n")

    return count



# Write dependencies and count them

java_count = write_dependencies(java_dependencies_path, java_dependencies, format_java)

node_count = write_dependencies(node_dependencies_path, node_dependencies, format_node)

python_count = write_dependencies(python_dependencies_path, python_dependencies, format_python)

dotnet_count = write_dependencies(dotnet_dependencies_path, dotnet_dependencies, format_dotnet)



# Print summary

print("Dependencies have been written:")

print(f"Java dependencies (pom.xml): {java_count}")

print(f"Node.js dependencies (package.json): {node_count}")

print(f"Python dependencies (requirements.txt): {python_count}")

print(f".NET dependencies (packages.config): {dotnet_count}")



