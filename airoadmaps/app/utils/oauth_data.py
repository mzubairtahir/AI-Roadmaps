import httpx

async def get_user_detail(access_token: str):
    """
    Fetches user details from Google's OAuth2 token info endpoint using the provided access token.

    Args:
        access_token (str): The access token used to fetch user details.

    Returns:
        dict | None: The user data if successful, otherwise None.
    """
    endpoint = 'https://oauth2.googleapis.com/tokeninfo'
    headers = {'Authorization': f'Bearer {access_token}'}

    async with httpx.AsyncClient() as client:
        try:
            # Make the request to fetch user details
            response = await client.get(url=endpoint, params={'id_token': access_token})

            # Check if the response is successful
            if response.is_success:
                return response.json()

            return None
        except httpx.HTTPStatusError:
            # Handle specific HTTP status errors
            return None
        except Exception:
            # General exception handling for any unforeseen errors
            return None
