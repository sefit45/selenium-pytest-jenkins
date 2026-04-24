# Kubernetes Automation Framework Deployment

This folder contains Kubernetes manifests for running the Selenium Pytest Jenkins Automation Framework in a Kubernetes-ready architecture.

## Components

- Selenium Hub Deployment
- Selenium Hub Service
- Chrome Node Deployment
- Firefox Node Deployment
- Pytest Runner Deployment
- ConfigMap for non-sensitive configuration
- Secret for sensitive API key management

## Architecture

```text
Pytest Runner Pod
        |
        v
Selenium Hub Service
        |
        v
Chrome Node Pods / Firefox Node Pods