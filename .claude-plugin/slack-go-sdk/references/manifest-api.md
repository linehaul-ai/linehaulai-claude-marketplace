# Manifest API

## Creating App Manifest

```go
manifest := &slack.Manifest{
    DisplayInformation: slack.ManifestDisplayInformation{
        Name:            "My Bot",
        Description:     "Helpful Slack bot",
        BackgroundColor: "#2c2d30",
    },
    Features: slack.ManifestFeatures{
        BotUser: &slack.ManifestBotUser{
            DisplayName:  "mybot",
            AlwaysOnline: true,
        },
        SlashCommands: []slack.ManifestSlashCommand{
            {
                Command:     "/deploy",
                Description: "Deploy application",
                UsageHint:   "environment version",
            },
        },
    },
    OAuthConfig: slack.ManifestOAuthConfig{
        RedirectURLs: []string{"https://myapp.com/oauth/callback"},
        Scopes: slack.ManifestOAuthScopes{
            Bot: []string{"chat:write", "channels:read"},
        },
    },
    Settings: slack.ManifestSettings{
        EventSubscriptions: &slack.ManifestEventSubscriptions{
            BotEvents: []string{"message.channels", "app_mention"},
        },
        Interactivity: &slack.ManifestInteractivity{
            IsEnabled: true,
        },
    },
}

createdManifest, err := api.CreateManifest(manifest)
```

## Updating Manifest

```go
updatedManifest, err := api.UpdateManifest(appID, manifest)
```

## Exporting Manifest

```go
manifest, err := api.ExportManifest(appID)
```

## Best Practices

1. Version control manifests
2. Use manifest for consistent app configuration
3. Automate deployment with manifest API
4. Test manifests in dev workspace first
