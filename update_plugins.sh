#!/bin/bash
set -e

REPO_DIR="$HOME/.gemini/repos/kennethsplugins"
PLUGINS_CONFIG_DIR="$HOME/.gemini/config/plugins"

echo "🔄 Opdaterer Kenneths plugins fra GitHub..."
cd "$REPO_DIR"

# Hent seneste version fra GitHub
git pull

# Sørg for at alle plugins (også eventuelle nye) er forbundet til Antigravity
echo "plugin.json" >> "$REPO_DIR/.git/info/exclude" 2>/dev/null || true

for plugin_path in "$REPO_DIR"/plugins/*; do
  if [ -d "$plugin_path" ]; then
    plugin_name=$(basename "$plugin_path")

    # Link plugin.json hvis den findes i .claude-plugin
    if [ -f "$plugin_path/.claude-plugin/plugin.json" ]; then
      ln -sf .claude-plugin/plugin.json "$plugin_path/plugin.json"
    fi

    # Link til Antigravity plugins
    ln -sfn "$plugin_path" "$PLUGINS_CONFIG_DIR/$plugin_name"
  fi
done

echo "✅ Alle plugins er opdateret og synkroniseret med Antigravity!"
