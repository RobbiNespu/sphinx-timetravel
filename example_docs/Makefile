# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
PAPER         ?=
BUILDDIR      ?= _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
.PHONY: help Makefile

# Put it first so that "make" without argument is called with help first.
help:
	@$(SPHINXBUILD) -M help . $(BUILDDIR) $(ALLSPHINXOPTS) 2>&1 | grep -E '^[a-zA-Z_-]+:' || true

.DEFAULT_GOAL := help

%: Makefile
	@$(SPHINXBUILD) -M $@ . $(BUILDDIR) $(ALLSPHINXOPTS)

html:
	@$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML files are in $(BUILDDIR)/html."

clean:
	rm -rf $(BUILDDIR)

.PHONY: html clean
