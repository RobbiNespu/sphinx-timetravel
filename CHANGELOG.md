# Changelog

All notable changes to the sphinx-timetravel project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- LaTeX/PDF output support
- Interactive JavaScript timeline
- More color themes
- Custom event markers/icons
- Timeline filtering by date range

## [0.1.0] - 2024-11-11

### Added
- Initial release of sphinx-timetravel
- Vertical timeline layout with chronological display
- Horizontal timeline layout with SVG year axis
- Support for year/month resolution (YYYY and YYYY-MM formats)
- Responsive design for mobile, tablet, and desktop
- Interactive hover effects and animations
- Customizable timeline height and width
- Event titles, descriptions, and date labels
- CSS styling with gradient timeline axis
- Complete documentation with examples
- Example documentation with vertical, horizontal, and advanced timelines
- MIT License

### Features
- **Vertical Timeline**: Classic chronological layout with alternating left/right positioning
- **Horizontal Timeline**: Year-based SVG visualization with event markers
- **Flexible Formatting**: Support for YYYY or YYYY-MM date specifications
- **Responsive**: Mobile-friendly with automatic layout adjustments
- **Styled**: Professional appearance with smooth animations
- **Well-documented**: Comprehensive README and example files

### Project Files
- `sphinx_timetravel/` - Main plugin package
  - `__init__.py` - Extension setup and registration
  - `timeline.py` - Timeline directive and HTML generation
  - `_static/timeline.css` - Styling and responsive design
- `example_docs/` - Example Sphinx documentation
  - `conf.py` - Sphinx configuration
  - `index.rst` - Getting started guide
  - `vertical_timeline.rst` - Vertical timeline examples
  - `horizontal_timeline.rst` - Horizontal timeline examples
  - `advanced_examples.rst` - Complex use cases
- `setup.py` - Package configuration
- `pyproject.toml` - Modern Python packaging
- `MANIFEST.in` - Distribution manifest
- `README.md` - User documentation
- `LICENSE` - MIT License
- `PUBLISHING.md` - Publishing guide
- `.gitignore` - Git ignore patterns

## Semantic Versioning

- **MAJOR** (e.g., 1.0.0): Breaking changes
- **MINOR** (e.g., 0.1.0): New features, backwards compatible
- **PATCH** (e.g., 0.1.1): Bug fixes, backwards compatible

## Future Roadmap

### 0.2.0 (Planned)
- [ ] LaTeX/PDF support
- [ ] More timeline themes
- [ ] JavaScript interactivity
- [ ] Custom event icons
- [ ] Date range filtering

### 0.3.0 (Planned)
- [ ] Animation options
- [ ] Event grouping
- [ ] Multi-language support
- [ ] Export to image formats

### 1.0.0 (Planned)
- Stable API
- Full test coverage
- Performance optimizations
- Enterprise features

## Contributing

See README.md for contribution guidelines.

## Support

For issues, questions, or feedback:
- GitHub Issues: https://github.com/robbinespu/sphinx-timetravel/issues
- GitHub Discussions: https://github.com/robbinespu/sphinx-timetravel/discussions

## License

MIT License - See LICENSE file for details
