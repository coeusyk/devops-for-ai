# DevOps for AI

This repository documents a DevOps learning journey, leveraging Jenkins via Docker instead of a traditional installer for a more streamlined and containerized setup. This approach allows for the use of Linux Shell scripts, as Docker containers are Linux-based.

## Customizations

The Dockerfile has been customized with the following enhancements:

- Installation of basic dependencies to support a wider range of operations.
- Addition of Python, which will be utilized for pipeline creation and management.
- Inclusion of Java, ensuring compatibility with Java-based tools and plugins.

## Installation

Refer to the following official Jenkins documentation link: [Installing Jenkins - Docker](https://www.jenkins.io/doc/book/installing/docker/)

> **Note**: Ensure that the `Dockerfile` is in the root directory of your project, which should be the current working directory when running Docker commands.
