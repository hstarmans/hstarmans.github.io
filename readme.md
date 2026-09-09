# Hexastorm Website Source

Source repository for the official Hexastorm documentation and project website ([hexastorm.com](https://hexastorm.com)).

## Development Setup

The website is built with [Quarto](https://quarto.org/).

1. **Install Quarto Iconify Extension**:
   ```bash
   quarto add mcanouil/quarto-iconify
   ```

2. **Run Local Preview Server**:
   ```bash
   quarto preview
   ```

3. **Build & Render Entire Site**:
   ```bash
   quarto render
   ```

## Deployment

The website publishes directly to GitHub Pages:
```bash
quarto publish gh-pages
```

Custom domain is managed via the `CNAME` file pointing to `hexastorm.com`.