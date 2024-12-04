Usage Instructions for generate_plugin_files.py; this script generates dependency files for multiple programming languages by categorising dependencies into Java, Node.js, Python, and .NET. The script takes predefined dependency lists and writes them into language-specific file formats:

> Download the text file named plugins.txt

> Ensure each line contains a plugin name followed by a tab (\t) and its version.

> Save the script named generate_files.py

> Run the script in a Python environment:

``` python generate_files.py ```

The files pom.xml, package.json, and dependency.csproj will be generated in the current directory.
