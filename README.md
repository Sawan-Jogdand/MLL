# ML Snippet Backend

Minimal FastAPI backend for returning code snippets as plain text. Snippets are never executed.

- Put your code files manually inside `backend/snippets/`
- The API serves them by filename
- The raw endpoint returns the code text
- The Windows terminal command copies it to the clipboard without executing it

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

## Fetch a snippet

```bash
curl http://localhost:8000/api/snippets/code1
```

This prints the contents of `backend/snippets/code1.txt` as plain text. Use the same URL with `Invoke-WebRequest` to copy a snippet to a Windows clipboard.

## Copy to Windows clipboard

Paste this in PowerShell or CMD on a Windows machine:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -Command "$u = 'http://localhost:8000/api/snippets/code1'; $content = (Invoke-WebRequest -Uri $u -UseBasicParsing).Content; $content | Set-Clipboard; Write-Host 'Snippet copied to clipboard.'"
```

This does not run the code. It only copies it to the clipboard.

## Add your own snippets

Put any file in:

```text
backend/snippets/
```

Example:

```text
backend/snippets/code1.txt
backend/snippets/java.txt
backend/snippets/sql.txt
```

Then call:

```text
http://localhost:8000/api/snippets/java
```

Snippet names may contain only letters, numbers, underscores, and hyphens. The service rejects invalid names and returns 404 when the corresponding `.txt` file does not exist.

## Deploy to Vercel

1. Push this project to a Git provider supported by Vercel. Keep `backend/snippets/` in the repository; `vercel.json` includes those files in the serverless function.
2. In Vercel, choose **Add New → Project**, import the repository, and leave the project root at the repository root.
3. Deploy. Vercel detects `vercel.json` and installs the dependencies in `requirements.txt`.
4. Test the deployment using the URL Vercel assigns:

   ```text
   https://<your-vercel-domain>/api/snippets/code1
   ```

   The response is the raw contents of `backend/snippets/code1.txt` with a plain-text content type. Missing snippets return 404.

For recipients, use the deployed HTTPS URL in a PowerShell command:

```powershell
$url = "https://<your-vercel-domain>/api/snippets/code1"; (Invoke-WebRequest -Uri $url).Content | Set-Clipboard
```

This only copies the text to the clipboard. It does not execute the snippet. Deployment is not performed automatically by this project.
