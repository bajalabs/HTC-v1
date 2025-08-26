<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# File Download Location in Docker and Playwright MCP

When you download files using Docker and Playwright MCP, the files are saved in **temporary directories** within the Docker container. Here's what you need to know about where these files are stored:

## Default Download Locations

**Inside the Docker Container:**

- Downloaded files are stored in a temporary directory, typically `/tmp/playwright-artifacts-<random-id>/`[^1][^2]
- Each download gets a unique temporary path like `/tmp/playwright-artifacts-zUHKYv/ab49a46d-cdcb-46fb-bd5a-8695661713e3`[^1]
- These temporary files are automatically deleted when the browser context that created them is closed[^3]

**Container Temporary Directory:**

- Docker containers use `/tmp` as the default temporary directory for file operations[^4]
- The specific Playwright temporary artifacts folder is created within this `/tmp` directory[^1]


## Accessing Downloaded Files

There are several ways to access your downloaded files:

### 1. Using Playwright's Download API

When handling downloads in Playwright MCP, you can:

- Use `download.path()` to get the temporary file path[^3]
- Use `download.saveAs(targetPath)` to save the file to a specific location[^3]
- Access `download.suggestedFilename()` to get the original filename[^1]


### 2. Volume Mounting

To persist downloaded files outside the container, you need to mount a volume:

```bash
docker run -v /host/download/path:/container/download/path your-playwright-image
```


### 3. Configuring Download Directory

You can specify a custom downloads directory when launching the browser:

```javascript
const browser = await playwright.chromium.launch({
    downloadsPath: '/app/downloads'  // Custom download directory
});
```


## Important Considerations

**Temporary Nature:**

- Files in `/tmp/playwright-artifacts-*` directories are temporary and will be deleted when the browser context closes[^3]
- If you need to preserve downloads, you must either save them to a mounted volume or copy them before the context closes

**Docker Container Isolation:**

- Files downloaded inside a Docker container are isolated from the host system unless you explicitly mount volumes[^5]
- Without volume mounting, downloads exist only within the container's filesystem

**MCP Server Limitations:**

- Currently, some Playwright MCP implementations don't provide direct access to download file contents[^6]
- There are ongoing efforts to add tools like `browser_downloads_list` and `browser_file_download` to access downloaded files through MCP[^6]


## Best Practices

1. **Mount a Volume:** If you need to access downloaded files from the host system, mount a volume to the container's download directory
2. **Save Files Explicitly:** Use `download.saveAs()` to save files to a persistent location before the browser context closes
3. **Monitor Disk Space:** Temporary files can accumulate, so ensure adequate disk space in `/tmp`[^4]

The exact location depends on your specific Docker setup and how you've configured the Playwright MCP server, but the temporary directory pattern (`/tmp/playwright-artifacts-*`) is consistent across implementations.
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://stackoverflow.com/questions/77869473/suggestedfilename-in-playwright-docker-is-not-set-correctly-default-to-downl

[^2]: https://stackoverflow.com/questions/79339560/playwright-python-download-get-temporary-file

[^3]: https://playwright.dev/docs/downloads

[^4]: https://stackoverflow.com/questions/44010124/where-does-docker-store-its-temp-files-during-extraction

[^5]: https://www.reddit.com/r/docker/comments/16w4ghi/where_are_my_downloads_located/

[^6]: https://github.com/microsoft/playwright-mcp/issues/154

[^7]: https://hub.docker.com/mcp/server/playwright/manual

[^8]: https://github.com/iuill/playwright-mcp-docker

[^9]: https://stackoverflow.com/questions/79628847/how-do-i-set-the-default-download-path-in-playwright-and-c-sharp

[^10]: https://playbooks.com/mcp/playwright-browser-automation

[^11]: https://hub.docker.com/mcp/server/playwright-mcp-server

[^12]: https://github.com/microsoft/playwright/issues/31316

[^13]: https://lobehub.com/mcp/hyhfish-playwright-mcp

[^14]: https://blog.devops.dev/integrating-playwright-in-ci-with-github-actions-and-docker-7baafe76de99

[^15]: https://playwright.dev/docs/docker

[^16]: https://testgrid.io/blog/playwright-testing-with-docker/

[^17]: https://scrapingant.com/blog/playwright-download-file

[^18]: https://glama.ai/mcp/servers/@torohash/playwright-sse-mcp-server

[^19]: https://www.pragnakalp.com/dockerizing-playwright-for-seamless-web-scraping/

[^20]: https://executeautomation.github.io/mcp-playwright/docs/local-setup/Installation

[^21]: https://hub.docker.com/r/microsoft/playwright

[^22]: https://www.npmjs.com/package/@executeautomation/playwright-mcp-server

[^23]: https://docs.getxray.app/display/XRAYCLOUD/Containerize+Playwright+tests+with+Docker

[^24]: https://ray.run/discord-forum/threads/86361-install-in-docker-container

[^25]: https://lobehub.com/mcp/microsoft-playwright-mcp-patch

[^26]: https://github.com/microsoft/playwright-java/issues/1815

[^27]: https://dev.to/debs_obrien/install-playwright-mcp-server-in-vs-code-4o91

[^28]: https://www.youtube.com/watch?v=exsikHe20D8

[^29]: https://learn.microsoft.com/en-us/answers/questions/1325862/temporary-files-in-docker-on-azure-k8s

[^30]: https://forums.docker.com/t/docker-compose-scheduled-temporary-tar-file-in-tmp/118730

[^31]: https://forums.docker.com/t/where-are-images-stored/9794

[^32]: https://lobehub.com/es/mcp/iuill-playwright-mcp-docker

[^33]: https://github.com/docker/scout-cli/issues/42

[^34]: https://www.lambdatest.com/automation-testing-advisor/csharp/classes/Microsoft.Playwright.Tests.TempDirectory

[^35]: https://playwright.dev/python/docs/docker

[^36]: https://github.com/microsoft/playwright-java/issues/1268

