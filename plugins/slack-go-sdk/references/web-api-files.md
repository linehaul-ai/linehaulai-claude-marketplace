# Web API: File Operations

## Uploading Files

### Basic File Upload

```go
params := slack.FileUploadParameters{
    File:     "/path/to/document.pdf",
    Channels: []string{"C1234567890"},
    Title:    "Monthly Report",
}

file, err := api.UploadFile(params)
if err != nil {
    return fmt.Errorf("failed to upload file: %w", err)
}

fmt.Printf("File uploaded: %s (ID: %s)\n", file.Name, file.ID)
```

### Upload with Initial Comment

```go
params := slack.FileUploadParameters{
    File:           "/path/to/screenshot.png",
    Channels:       []string{"C1234567890"},
    Title:          "Bug Screenshot",
    InitialComment: "Screenshot showing the layout issue on mobile",
}

file, err := api.UploadFile(params)
```

### Upload from Bytes

```go
import "bytes"

func uploadFileFromBytes(api *slack.Client, data []byte, filename, channelID string) error {
    params := slack.FileUploadParameters{
        Reader:   bytes.NewReader(data),
        Filename: filename,
        Channels: []string{channelID},
    }

    _, err := api.UploadFile(params)
    return err
}
```

### Upload to Multiple Channels

```go
params := slack.FileUploadParameters{
    File:     "/path/to/announcement.pdf",
    Channels: []string{"C111", "C222", "C333"},
    Title:    "Company Announcement",
}

file, err := api.UploadFile(params)
```

## Retrieving Files

### Get File Information

```go
file, _, _, err := api.GetFileInfo("F1234567890", 0, 0)
if err != nil {
    return err
}

fmt.Printf("Name: %s\n", file.Name)
fmt.Printf("Size: %d bytes\n", file.Size)
fmt.Printf("Type: %s\n", file.Filetype)
fmt.Printf("URL: %s\n", file.URLPrivateDownload)
```

### List Files

```go
params := slack.GetFilesParameters{
    Channel: "C1234567890",
    Count:   100,
}

files, paging, err := api.GetFiles(params)
if err != nil {
    return err
}

for _, file := range files {
    fmt.Printf("- %s (%s)\n", file.Name, file.ID)
}
```

### List Files by User

```go
params := slack.GetFilesParameters{
    User:  "U1234567890",
    Count: 50,
}

files, _, err := api.GetFiles(params)
```

## Downloading Files

### Download File Content

```go
import (
    "io"
    "net/http"
)

func downloadFile(fileURL, token, destPath string) error {
    req, err := http.NewRequest("GET", fileURL, nil)
    if err != nil {
        return err
    }

    req.Header.Set("Authorization", "Bearer "+token)

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        return err
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        return fmt.Errorf("download failed: %s", resp.Status)
    }

    out, err := os.Create(destPath)
    if err != nil {
        return err
    }
    defer out.Close()

    _, err = io.Copy(out, resp.Body)
    return err
}
```

## Deleting Files

### Delete Single File

```go
err := api.DeleteFile("F1234567890")
if err != nil {
    return fmt.Errorf("failed to delete file: %w", err)
}
```

## File Sharing

### Share File to Channel

```go
// Upload file privately first
params := slack.FileUploadParameters{
    File:  "/path/to/file.pdf",
    Title: "Document",
}

file, err := api.UploadFile(params)
if err != nil {
    return err
}

// Then share to channel
err = api.ShareFilePublicURLExternal(file.ID, "C1234567890")
```

## Multi-Part Uploads (Large Files)

### Upload Large File in Chunks

```go
func uploadLargeFile(api *slack.Client, filePath, channelID string) error {
    file, err := os.Open(filePath)
    if err != nil {
        return err
    }
    defer file.Close()

    fileInfo, err := file.Stat()
    if err != nil {
        return err
    }

    params := slack.FileUploadParameters{
        Reader:   file,
        Filename: filepath.Base(filePath),
        Filesize: int(fileInfo.Size()),
        Channels: []string{channelID},
    }

    _, err = api.UploadFile(params)
    return err
}
```

## Production Patterns

### Upload with Progress Tracking

```go
type ProgressReader struct {
    reader   io.Reader
    total    int64
    current  int64
    callback func(current, total int64)
}

func (pr *ProgressReader) Read(p []byte) (int, error) {
    n, err := pr.reader.Read(p)
    pr.current += int64(n)
    if pr.callback != nil {
        pr.callback(pr.current, pr.total)
    }
    return n, err
}

func uploadWithProgress(api *slack.Client, filePath, channelID string) error {
    file, err := os.Open(filePath)
    if err != nil {
        return err
    }
    defer file.Close()

    stat, err := file.Stat()
    if err != nil {
        return err
    }

    progressReader := &ProgressReader{
        reader: file,
        total:  stat.Size(),
        callback: func(current, total int64) {
            percent := float64(current) / float64(total) * 100
            fmt.Printf("\rUploading: %.1f%%", percent)
        },
    }

    params := slack.FileUploadParameters{
        Reader:   progressReader,
        Filename: filepath.Base(filePath),
        Filesize: int(stat.Size()),
        Channels: []string{channelID},
    }

    _, err = api.UploadFile(params)
    fmt.Println() // New line after progress
    return err
}
```

### Batch File Deletion

```go
func deleteOldFiles(api *slack.Client, beforeDate time.Time) error {
    params := slack.GetFilesParameters{
        TimestampTo: slack.JSONTime(beforeDate.Unix()),
        Count:       100,
    }

    files, _, err := api.GetFiles(params)
    if err != nil {
        return err
    }

    for _, file := range files {
        err := api.DeleteFile(file.ID)
        if err != nil {
            fmt.Printf("Warning: failed to delete %s: %v\n", file.Name, err)
            continue
        }
        fmt.Printf("Deleted: %s\n", file.Name)
        time.Sleep(time.Second) // Rate limiting
    }

    return nil
}
```

### Generate CSV and Upload

```go
func generateAndUploadReport(api *slack.Client, channelID string) error {
    // Create CSV buffer
    var buf bytes.Buffer
    writer := csv.NewWriter(&buf)

    // Write data
    writer.Write([]string{"Name", "Count", "Status"})
    writer.Write([]string{"Item 1", "42", "Active"})
    writer.Write([]string{"Item 2", "15", "Pending"})
    writer.Flush()

    // Upload
    params := slack.FileUploadParameters{
        Reader:   &buf,
        Filename: fmt.Sprintf("report_%s.csv", time.Now().Format("2006-01-02")),
        Filetype: "csv",
        Channels: []string{channelID},
        Title:    "Daily Report",
    }

    _, err := api.UploadFile(params)
    return err
}
```

## Common Pitfalls

1. **File size limits** - Slack has upload limits (check workspace settings)
2. **Not handling download authentication** - Use Bearer token for private files
3. **Missing file type** - Specify filetype for better preview
4. **Rate limits on bulk operations** - Implement delays between uploads/deletions
5. **Temporary URLs** - Download URLs expire, don't store them long-term
