from daytona_sdk import Daytona, DaytonaConfig, SandboxTargetRegion
from daytona_sdk import Daytona, CreateSandboxParams
# Using environment variables (DAYTONA_API_KEY, DAYTONA_SERVER_URL, DAYTONA_TARGET)
daytona = Daytona()

# Using explicit configuration
config = DaytonaConfig(
    api_key="*******************",
    api_url="https://app.daytona.io/api",
    target=SandboxTargetRegion.US
)
daytona = Daytona(config)

def main():
    # Initialize the SDK (uses environment variables by default)
    daytona = Daytona()

    # Create a new sandbox
    sandbox = daytona.create(CreateSandboxParams(
        language="python",
        env_vars={"PYTHON_ENV": "development"}
    ))

    # Execute a command
    response = sandbox.process.exec("echo 'Hello, World!'")
    print(response.result)

if __name__ == "__main__":
    main()