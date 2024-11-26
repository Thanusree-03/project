using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace UrlShortenerApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UrlShortenerController : ControllerBase
    {
        private static Dictionary<string, string> urls = new Dictionary<string, string>();

        [HttpPost("shorten")]
        public IActionResult Shorten([FromBody] UrlRequest request)
        {
            var id = System.Guid.NewGuid().ToString().Substring(0, 6);
            var shortUrl = $"{Request.Scheme}://{Request.Host}/api/{id}";
            urls[id] = request.Url;
            return Ok(new { shortUrl });
        }

        [HttpGet("{id}")]
        public IActionResult RedirectToUrl(string id)
        {
            if (urls.ContainsKey(id))
            {
                return Redirect(urls[id]);
            }
            return NotFound();
        }
    }

    public class UrlRequest
    {
        public string Url { get; set; }
    }
}
