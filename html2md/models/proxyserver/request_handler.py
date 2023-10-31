import aiohttp
from aiohttp import web
import asyncio
import validators


async def proxy_handler(request):
    """
    Handles incoming requests from the clients, forwards the requests
    to the API, get the responses back from the API and forward them
    back to the clients.
    """
    userUrl = request.query.get('url', '')
    print(f"Received request for URL: {userUrl}")
    
    if validators.url(userUrl):
        apiUrl = f"http://127.0.0.1:5000/convert/url/{userUrl}"
        async with aiohttp.ClientSession() as session: 
            try:
                async with session.get(apiUrl) as response:
                    headers = dict(response.headers)
                    markdown = await response.text()
                    response_text = f"Headers: {headers}\n\nText: {markdown}"
                    return web.Response(text=response_text)
                   
                
            except aiohttp.ClientError as e:
                return web.json_response({"error": str(e)}, status=502)  
    
    else:
        return web.Response(text="Invalid URL. Please provide a complete URL with scheme and domain.", status=400)
        
async def main():
    app = web.Application() 
    app.router.add_get('/resource', proxy_handler)
    return app
    
    
if __name__ == "__main__":
    app = asyncio.get_event_loop().run_until_complete(main())
    web.run_app(app)
