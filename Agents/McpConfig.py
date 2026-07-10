import os

from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


def file_system_mcp_config():
    return McpWorkbench(StdioServerParams(command="/home/<username>/.nvm/versions/node/v22.23.1/bin/npx",
                                          args=[
                                              "-y",
                                              "@modelcontextprotocol/server-filesystem",
                                              str(os.getenv("directory_location"))
                                          ]
                                    ))