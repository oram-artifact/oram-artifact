# Artifact

[![check-artifact](https://github.com/oram-artifact/oram-artifact/actions/workflows/check.yml/badge.svg)](https://github.com/oram-artifact/oram-artifact/actions/workflows/check.yml)

This repository hosts the artifact accompanying CCS'26 submission #3589. The
archive [`oram-security.tar.gz`](oram-security.tar.gz) is byte-for-byte
identical to the artifact already submitted for evaluation. Its build and usage
instructions are documented in the `README.md` inside the archive.

The purpose of this repository is to demonstrate that the proof checking is
reproducible.

## Continuous verification

The [`check-artifact`][runs] workflow checks that the proofs in the submitted
archive go through. It extracts
[`oram-security.tar.gz`](oram-security.tar.gz) and checks every proof inside the
official EasyCrypt container image, with all required SMT provers pre-installed.
A green badge above means every proof checks.

### Inspecting the log

Click the badge above (or open the [workflow runs page][runs]) and select a
run. Its **Summary** page shows the report inline: an overall pass/fail line, a
per-file table, and the raw `report.log` in a collapsible block. The same
`report.log` is also attached to each run as a downloadable artifact, and the
full console output is available under the run's job logs.

[runs]: https://github.com/oram-artifact/oram-artifact/actions/workflows/check.yml
