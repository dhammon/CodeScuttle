
class ResponseLimit:
    url = 'https://api.github.com/search/code?q=%22checkAccountNumber%22%20%22enumerateAccounts%22'
    headers = {'Server': 'GitHub.com', 'Date': 'Sun, 05 Feb 2023 19:39:57 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'X-OAuth-Scopes': 'admin:enterprise, admin:gpg_key, admin:org, admin:org_hook, admin:public_key, admin:repo_hook, delete:packages, delete_repo, gist, notifications, repo, user, workflow, write:discussion, write:packages', 'X-Accepted-OAuth-Scopes': 'repo', 'X-GitHub-Media-Type': 'github.v3; format=json', 'x-github-api-version-selected': '2022-11-28', 'X-RateLimit-Limit': '30', 'X-RateLimit-Remaining': '24', 'X-RateLimit-Reset': '1675626041', 'X-RateLimit-Used': '6', 'X-RateLimit-Resource': 'search', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Vary': 'Accept-Encoding, Accept, X-Requested-With', 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': 'AC71:209D:351302:36BA4F:63E0060D'}
    content = b'{\n  "documentation_url": "https://docs.github.com/en/free-pro-team@latest/rest/overview/resources-in-the-rest-api#secondary-rate-limits",\n  "message": "Some rate limit hit That I Made Up."\n}\n'