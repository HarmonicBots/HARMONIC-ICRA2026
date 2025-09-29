# HARMONIC ICRA 2026 - Assets Directory Structure

This directory contains all the media files, documents, and assets for the HARMONIC ICRA 2026 webpage.

## Directory Structure

```
assets/
├── images/
│   ├── architecture/          # System architecture diagrams and figures
│   │   ├── harmonic_architecture.png
│   │   ├── ontoagent_diagram.png
│   │   └── behavior_tree_diagram.png
│   └── results/               # Experimental results and visualizations
│       ├── evaluation_metrics.png
│       ├── performance_charts.png
│       └── comparison_plots.png
├── videos/
│   └── demos/                 # Demo videos and presentations
│       ├── main_demo.mp4      # 3-minute main presentation video
│       ├── tactical_demo.mp4  # Tactical component demonstration
│       ├── evaluation_demo.mp4 # Evaluation results video
│       └── system_overview.mp4 # System overview video
├── files/
│   └── papers/                # Paper documents and supplementary materials
│       ├── paper.pdf          # Main paper PDF
│       ├── supplementary.pdf  # Supplementary material
│       └── bibtex.txt         # BibTeX citation file
└── README.md                  # This file
```

## File Naming Conventions

### Images
- Use descriptive names with underscores: `harmonic_architecture.png`
- Include resolution in filename if multiple versions: `diagram_high_res.png`, `diagram_web.png`
- Use PNG for diagrams, JPG for photos, SVG for scalable graphics

### Videos
- Use descriptive names: `main_demo.mp4`, `tactical_component.mp4`
- Keep file sizes reasonable for web (under 50MB recommended)
- Use MP4 format for maximum compatibility
- Consider creating compressed versions for web: `demo_compressed.mp4`

### Files
- Use clear, descriptive names: `paper.pdf`, `supplementary_material.pdf`
- Include version numbers if needed: `paper_v1.pdf`, `paper_final.pdf`

## Recommended File Specifications

### Images
- **Architecture diagrams**: 1200x800px minimum, PNG format
- **Results plots**: 1000x600px minimum, PNG format
- **Screenshots**: Original resolution, PNG format
- **File size**: Under 2MB per image for web optimization

### Videos
- **Main demo**: 3-5 minutes, 1920x1080 resolution
- **Component demos**: 1-2 minutes, 1280x720 resolution
- **Format**: MP4 with H.264 codec
- **File size**: Under 100MB per video

### Documents
- **Paper PDF**: High quality, under 10MB
- **Supplementary**: Under 20MB
- **BibTeX**: Plain text format

## Usage in HTML

Update the following paths in `index.html`:

```html
<!-- Main demo video -->
<source src="assets/videos/demos/main_demo.mp4" type="video/mp4">

<!-- Architecture diagram -->
<img src="assets/images/architecture/harmonic_architecture.png" alt="HARMONIC System Architecture">

<!-- Paper link -->
<a href="assets/files/papers/paper.pdf" target="_blank" class="citation-button">
```

## File Organization Tips

1. **Keep original files**: Store high-resolution originals separately
2. **Web optimization**: Create web-optimized versions for faster loading
3. **Backup**: Keep backups of all assets
4. **Version control**: Use descriptive filenames to track versions
5. **Accessibility**: Include alt text and captions for all media

## Current Status

- [ ] Main demo video (3-minute presentation)
- [ ] Architecture diagram
- [ ] Tactical component demo video
- [ ] Evaluation results video
- [ ] Paper PDF
- [ ] Supplementary materials
- [ ] BibTeX citation file

## Notes

- All paths in the HTML are relative to the project root
- Ensure all files are properly optimized for web delivery
- Test all links and media files before final submission
- Consider using a CDN for large video files in production
