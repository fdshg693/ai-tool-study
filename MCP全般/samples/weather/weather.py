from typing import Any
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")


async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    return {"forecast": "Sunny with a chance of rain."}


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """

    forecast_data = await make_nws_request("test_url")

    if forecast_data is not None:
        return forecast_data.get("forecast", "No forecast available.")
    else:
        return "No forecast available."


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
