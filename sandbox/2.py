from daytona_sdk import Daytona, DaytonaConfig

# Define the configuration
config = DaytonaConfig(
    api_key="*******************",
    api_url="https://app.daytona.io/api",
    target="asia"
)
# Initialize the Daytona client
daytona = Daytona(config)

# Create the Sandbox instance
sandbox = daytona.create()

# Run the code securely inside the Sandbox
response = sandbox.process.code_run('print("Hello World from code!")')
if response.exit_code != 0:
  print(f"Error: {response.exit_code} {response.result}")
else:
    print(response.result)

# Clean up
daytona.remove(sandbox)